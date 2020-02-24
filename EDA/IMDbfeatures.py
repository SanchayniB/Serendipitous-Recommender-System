
# Importing data and filtering it

import pandas as pd
import numpy as np

import json,csv
import sys

from Filtering import train_filtering 

# To run: python python IMDbfeatures.py config.json in the terminal
# Make sure you do necessary edits to the config file before running it

def main(config_arg):
    config = config_arg + ".json"
    config = json.loads(open(config_arg).read())
    train_loc = config['loc'] + '//training.csv'
    
    train_subset = train_filtering(train_loc, [2017])
    print(train_subset.head())
    
    train_subset_path = config['intermediate_loc'] + '//train_subset.csv'
    train_subset.to_csv(train_subset_path)

   


if __name__ == "__main__":
    main(sys.argv[1])

# Building a function to extract imbd features

