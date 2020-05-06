from os import path
import re
import io
from zipfile import ZipFile

import kaggle_environments.envs.halite.halite as original_halite

version = "0.2"
ignore_action = "INFO"
specification = original_halite.specification.copy()
specification["action"]["additionalProperties"]["enum"].append(ignore_action)
specification["name"] = "halitehack"
specification["version"] = f'halite: {specification["version"]} halitehack: {version}'

def interpreter(state, env):
    for agent in state:
        agent.info = ""
    for agent in state:
        actions = agent.action
        if actions is not None:
            for k,v in list(actions.items()):
                if v == ignore_action:
                    del actions[k]
                    agent.info = k
    return original_halite.interpreter(state, env)

dirpath = path.dirname(__file__)
def html_renderer():
    pattern = re.compile("(.*\.zip)(.+)")
    match = pattern.fullmatch(dirpath)
    # is dirpath a zipfile?
    if match is not None:
        zip_path = match[1]
        inzip_path = path.join(match[2], "halitehack.js")
        with ZipFile(zip_path) as myzip:
            with myzip.open(inzip_path[1:]) as zf:
                f = io.TextIOWrapper(zf)
                return f.read()
    else:
        jspath = path.abspath(path.join(dirpath, "halitehack.js"))
        with open(jspath) as f:
            return f.read()
