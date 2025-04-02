from typing import *
import pathlib
import os

CURRENT_DIRECTORY = os.path.relpath(pathlib.Path.cwd(),pathlib.Path.cwd().parent)
HOME_DIRECTORY = pathlib.Path.home()

def render_landing():
    """
    Handles pgcontents.md in each folder/directory
    """
    ...

def render_end_node():
    """
    This will help render an "endnode" --- that is, a directory with no other subdirectories
    The input directory is assumed to have a pgcontents.md, and can optionally have other .md files,
    in which case those other .md files will be accessible from the converted version of
    pgcontents.md.
    """
    ...

def render_full_directory(inputpath: pathlib.Path = CURRENT_DIRECTORY,endpath: pathlib.Path = HOME_DIRECTORY):
    """
    This takes a folder (assumed to be the working directory) and returns a new folder
    in a specified location (assumed to be home directory) which can be pasted to a
    static site hosting service. Same input conditions as render_end_node(), except this supports
    subdirectories as well. It accomplishes this via a recursive DFS (hopefully).

    Here's the potential logic flow~~~
        
        if dir.hasNoSubDirs:
            render_end_node()
        else:
            render_landing()  # Handles pgcontents.md
            for i in dir.subDirs:
                render_full_directory()

    """
    ...