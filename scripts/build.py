import json
import os
import pathlib
import subprocess

root = pathlib.Path(__file__).resolve().parents[1]

commit = os.environ.get("VERCEL_GIT_COMMIT_SHA")
if not commit:
    commit = subprocess.check_output(
        ["git", "rev-parse", "HEAD"],
        cwd=root
    ).decode().strip()

commit_time = subprocess.check_output(
    ["git", "show", "-s", "--format=%cI", "HEAD"],
    cwd=root
).decode().strip()

data = {
    "commit": commit,
    "commit_time": commit_time,
}

(root / "build_info.json").write_text(
    json.dumps(data),
    encoding="utf-8"
)