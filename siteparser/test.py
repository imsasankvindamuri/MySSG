from pageparser import *
from typing import *
import pathlib
import os
from constants.consts import CURRENT_DIRECTORY, HOME_DIRECTORY, EXPECTED_ENDNODE_CONTENTS

def render_landing():
    """
    Handles pgcontents.md in each folder/directory
    """
    ...

def render_end_node(inputpath: pathlib.Path = CURRENT_DIRECTORY, outputpath: pathlib.Path = HOME_DIRECTORY):
    """
    This will help render an "endnode" --- that is, a directory with no other subdirectories.
    The input directory must satisfy these conditions, otherwise an error is raised:
        - The name of the directory ends with "__page" with double underscores
        - Its contents are only these files below:--
            - A display.md file which has the markdown contents
    """
    #Initial Error Handling
    if not inputpath.is_dir():
        raise Exception(f"{inputpath} must be a directory with a name that ends with '__page'")
    if not inputpath.as_posix().endswith("__page"):
        raise Exception(f"{inputpath} does not end with '__page'")
    if not set(os.listdir(inputpath)) == EXPECTED_ENDNODE_CONTENTS:
        raise Exception(f"{inputpath} has contents {set(os.listdir(inputpath))}. It should only have {EXPECTED_ENDNODE_CONTENTS}")
    
    #Defining some filepaths
    markdown_filepath = inputpath / ("display.md")
    
    pagemaker.mkpage(markdown_filepath, outputpath)

def render_full_directory(inputpath: pathlib.Path = CURRENT_DIRECTORY,endpath: pathlib.Path = HOME_DIRECTORY):
    """
    This takes a folder (assumed to be the working directory) and returns a new folder
    in a specified location (assumed to be home directory) which can be pasted to a
    static site hosting service. It accomplishes this via a recursive BFT (hopefully).
    """
    ...

if __name__ == "__main__":
    render_end_node(pathlib.Path("./RV-1.32.5__page")) #Current Test Case