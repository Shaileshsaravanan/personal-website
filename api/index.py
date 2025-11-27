import json
import pathlib
from flask import Flask, jsonify, render_template

app = Flask(__name__)

_build_info_path = pathlib.Path(__file__).with_name("build_info.json")
if _build_info_path.exists():
    _build_info = json.loads(_build_info_path.read_text(encoding="utf-8"))
else:
    _build_info = {"commit": None, "commit_time": None}


@app.route("/")
def build_info_json():
    return jsonify(_build_info)


@app.route("/")
def index():
    return render_template("index.html", build_info=_build_info)

if __name__ == '__main__':
    app.run(debug=True)