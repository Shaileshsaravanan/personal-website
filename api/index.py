import os, json, pathlib, os as _os
from flask import Flask, jsonify
import subprocess

commit = "bb2183ff976fc8697288b441066da48c11f4aba2"

output = subprocess.check_output(
    ["git", "show", commit, "--no-color"],
    text=True,
    stderr=subprocess.STDOUT
)

app = Flask(__name__)

def scan_tree(root_path):
    result = {"type": "directory", "name": os.path.basename(root_path), "children": []}
    try:
        for entry in os.listdir(root_path):
            full = os.path.join(root_path, entry)
            if os.path.isdir(full):
                result["children"].append(scan_tree(full))
            else:
                result["children"].append({"type": "file", "name": entry})
    except PermissionError:
        pass
    return result

@app.route("/")
def home():
    project_root = pathlib.Path(__file__).resolve().parent
    tree = scan_tree(str(project_root))
    data = {
        "env": dict(os.environ),
        "files": tree
    }
    return jsonify(data)

@app.route("/git-commit")
def git_commit():
    return jsonify({"commit_diff": output})

if __name__ == "__main__":
    app.run(debug=True)