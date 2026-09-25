import json
import logging
from pathlib import Path
import sys

import pandas as pd
import yaml
import os
from dotenv import load_dotenv

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)-8s %(message)s",
    datefmt="%H:%M:%S"
)
logger = logging.getLogger(__name__)


def inspect_csv(filepath: any) -> any:
    """Read a CSV file and display basic information."""
    #TO DO
    # 1. Read the file using pd.read_csv().
    data = pd.read_csv(filepath)
    # 2. Log the filepath at INFO.
    logger.info("File validated @ %s", {filepath.name})
    # 3. Print the first three rows (e.g. DataFrame.head(3))
    print(data.head(3))



def inspect_json(filepath):
    """Read a JSON file and display basic information."""
    # TO DO:
    # 1. Open the file and read it using json.load().
    with open(filepath, "r") as file:
        data = json.load(file)
    logger.info("Filepath at %s", filepath.name)
    # 2. Log the filepath at INFO.
    # 3. Print the contents.
    print(data)


def inspect_yaml(filepath):
    """Read a YAML file and display basic information."""
    # TO DO:
    # 1. Open the file and read it using yaml.safe_load().
    # 2. Log the filepath at INFO.
    # 3. Print the contents.
    with open(filepath, "r") as f:
        config = yaml.safe_load(f)
    logger.info("Filepath located @ %s", filepath.name)
    print (config["cleaning"]["missing"])
    print(config["processing"]["batch_size"])


def inspect_env():
    """Read a .env file and display basic information."""
    load_dotenv()

    keys = [
        key for key in ["USERNAME", "PASSWORD"]
        if os.getenv(key) is not None
    ]
    logger.info("Inspecting ENV")
    print(keys)
    # TODO:
    # 1. Log at INFO that .env was loaded.
    # 2. Print keys.
    # Do not print passwords, API keys, or other secret values.


def main():
    # TODo
    # 1. Create a Path object for the data directory.
    # 2. Use the / operator to build the CSV, JSON, and YAML paths.
    # 3. Call each inspection function using the matching path.
    # 4. Call inspect_env() without an argument.
    data_dir = Path("data")
    filepath_csv = data_dir / "sample.csv"
    filepath_json = data_dir / "sample.json"
    filepath_yaml = data_dir / "sample.yaml"

    inspect_csv(filepath_csv)
    inspect_json(filepath_json)
    inspect_yaml(filepath_yaml)
    inspect_env()
    print(filepath_csv)
    print(filepath_csv.name)
if __name__ == "__main__":
    main()