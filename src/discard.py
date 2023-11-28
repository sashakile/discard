from pathlib import Path
from itertools import islice
from json import load
from pprint import pprint

HOME_PATH = Path("/mnt/c/Users/augus/Downloads/takeout-20230823T012425Z-001/Takeout/Keep/")

def get_annotations(path):
    with open(path) as f:                                
        content = load(f)
        annotations = content.get("annotations",[])
        yield from annotations            


for path in islice(HOME_PATH.glob("*.json"), 100):
    for ann in get_annotations(path):
        pprint(ann)


# discard add url
# discard import file.json
# discard import dir/
# discard init
