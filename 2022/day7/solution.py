from pathlib import Path

class File(object):
    "Represents a file"
    def __init__(self, name, size):
        self.name = name
        self.size = size

class Folder(object):
    "Represents a folder"
    def __init__(self, name = "/", subfolders = None):
        self.parent = None
        self.name = name
        self.subfolders = []
        self.files = []

        if subfolders is not None:
            [self.AddSubFolder(subfolder) for subfolder in subfolders]

    def __repr__(self) -> str:
        return self.name

    def AddFile(self, file):
        self.files.append(file)

    def GetSubFolders(self):
        return self.subfolders

    def AddSubFolder(self, node):
        assert isinstance(node, Folder)
        # set parent to this instance for new node
        node.parent = self
        self.subfolders.append(node)

    def FindFolder(self, name):
        for node in self.subfolders:
            if node.name == name:
                return node
        return None

    def GetSize(self):
        temp_sum = sum([file.size for file in self.files])
        for child_node in self.subfolders:
            temp_sum += child_node.GetSize()
        return temp_sum

def parse_command(line):
    cmd_segments = line[2:].split(' ')
    cmd = cmd_segments[0]
    arg = ""
    if len(cmd_segments) == 2:
        arg = cmd_segments[1]
    return (cmd, arg)

def build_tree(input_values):
    tree = Folder("/")
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
                        current_node = current_node.FindFolder(dir_name)
        else:
            # dir listing
            contents = line.split(' ')
            if contents[0] != "dir":
                # file
                file_size = int(contents[0])
                file_name = contents[1]
                current_node.AddFile(File(file_name, file_size))
            else:
                # dir
                dir_name = contents[1]
                current_node.AddSubFolder(Folder(dir_name))
    return tree

def sum_tree(folder, sizes):
    sizes.append( folder.GetSize() )
    [sum_tree(sub_folder, sizes) for sub_folder in folder.GetSubFolders()]

def part1(tree):
    sizes = []
    sum_tree( tree, sizes )
    
    return sum([size for size in sizes if size <= 100000])

def part2(tree):
    sizes = []
    sum_tree( tree, sizes )
    total_disk_space = 70000000
    required = 30000000
    sorted_sizes = sorted(sizes)
    used_space = sorted_sizes[-1]
    unused_space = total_disk_space - used_space
    missing_space = required - unused_space
    
    return [size for size in sorted_sizes if size > missing_space][0]

def get_input(filename):
    with open(filename, "r") as f:
        return f.read().split("\n")

if __name__ == "__main__":
    input_values = get_input("input.txt")
    tree = build_tree( input_values )
    
    part1_result = part1(tree)
    part1_expected = 1423358
    #part1_expected = 95437
    assert part1_expected == part1_expected

    part2_result = part2(tree)
    part2_expected = 545729
    #part2_expected = 24933642
    assert part2_result == part2_expected