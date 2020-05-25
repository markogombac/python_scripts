#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 14:20:07 2020

@author: Marko
"""
#.replace("\n", " ").replace("\r", " ").replace("\r\n", " ")
import GetOldTweets3 as got
import csv
import ast
import time

# Create a file with 'data_' and the current time
filename = 'New_datesV0.1'+'_'+time.strftime('%Y%m%d-%H%M%S')+'.csv'
# Create a new file with that filename
csvFile = open(filename, 'w')
dir1 = "/Users/Marko/Thesis_programs/"
queries = ["COVID19"]
coordinates = file_dict_reader(dir1+"Data_04_12/region_coord3.txt")

csvWriter = csv.writer(csvFile)
csvWriter.writerow(['text',
                'id',
                'date',
                'geo',
                'hashtags',
                'favorites',
                'retweets',
                'mentions',
                'region'])


def scraper(queries,coordinates,date1,date2):
    for hashtag in queries:
       for key in coordinates:
           for value in coordinates[key]:
              coor = ",".join(format(f,'.6f')for f in value[:2])
              radius = str(value[2]) + "km"
              print(coor)
              tweetCriteria = got.manager.TweetCriteria().setQuerySearch(hashtag)\
                                           .setSince(date1)\
                                           .setUntil(date2)\
                                           .setNear(coor)\
                                           .setWithin(radius)\
                                           .setMaxTweets(400)
              #tweepy.Cursor(api.search,q=queries,geocode=coor,since="2020-02-16",tweet_mode = 'extended',count = 5).items()
              container = got.manager.TweetManager.getTweets(tweetCriteria)
              for status in container:
                  print(status.text)
                  insert_status(status,key)

def insert_status(status,region):
    try:
        csvWriter.writerow([status.text,
                            status.id,
                            status.date,
                            status.geo,
                            status.hashtags,
                            status.favorites,
                            status.retweets,
                            status.mentions,
                            region])
    except Exception as e:
        # Print the error
        print(e)
        # and continue
        pass

def file_dict_reader(file_name):
    file = open(file_name,"r")
    contents = file.read()
    dictionary = ast.literal_eval(contents)
    file.close()
    return dictionary


scraper(queries,coordinates,"2020-04-02","2020-05-02")        
