#!/usr/bin/env python3
"""
generate_versions.py
Generate JSON file with gallery versions based on Git tags of submodules.
"""
import subprocess
from pathlib import Path

from common import GALLERIES

def get_git_tags_with_dates(repo_path):
    """Return a list of (tag, date) tuples sorted by creation date descending."""
    try:
        output = subprocess.check_output(
            ["git", "-C", str(repo_path), "tag", "--sort=-creatordate",
             "--format=%(refname:short)|%(creatordate:short)"],
            text=True
        ).splitlines()
        tags = []
        for line in output:
            if "|" in line:
                tag, date = line.split("|", 1)
                tags.append({"tag": tag.strip(), "date": date.strip()})
        return tags
    except Exception:
        return []

def get_versions():
    """Return a dict with latest version, all tags with dates, and zip URLs."""
    gallery_versions = {}
    for name in GALLERIES:
        path = Path(f"../docs/SWOT-{name}")
        tags = get_git_tags_with_dates(path)
        latest = tags[0] if tags else {"tag": "dev", "date": ""}
        zip_base = f"https://github.com/SWOT-community/SWOT-{name}/archive/refs/tags"
        gallery_versions[name] = {
            "latest": latest["tag"],
            "latest_date": latest["date"],
            "tags": tags[1:],
            "zip_base": zip_base,
        }
    print(gallery_versions)
    return gallery_versions

def get_myst_substitutions():
    """Return a dict of MyST substitutions for all galleries."""
    substitutions = {}
    for name, v in get_versions().items():
        key = name.replace("-", "_").lower()

        substitutions[f"{key}_latest_badge"] = (
            f"{{bdg-primary}}`{v['latest']}` {{bdg-secondary}}`{v['latest_date']}`"
        )

        lines = [
            f"- {{bdg-primary}}`{v['latest']}` _{v['latest_date']}_ — "
            f"[Download ZIP]({v['zip_base']}/{v['latest']}.zip) ⬅ **latest**"
        ]
        for t in v["tags"]:
            lines.append(
                f"- {{bdg-secondary}}`{t['tag']}` _{t['date']}_ — "
                f"[Download ZIP]({v['zip_base']}/{t['tag']}.zip)"
            )
        substitutions[f"{key}_downloads"] = "\n".join(lines)
        substitutions[f"{key}_latest"] = v["latest"]

    return substitutions

if __name__ == "__main__":
    print(get_myst_substitutions())