from itertools import islice
from youtube_comment_downloader import *
downloader = YoutubeCommentDownloader()
print("Fetching youtube comments")

comments = downloader.get_comments_from_url('https://www.youtube.com/watch?v=zwR6M5zpnWs', sort_by=SORT_BY_POPULAR) #119 comments
# comments = downloader.get_comments_from_url('https://www.youtube.com/watch?v=MZ8giCWDcyE', sort_by=SORT_BY_POPULAR) # mkbhd 5000 comments
print("Fetched youtube comments")

from textblob import TextBlob

import json

json_arr = []

print("Analysizing youtube comments")

for comment in comments:
        testimonial = TextBlob(comment['text'])
        if(testimonial.sentiment.polarity>0.0):
            senti = 'positive'
        elif(testimonial.sentiment.polarity<0.0):
            senti = 'negative'
        else :
            senti = 'neutral'
        json_arr.append( {"text": comment['text'], "polarity" : testimonial.sentiment.polarity, "sentiment": senti})
print("Analysed youtube comments")
print("Creating output file")

json_object = json.dumps(json_arr, indent=4)
print("Created output file")

with open("output.json", "w") as outfile:
    outfile.write(json_object)

# import csv

# with open('output.csv', 'w', newline='', encoding='utf-8') as file:
#     writer = csv.writer(file)
    
#     writer.writerow(["Text", "Polarity", "Sentiment"])

#     for comment in comments:
#         testimonial = TextBlob(comment['text'])
#         if(testimonial.sentiment.polarity>0.0):
#             senti = 1
#         else :
#             senti = 0
#         print(testimonial.sentiment.polarity)
#         print(senti)
#         writer.writerow([comment['text'], testimonial.sentiment.polarity, senti])
    


