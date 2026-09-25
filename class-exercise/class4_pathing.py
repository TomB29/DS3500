import logging
from pathlib import Path
import pandas as pd

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)-8s %(message)s',
    datefmt='%H:%M:%S'
)
logger = logging.getLogger(__name__)

# 1. Creating paths
file_path   = Path('data') / 'sales.csv'
config_path = Path('config') / 'settings.yaml'

# 2. Path properties
print(file_path.name)    # 'sales.csv'
print(file_path.stem)    # 'sales'
print(file_path.suffix)  # '.csv'
print(file_path.parent)  # 'data'

# 3. Checking existence — log the outcome
if not file_path.exists():
    logger.warning(f"File does not exist: {file_path}")
else:
    logger.info(f"File found: {file_path.name}")

# 4. Checking whether a path is specifically a file
if file_path.is_file():
    logger.info(f"{file_path.name} is a file")

df = pd.read_csv("sample.csv")
# TSV
#df = pd.read_csv('data.tsv', sep='\t')
print(df)
df.to_csv("output.csv", index=False)

import json

with open("sample.json", "r") as f:
    data = json.load(f)

print(data["Status"])
print(data["data"])
with open("output.json", "w") as f:
    json.dump(data, f, indent=2)