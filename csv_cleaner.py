#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 11 05:20:49 2020

@author: Marko
"""
import os
import pandas as pd

os.chdir("/Users/Marko/Thesis_programs/Twitter_geo_data")
filename = "combined_csv.csv"
filename2 = "clean_comb2.csv"

def csv_cleaner(filename,index):
    raw_df = pd.read_csv(filename)
    raw_df.drop_duplicates(subset = index,keep='first',inplace=True)
    return raw_df

#clean_df = csv_cleaner(filename,"id")


#to_drop = ["coordinates","created_at","favorite_count","favorited","geo","lang","place","retweet_count","retweeted","source"]

#for item in to_drop:
    #clean_df.drop(item,axis=1)

#clean_df.to_csv('clean_comb.csv')

raw_df = pd.read_csv(filename2)
clean_dict = {"date":[],"favorites":[],"id":[],"mentions":[],"region":[],"retweets":[],"text":[]}
for index,row in raw_df.iterrows():
    split_str = row["date"].split(" ")
    clean_dict["date"].append(split_str[0])
    clean_dict["favorites"].append(row["favorites"])
    clean_dict["id"].append(row["id"])
    clean_dict["mentions"].append(row["mentions"])
    clean_dict["region"].append(row["region"])
    clean_dict["retweets"].append(row["retweets"])
    clean_dict["text"].append(row["text"])

clean_df = pd.DataFrame.from_dict(clean_dict)
clean_df.to_csv('cleanest_comb.csv')