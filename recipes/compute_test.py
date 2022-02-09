# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
profile_test_prepared_distinct = dataiku.Dataset("profile_test_prepared_distinct")
profile_test_prepared_distinct_df = profile_test_prepared_distinct.get_dataframe()


# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

test_df = profile_test_prepared_distinct_df # For this sample code, simply copy input to output

clwo2=pd.read_csv("/home/sam/dataiku_design/dss_data/jupyter-run/dku-workdirs/TEST/notebook_editor_for_compute_finalcc1adc65/crawl.csv",encoding="utf-8")
# Write recipe outputs
test = dataiku.Dataset("test")
test.write_with_schema(clwo2)
