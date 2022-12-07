from pathlib import Path

class Node(object):
    "Generic tree node"
    def __init__(self, name = "/", size = 0, children = None):
        self.parent = None
        self.name = name
        self.size = size
        self.children = []
        if children is not None:
            for child in children:
                self.add_child(child)

    def __repr__(self) -> str:
        return self.name

    def add_child(self, node):
        assert isinstance(node, Node)
        # set parent to this instance for new node
        node.parent = self
        self.children.append(node)

    def find_node(self, name):
        for node in self.children:
            if node.name == name:
                return node
        return None

    def get_sum(self):
        sum = 0
        for child_node in self.children:
            if child_node.size == 0:
                sum += child_node.get_sum()
            sum += child_node.size
        return sum

def parse_command(line):
    cmd_segments = line[2:].split(' ')
    cmd = cmd_segments[0]
    arg = ""
    if len(cmd_segments) == 2:
        arg = cmd_segments[1]
    return (cmd, arg)

def build_tree(input_values):
    tree = Node("/")
    current_node = tree
    for line in input_values:
        if line[0] == '$':
            # command
            cmd = parse_command(line)
            process = cmd[0]
            process_arg = cmd[1]
            if process == "cd":
                if process_arg == "..":
                    # move to parent
                    current_node = current_node.parent
                else:
                    if process_arg != "/": # skip root as this has already been added
                        # switch directory
                        dir_name = process_arg
                        current_node = current_node.find_node(dir_name)
        else:
            # dir listing
            contents = line.split(' ')
            if contents[0] != "dir":
                # file
                file_size = int(contents[0])
                file_name = contents[1]
                current_node.add_child(Node(file_name, file_size))
            else:
                # dir
                dir_name = contents[1]
                current_node.add_child(Node(dir_name))
    return tree

def sum_tree(node, sizes):
    sizes.append( node.get_sum() )
    for child_node in node.children:
        sum_tree(child_node, sizes)

def part1(input_values):
    tree = build_tree( input_values)
    sizes = []
    sum_tree( tree, sizes )
    
    sum = 0
    for size in sizes:
        if size <= 100000:
            sum += size
    
    return sum

def get_input(filename):
    with open(filename, "r") as f:
        return f.read().split("\n")

if __name__ == "__main__":
    input_values = get_input("sample_input.txt")
    part1_result = part1(input_values)
    print(part1_result)