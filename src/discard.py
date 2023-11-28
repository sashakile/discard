from pathlib import Path
from itertools import islice
from json import load
from pprint import pprint

HOME_PATH = Path(
    "/mnt/c/Users/augus/Downloads/takeout-20230823T012425Z-001/Takeout/Keep/")


def get_content(path):
    with open(path) as f:
        content = load(f)
        return content

def get_annotations(content):
    annotations = content.get("annotations", [])
    yield from annotations


for path in islice(HOME_PATH.glob("*.json"), 100):
    for ann in get_annotations(get_content(path)):
        pprint(ann)


# discard add url
# discard import file.json
# discard import dir/
# discard init
