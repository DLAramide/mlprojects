import os
import sys 

import pandas as pd
import numpy as np
import pickle

from src.exception import CustomException

def save_object(file_path, obj):
    try:
        with open(file_path, 'wb') as f:
            pickle.dump(obj, f)
    except Exception as e:
        raise CustomException(e,sys)