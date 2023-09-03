from pathlib import Path
from itertools import islice
from json import load

HOME_PATH = Path("/mnt/c/Users/augus/Downloads/takeout-20230823T012425Z-001/Takeout/Keep/")

for path in islice(HOME_PATH.glob("*.json"), 1):
    with open(path) as f:
        content = load(f)

content

# discard add url
# discard import file.json
# discard import dir/
# discard init
