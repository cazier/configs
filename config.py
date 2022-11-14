import json
import pathlib
import sys

import yaml

# Directly giving variable values
bind = "0.0.0.0"
port = 9000


# Getting a variable value out of a yaml file
if (path := pathlib.Path("config.yaml")).exists():
    _yaml = yaml.safe_load(path.read_text(encoding="utf-8"))
else:
    _yaml = {}

user = _yaml.get("name", "Bob")
greeting = _yaml.get("greeting", "Hello")

# Getting a variable value out of a json file
if (path := pathlib.Path("config.json")).exists():
    _json = json.loads(path.read_text(encoding="utf-8"))
else:
    _json = {}

kind = _json.get("kind", "setting")
source = _json.get("source", "an omniscient being")

# Getting a variable value from the command line arguments
debug = False
if len(sys.argv) > 1:
    # This is a terrible approach since it assumes the first argument is only ever debug... But it
    # gets the point across.
    debug = sys.argv[1].lower() == "debug"
