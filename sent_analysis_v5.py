#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  4 15:52:03 2020
@author: Marko
"""
#sentiment analysis

import pandas as pd
import os 
import requests
import glob

os.chdir("/Users/Marko/Thesis_programs/Sent_test2/")
extension = 'csv'
all_filenames1 = [i for i in glob.glob('*.{}'.format(extension))]
#all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
print(len(all_filenames1))
#df_count = pd.read_csv("/Users/Marko/Thesis_programs/Sent_test/final_files/clean_new3.csv")
sentiment_score1 = {"index":[],"sent":[],"code":[]}
text_analytics_subscription_key = "1ced9ff890c945d7be8c4a961d7bcd32" 
text_analytics_endpoint = "https://firstsent.cognitiveservices.azure.com/"
meta_source1 = pd.read_csv("/Users/Marko/Thesis_programs/Sentiment_analysis/final_files2/new_clean4.csv")
def create_entry(tweet_text, ID):
    doc_entry = {"language": "it", "id": ID, "text": tweet_text}
    return(doc_entry)
counter = 0
for file in all_filenames1:
    counter += 1 
    print(counter)
    #print(file)
    source_df = pd.read_csv(file)
    data = {"documents": []}
    for index,row in source_df.iterrows():
        data["documents"].append(create_entry(row["text"], row["index"]))
        #print(type(row["id"]))
    
    headers = {
        # Request headers
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': text_analytics_subscription_key,
    }
    
    params = {'showStats': True}
    analyze_url = text_analytics_endpoint + "text/analytics/v3.0-preview/sentiment"
    response = requests.post(analyze_url, headers=headers, params=params, json=data)
    #response.raise_for_status()
    
    analysis = response.json()
    #print(analysis)
    sentiment = {doc['id'] : doc['documentScores'] for doc in analysis['documents']}
    #print(sentiment)
    id_list1 = []
    
    #list(mydict.values()).index(16)]
    
    #change it into a dictionary of ID's and categorical score
    #positive = 2, neutral =1, negative =0
    id_list=[]
    
    for f in sentiment.keys():
        id_list.append(f)
    

    for ids in id_list:       
        if sentiment[ids]['positive'] > sentiment[ids]['neutral'] and sentiment[ids]['positive'] > sentiment[ids]['negative']:
            sentiment_score1["index"].append(ids)
            sentiment_score1["sent"].append("positive") 
            sentiment_score1["code"].append(2)
        elif sentiment[ids]['neutral'] > sentiment[ids]['positive'] and sentiment[ids]['neutral'] > sentiment[ids]['negative']:
            sentiment_score1["index"].append(ids)
            sentiment_score1["sent"].append("neutral") 
            sentiment_score1["code"].append(1)
        else: 
            sentiment_score1["index"].append(ids)
            sentiment_score1["sent"].append("negative") 
            sentiment_score1["code"].append(0)
        
        
os.chdir("/Users/Marko/Thesis_programs/Sentiment_analysis/final_files2/")
#df_sentiment = pd.DataFrame.from_dict(sentiment_score)
print(sentiment_score1["index"][0])
print(sentiment)
df_sentiment1 = pd.DataFrame.from_dict(sentiment_score1)
df_sentiment1.to_csv("sent_data.csv") 
df_sentiment1["index"] = df_sentiment1["index"].astype(int)
df_merge1 = meta_source1.merge(df_sentiment1,left_on = "index", right_on = "index")
print(df_merge1.shape)
df_merge1.to_csv("merged_sent.csv")
