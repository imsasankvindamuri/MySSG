from typing import *
from pageparser.preprocessor import *
from pageparser.transliteration import *
from constants.consts import CURRENT_DIRECTORY, HOME_DIRECTORY
import os
import pathlib


def mkpage(filepath: pathlib.Path, outputpath: pathlib.Path, mdata: Dict[str,Any]) -> None:
    print(open(filepath,"r").read())

if __name__ == "__main__":
    pass