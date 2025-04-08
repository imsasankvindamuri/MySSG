from typing import *
from pageparser.preprocessor import preprocessor
from pageparser.transliteration import harvard_kyoto_to_iast, hk_to_iast
from constants.consts import CURRENT_DIRECTORY, HOME_DIRECTORY, CSS_FILE_STR
import os
import pathlib
from markdown import markdown


def mkpage(filepath: pathlib.Path, outputpath: pathlib.Path = HOME_DIRECTORY) -> None:
    
    if not filepath.exists():
        raise Exception(f"Path '{filepath.as_posix()}' does not exist.")
    if not filepath.is_file():
        raise Exception(f"Input file '{filepath.as_posix()}' is not a .md file")
    if not filepath.as_posix().endswith(".md"):
        raise Exception(f"Input '{filepath.as_posix()}' is not a .md file.")
    
    #Get contents and parse them for Harvard-Kyoto section written between the /| delimiters
    contents = preprocessor(filepath.as_posix())

    # Determine target directory and file name
    target_dir = outputpath / filepath.parent.name
    target_html = target_dir / (filepath.stem + ".html")  # 'display.md' → 'display.html'
    target_css = target_dir / pathlib.Path("style.css")

    # Ensure the target directory exists
    os.makedirs(target_dir, exist_ok=True)

    # Write the file
    with open(target_html, "w") as file:
        file.write(f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Draupadeya’s Diatribe Diary</title>
</head>
<link rel="stylesheet" href="style.css">
<body>
  <div class="sitename">
    <h1>Draupadeya’s Diatribe Diary</h1>
  </div>
  <div class="navbar">
    Home / Rigveda / 1.32 / Verse 5
  </div>
  <div class="content">
  {markdown(contents)}
  </div>
</body>
</html>""")
    
    with open(target_css, "w") as file:
        file.write(CSS_FILE_STR)
    


if __name__ == "__main__":
    pass