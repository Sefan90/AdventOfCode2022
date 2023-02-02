class Node():
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position

def part1():
    file = [[c for c in r.replace("\n","")] for r in open('input.txt','r')]
    start = Node((0,0))
    end = Node((0,0))
    for i in range(len(file)):
        for j in range(len(file[i])):
            if file[i][j] == "S":
                start = Node(None,(i,j))
                start.g = start.h = start.f = 0
            elif file[i][j] == "E":
                end = Node(None,(i,j))
                end.g = end.h = end.f = 0
    openList = []
    closedList = []
    openList.append(start)

    while len(openList) > 0:
        current_node = openList[0]
        current_index = 0
        for index, item in enumerate(openList):
            if item.f == current_node.f:
                current_node = item
                current_index = index

        openList.pop(current_index)
        closedList.append(current_node)

        if current_node == end:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1]

        children = []
        for new_pos in [(0,-1),(0,1),(-1,0),(1,0)]:
            node_pos = (current_node.position[0] + new_pos[0], current_node.position[1] + new_pos[1])
            if node_pos[0] > (len(file)-1) or node_pos[0] < 0 or node_pos[1] > (len(file[len(file)-1])-1) or node_pos[1] < 0:
                continue
            if ord(file[node_pos[0]][node_pos[1]]) > ord(file[current_node.position[0]][current_node.position[1]])+1 and file[node_pos[0]][node_pos[1]] != "E" and file[current_node.position[0]][current_node.position[1]] != "z" and file[current_node.position[0]][current_node.position[1]] != "S":
                continue
            if file[node_pos[0]][node_pos[1]] == "E" and file[current_node.position[0]][current_node.position[1]] != "z":
                continue
            if Node(current_node, node_pos) in closedList:
                continue
            new_node = Node(current_node, node_pos)
            children.append(new_node)

        for child in children:
            for closedChild in closedList:
                if child == closedChild:
                    continue
            child.g = current_node.g + 1
            child.h = ((child.position[0] + end.position[0])**2) + ((child.position[1] + end.position[1])**2)
            child.f = child.g + child.h

            for openNode in openList:
                if child == openNode and child.g >openNode.g:
                    continue

            openList.append(child)
    
print(len(part1())-1)