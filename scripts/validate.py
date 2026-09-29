#!/usr/bin/env python3
"""Validate the portable plugin package without external dependencies."""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
SKILL = ROOT / "skills" / "humanizer" / "SKILL.md"


def load_json(path: Path) -> dict:
    with path.open(encoding="utf-8") as file:
        return json.load(file)


def main() -> None:
    required = [
        ROOT / "plugin.json",
        ROOT / ".codex-plugin" / "plugin.json",
        ROOT / ".claude-plugin" / "plugin.json",
        ROOT / ".claude-plugin" / "marketplace.json",
        SKILL,
        ROOT / "skills" / "humanizer" / "references" / "writing-patterns.md",
        ROOT / "skills" / "humanizer" / "references" / "indian-english.md",
    ]
    missing = [str(path.relative_to(ROOT)) for path in required if not path.is_file()]
    assert not missing, f"Missing required files: {missing}"

    manifests = [load_json(path) for path in required[:4]]
    versions = {manifest.get("version") for manifest in manifests[:3]}
    assert versions == {"1.0.0"}, f"Manifest versions do not match: {versions}"
    assert all(manifest.get("name") == "sunnyjoshi-skills" for manifest in manifests[:3])

    text = SKILL.read_text(encoding="utf-8")
    assert re.match(r"\A---\nname: humanizer\n", text)
    assert "Return only the finished rewrite" in text

    editable_docs = [SKILL, *required[5:]]
    offenders = [
        str(path.relative_to(ROOT))
        for path in editable_docs
        if "\u2014" in path.read_text(encoding="utf-8")
    ]
    assert not offenders, f"Em dash found in skill content: {offenders}"

    print("sunnyjoshi-skills v1.0.0 is valid")


if __name__ == "__main__":
    main()
