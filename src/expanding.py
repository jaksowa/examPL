import stem_volume
from stem_volume import *
import pandas as pd
import numpy as np
input_df = pd.read_csv('../data/trees_sampled.csv')
from mapping import species_mapping
metadata = pd.read_csv(../data/form_metadata.csv',sep= ';')