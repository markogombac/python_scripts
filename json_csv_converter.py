import pandas as pd
import json


#File directory here 
file = "/Users/Marko/Thesis_programs/Data_04_12/covid-19-mobility-tracker-master/output/IT/mobility.json"

#Load the json file in as a dictionary
with open(file) as f:
    d = json.load(f)

#Convert the dictionary into a datafram
df = pd.DataFrame.from_dict(d)
print(df)
#Convert dataframe to csv - put the desired file name in parenthesis 
df.to_csv("/Users/Marko/Thesis_programs/Data_04_12/test/Italy_mobility_report_test.csv")

