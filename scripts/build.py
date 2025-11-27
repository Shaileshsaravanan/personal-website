import json
import os
import pathlib

root = pathlib.Path(__file__).resolve().parents[1]

env_data = {k: v for k, v in os.environ.items()}

paths = {
    "root": str(root),
    "script": str(pathlib.Path(__file__).resolve()),
    "script_dir": str(pathlib.Path(__file__).resolve().parent),
    "cwd": str(pathlib.Path.cwd()),
}

all_dirs = {}
for base in [root]:
    for p in base.rglob("*"):
        if p.is_dir():
            all_dirs[str(p)] = True

data = {
    "env": env_data,
    "paths": paths,
    "directories": all_dirs,
}

(root / "build_info.json").write_text(
    json.dumps(data, indent=2),
    encoding="utf-8"
)