from pathlib import Path

class Tree(object):
    "Generic tree node"
    def __init__(self, name="/", children=None):
        self.name = name
        self.children = []
        if children is not None:
            for child in children:
                self.add_child(child)

    def __repr__(self) -> str:
        return self.name

    def add_child(self, node):
        assert isinstance(node, Tree)
        self.children.append(node)

def parse_command(line):
    cmd_segments = line[2:].split(' ')
    cmd = cmd_segments[0]
    arg = ""
    if len(cmd_segments) == 2:
        arg = cmd_segments[1]
    return (cmd, arg)

def build_tree(input_values):
    tree = Tree()
    current_path = ""
    for line in input_values:
        if line[0] == '$':
            # command
            cmd = parse_command(line)
            process = cmd[0]
            cmd_arg = cmd[1]
            if process == "cd":
                if cmd_arg == "..":
                    # move to parent
                    print("")
                else:

                    current_path += cmd[1]
                    if current_path != "/":
                        current_path += "/"
        else:
            # dir listing
            contents = line.split(' ')
            if contents[0] != "dir":
                # file
                file_size = int(contents[0])
                file_name = contents[1]
                file_path = "{}{}".format(current_path, file_name)

def part1(input_values):
    tree = build_tree(input_values)
    return 0

def get_input(filename):
    with open(filename, "r") as f:
        return f.read().split("\n")

if __name__ == "__main__":
    input_values = get_input("sample_input.txt")
    part1_result = part1(input_values)