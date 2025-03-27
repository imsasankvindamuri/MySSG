from typing import *
import os

NodeInfoType = Dict[str, List[str]] #Stores all the info on node; its children and its metadata
TreeType = Dict[str, NodeInfoType] #Maps each nodepath to a corresponding NodeInfoType

class Tree():
    def __init__(self, path: str) -> None:
        if not os.path.exists(path):
            raise FileNotFoundError("The given path does not exist...")
        if not os.path.isdir(path):
            raise NotADirectoryError(f"The given path '{path}' is a file, not a directory.")

        self.struct: TreeType = {}
        self.path: str = path
        self._build_tree()


    def _build_tree(self) -> None:

        for nodepath, children_nodes, file_content in os.walk(self.path):
            self.struct[nodepath] = {
                "child_nodes" : [ os.path.join(nodepath, child_name) for child_name in children_nodes],
                "content" : [os.path.join(nodepath, files) for files in file_content]
            }


if __name__ == "__main__":
    #IGNORE: This is purely testing and will be replaced with 'pass' once my program pasess my unit tests.
    tree = Tree("../transl")
    print(tree.path)
    print(tree.struct)