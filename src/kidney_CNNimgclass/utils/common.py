from kidney_CNNimgclass import logger
import os
from box.exceptions import BoxValueError
import yaml
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64

@ensure_annotations
def read_yaml(path_to_yamls : Path) -> ConfigBox:
    """ read yaml file and returns content as ConfigBox type data type
    i.e with json like dot notation capability

    Args:
    path_to_yaml (str): path like input

    Raises:
    ValueError: if yaml file is empty
    e: empty file

    returns: configBox
    
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content= yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully.")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e

@ensure_annotations
def create_directories(paths_to_directories: List , verbose=True):
    """Create directories from paths list 
    Args: 
        path_to_directories: paths list
        creation_log: bool , ignore when multiple folders to be created, defaults to false
    """

    for path in paths_to_directories:
        os.makedirs(path, exists_ok=True)
        if verbose:
            logger.info(f"Folder created at: {path}")
        
@ensure_annotations
def save_json(path : Path , data: dict):
    """
    save json data
    Args:
        path (Path): path to destination
        data (dict): data dict to be saved
    """
    with open(path, "w") as f:
        json.dump(data,f,indent=4)

    logger.info(f"JSON file saved at path: {path}")

@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """
    Load json from path
    Args:
        path (Path) : to be loaded from

    Return:
        ConfigBox: data as class attributes (same as dot notation in JS) instead of dict
    """

    with open(path) as f:
        content = json.load(f)
    
    logger.info(f"JSON file loaded from path: {path}")
    return ConfigBox(content)

@ensure_annotations
def save_binary(data: Any, path: Path):
    """save binary file

    Args:
        data (Any): data to be saved as binary
        path (Path): path to binary file
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"binary file saved at: {path}")


@ensure_annotations
def load_binary(path: Path) -> Any:
    """load binary data

    Args:
        path (Path): path to binary file

    Returns:
        Any: object stored in the file
    """
    data = joblib.load(path)
    logger.info(f"binary file loaded from: {path}")
    return data

@ensure_annotations
def get_size(path: Path) -> str:
    """get size in KB

    Args:
        path (Path): path of the file

    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"


def decodeImage(imgstring, fileName):
    imgdata = base64.b64decode(imgstring)
    with open(fileName, 'wb') as f:
        f.write(imgdata)
        f.close()


def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read())
