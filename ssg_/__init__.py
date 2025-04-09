from __future__ import annotations

from pathlib import Path
import argparse
import re
from bs4 import BeautifulSoup
import markdown2
import shutil
import jinja2

Tag = str
Notes = dict[Tag, set[Path]]
CURRENT_DIR = Path(__file__).parent
TEMPLATE_LOADER = jinja2.FileSystemLoader(CURRENT_DIR / "templates")
TEMPLATE = jinja2.Environment(loader=TEMPLATE_LOADER, autoescape=False)

def prepare_output_directory(source: Path, target: Path) -> None:
    target.mkdir(parents=True)
    shutil.copytree(source / "static", target / "static")
    """
    May need to upgrade this... I don't know though.    
    """
    return None

def render_page(template_name: str, path: Path, **kwargs) -> None:
    """
    What the hell is **kwargs?

    Credit to w3schools for this one:
    If you do not know how many keyword arguments that will be passed into your function,
    add two asterisk: ** before the parameter name in the function definition.
    This way the function will receive a dictionary of arguments, and can access the items accordingly.

    Might replace Jinja2 with a personally made framework... wanna contribute something of my own after all.
    I don't care if it would be suicidal. I want to be original. Plus, I'm too lazy to learn a whole new framework right now.
    I might just make a naive function to generate webapages at runtime.
    """
    with path.open("w") as file:
        template = TEMPLATE.get_template(template_name)
        file.write(template.render(**kwargs))
    
    """
    Notes thus far (21:54 into the video)---
    My approach to programming seems to be a bit simplistic. I usually try to build from the ground-up,
    (That is to say, I build individual functionalities before making main() and testing via a temporary test.py)
    but I see that a top-down approach can be quite helpful, even if it feels like shots in the dark for me.
    Maybe I need to understand how to see the bigger picture--- at the moment, I code small details and build up
    from there. I should try this top-down approach more.
    """
    
    return None

def render_static_pages(source: Path, target: Path) -> None:
    render_page("index.html", target / "index.html")
    return None

def render_content(notes: Notes, target: Path) -> None:
    return None

def render_sitemap(notes: Notes, target: Path) -> None:
    ...

def text_as_html(path: Path) -> str:
    text = path.read_text()
    """
    Tutorial did more stuff inside markdown2.markdown that I couldn't be bothered with... I skipped it.
    I need to change this too: Need a way to render IAST (Since I plan to write commentaries on Sanskrit work often)
    """
    return markdown2.markdown(
        text.strip()
    )

def find_tags(path: Path) -> set[str]:
    tag_re = re.compile(r"(?:[^\\])(#[a-zA-Z0-9/-]+)")
    
    """
    Oh God... What the fuck? I'm never going 10 feet near regexes ever again.
    Once I remake this thing for my tastes, this will be the first to get edited.
    I don't even care if it becomes inefficient.
    """

    html = text_as_html(path)
    soup = BeautifulSoup(html,"html5lib")
    for quote in soup.find_all("blockquote"):
        quote.decompose()
    for code in soup.find_all("code"):
        code.decompose()
    return set(tag_re.findall(path.read_text()))

def symlink_latest_output(path: Path) -> None:
        ...

def get_cli_args() -> tuple[Path, Path]:
    parser = argparse.ArgumentParser(prog="ssg_")   #IN_TUTORIAL: "ssg"
    parser.add_argument("-s", help="where to find source notes", type=Path)
    parser.add_argument("-t",help="where to generate deployable site", type=Path)

    args = parser.parse_args()
    if args.s is None or args.t is None:
        parser.error("Provide both -s and -t")
    return args.s, args.t

def get_public_notes(path: Path) -> Notes:
    result: Notes = {}

    for dir in sorted(list(path.glob("*__page"))):  #IN_TUTORIAL: *.textbundle
        text = path / "text.md"
        tags = find_tags(text)
        if '#Public' not in tags:
            """
            Tags will be at the end of a document and will be like this:
            #Public #Poetry #Commentary
            """
            continue
        for tag in tags:
            result.setdefault(tag, set()).add(text)
            """
            The setdefault() method returns the value of the item with the specified key.
            If the key does not exist: insert the key with the specified value (set() in our case).
            """
        
    return result

def main() -> None:

    source_dir, target_dir = get_cli_args()
    notes = get_public_notes(source_dir)

    prepare_output_directory(source_dir, target_dir)
    render_static_pages(source_dir, target_dir)
    render_content(notes, target_dir)
    render_sitemap(notes, target_dir)
    symlink_latest_output(target_dir)