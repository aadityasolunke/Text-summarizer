import os 
from box.exceptions import BoxValueError
import yaml
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path 
from typing import Any
# src/text_summarizer/utils/common.py

from text_summarizer.logging import logger




@ensure_annotations
def read_yaml(path_to_yaml:Path) -> ConfigBox:
    """read yaml file and returns
    
    Args:
    path_to_yaml (str): path like  input 

    Raises:
    ValueError: if yaml is empty 
    e:empty file 

    Returns:
    ConfigBox:ConfigBox TypeError
    """
    try:
        with open (path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e :
        raise e

@ensure_annotations
def create_directories(path_to_directories:list, verbose=True):
    """create directories if not exist
    Args:
    path_to_directories (list): list of directories
    ignore_log (bool,optional): ingore if multiple dirs is to be created. Defaults to False."""

    for path in path_to_directories:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info(f"creating directory at: {path}")

@ensure_annotations
def get_size(path:Path) -> str:
    """get size in KB
    Args :
         path (Path): path to file
    Returns:
         str:size in KB
         """
    
    size_in_KB = round(os.path.getsize(path)/1024)
    return f"{size_in_KB} KB"