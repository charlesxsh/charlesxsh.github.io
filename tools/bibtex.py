#!/usr/bin/env python3
from typing import Optional
import bibtexparser
import os
import copy
import json
import argparse
import requests
from pydantic import BaseModel
import logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def resolve_bucket(s:str):
    s = s.lstrip("{ ")
    return s.rstrip(" }")

def bibentry_author_to_uranus_list(authors:str):
    results = []
    for author in authors.split(" and "):
        results.append({
            "name": author
        })
    return results

def get_paper_filepath(e):
    bib_id = e["ID"]
    return f"src/assets/pp/{bib_id}.pdf"

def get_slides_filepath(e):
    bib_id = e["ID"]
    return f"src/assets/pp/{bib_id}-slides.pdf"

def get_slides_url(e):
    bib_id = e["ID"]
    return f"/assets/pp/{bib_id}-slides.pdf"

def get_paper_url(e):
    bib_id = e["ID"]
    return f"/assets/pp/{bib_id}.pdf"

def bib_to_str(e):
    writer = bibtexparser.bwriter.BibTexWriter()
    db = bibtexparser.bibdatabase.BibDatabase()
    copy_e = copy.deepcopy(e)
    copy_e.pop('abstract', None)
    db.entries = [copy_e]
    return writer.write(db)

def bibentry_to_str(e):

    github_star = ""
    if "www-url" in e:
        url = e["www-url"]
        idx = url.find("https://github.com/")
        if idx != -1:
            name = url[len("https://github.com/"):]
            github_star = f"[![GitHub stars](https://img.shields.io/github/stars/{name}.svg?style=social&label=Star&maxAge=2592000)]({url})"



def try_get_bibentry_asset_url(filename:str, bibdb_assets_dir:str, bibdb_assets_url_prefix:str):
    filepath = os.path.join(bibdb_assets_dir, filename)
    if not os.path.exists(filepath):
        logger.info(f"[x] {filepath}")
        return None
    return f"{bibdb_assets_url_prefix}/{filename}"


class UranusPaper(BaseModel):
    name: str
    authors: list
    authorExtra: str = ""
    publicAt: str = ""
    abstract: str = ""
    paperLink: Optional[str] = None
    slideLink: Optional[str] = None
    githubLink: Optional[str] = None
    githubStarsSvgLink: Optional[str] = None
    bibtex: Optional[str] = None
    month: Optional[str] = None
    year: int


def bibentry_to_uranus_dict(bibentry, bibdb_assets_dir, bibdb_assets_url_prefix) -> UranusPaper:
    bibid = bibentry["ID"]
    uranus_paper = UranusPaper(
        name=resolve_bucket(bibentry["title"]),
        authors=bibentry_author_to_uranus_list(bibentry["author"]),
        authorExtra="",
        publicAt=bibentry.get("booktitle", bibentry.get("journal", "")),
        abstract=bibentry.get("abstract", ""),
        paperLink=try_get_bibentry_asset_url(
            f"{bibid}.pdf",
            bibdb_assets_dir,
            bibdb_assets_url_prefix
        ),
        month=bibentry.get("month", ""),
        year=int(bibentry["year"]),
        githubLink=bibentry.get("www-url", None),
        githubStarsSvgLink=None,
        slideLink=try_get_bibentry_asset_url(
            f"{bibid}-slides.pdf",
            bibdb_assets_dir,
            bibdb_assets_url_prefix
        ),
        bibtex=bib_to_str(bibentry)
    )

    if uranus_paper.githubLink:
        idx = uranus_paper.githubLink.find("https://github.com/")
        if idx != -1:
            repo_name = uranus_paper.githubLink[len("https://github.com/"):]
            uranus_paper.githubStarsSvgLink = f"https://img.shields.io/github/stars/{repo_name}.svg?style=social&label=Star&maxAge=2592000"

    return uranus_paper



def get_bibdb_from_file(tex_filepath: str):
    parser = bibtexparser.bparser.BibTexParser(common_strings=True)
    with open(tex_filepath) as f:
        db = bibtexparser.load(f, parser=parser)
    return db

def uranus_dicts_to_json_str(dicts) -> str:
    return json.dumps(dicts, indent=4)

def uranus_dicts_to_ts(dicts) -> str:
    json_str = json.dumps(dicts, indent=4)
    return f"""export default {json_str}"""

def uranus_dicts_to_md(dicts: list[UranusPaper]) -> str:
    md_str = ""
    for d in dicts:
        md_str += f"## {d.name}\n"
        md_str += f"**Authors** {', '.join([a['name'] for a in d.authors])}\n\n"
        md_str += f"**Published at** {d.publicAt}\n\n"
        md_str += f"**Year** {d.year}\n\n"
        if d.githubLink:
            md_str += f"[GitHub]({d.githubLink})\n"
        if d.paperLink:
            md_str += f"[Paper]({d.paperLink})\n"
        if d.slideLink:
            md_str += f"[Slides]({d.slideLink})\n"
        md_str += "\n\n"
    return md_str


def _get_bibdb_from_url(url: str):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    else:
        raise Exception(f"Failed to fetch data from {url}, status code: {response.status_code}")

def _save_bibdb_to_file(bibdb_str: str, filepath: str):
    with open(filepath, "w") as f:
        f.write(bibdb_str)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--bib-file", type=str)
    parser.add_argument("--bib-url", type=str, default="https://scholar.googleusercontent.com/citations?view_op=export_citations&user=2UVeQo4AAAAJ&citsig=AKr7NagAAAAAaBobjUBBkSyj3Wd-_i84xaT6LKE&hl=en")
    parser.add_argument("--out-file", type=str)
    parser.add_argument("--out-format", type=str, choices=["json", "ts", "md"], default="md")
    parser.add_argument("--bib-assets-dir", type=str, help="Dir of extra resources for BibTex like slides, paper, etc.", default=os.path.join("docs", "assets"))
    parser.add_argument("--bib-assets-url-prefix", type=str, help="relative url prefix for the assets dir", default="/assets")


    args = parser.parse_args()
    if args.bib_file is None and args.bib_url is None:
        raise Exception("Please provide either a bib file or a bib url")

    if args.bib_file is not None:
        bibdb_file = args.bib_file
    else:
        os.makedirs(".local", exist_ok=True)
        bibdb_file = ".local/temp.bib"
        bibdb_str = _get_bibdb_from_url(args.bib_url)
        _save_bibdb_to_file(bibdb_str, bibdb_file)

    bibdb_assets_dir = args.bib_assets_dir
    bibdb_assets_url_prefix = args.bib_assets_url_prefix
    out_file = args.out_file
    out_fmt = args.out_format


    bibdb = get_bibdb_from_file(bibdb_file)
    uranus_dicts:list[UranusPaper] = [
        bibentry_to_uranus_dict(
            e,
            bibdb_assets_dir,
            bibdb_assets_url_prefix
        ) for e in bibdb.entries
    ]

    # sort by year desc
    uranus_dicts.sort(key=lambda x: x.year, reverse=True)

    format_handlers = {
        "json": uranus_dicts_to_json_str,
        "ts": uranus_dicts_to_ts,
        "md": uranus_dicts_to_md
    }
    content = format_handlers[out_fmt](uranus_dicts)

    if out_file is not None:
        parent_dir = os.path.dirname(out_file)
        if not os.path.exists(parent_dir):
            os.makedirs(parent_dir)
        with open(out_file, "w") as f:
            f.write(content)
    else:
        print(content)


if __name__ == "__main__":
    main()