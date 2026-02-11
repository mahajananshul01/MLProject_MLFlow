import os 
from box.exceptions import BoxValueError
import yaml 
from src.mlProject_MlFlow.utils import logger
import json 
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

@ensure_annotations
def read_yaml(path_to_yaml : Path) -> ConfigBox:
    '''
    read yaml file and returns 
    
    Args: 
        paths_to_yaml(str) : path like input

    Raises:
        valueError if yaml is empty
        e: empty file
    Returns: 
        ConfigBox: Configbox Type
    '''

    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file : {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    

@ensure_annotations
def create_directories(path_to_directories : list , verbose = True):
    '''
    Docstring for create_directories
    Args: 
        path_to_directories(list) : list of path of directories 
        ignore_log(bool, optional) : ignore if multiple directories are to be created 
    '''
    for path in path_to_directories:
        os.makedirs(path , exist_ok=True)
        if verbose:
            logger.info(f'Created directory at {path}')


@ensure_annotations
def save_json(path : Path, data : dict):
    '''
    Docstring for save_json
        Args :
                path(Path) : save to json file 
                data(dict) : data to be saved in json file
    '''
    with open(path, 'w') as f:
        json.dump(data, f, indent= 4)

    logger.info(f"json file saved at {path}")


@ensure_annotations
def load_json(path : Path) -> ConfigBox:
    with open(path) as f:
        content = json.load(f)
    
    logger.info(f'json file successfully loaded from : {path}')
    return ConfigBox(content)

@ensure_annotations
def save_bin(data : Any, path : Path):
    joblib.dump(value=data, filename=Path)
    logger.info(f"Binary file saved at {path}")

@ensure_annotations
def load_bin(path : Path) -> Any:
    data = joblib.load(path)
    logger.info(f"Binary file loaded at {path}")
    return data

@ensure_annotations
def get_size(path : Path) -> str:
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"