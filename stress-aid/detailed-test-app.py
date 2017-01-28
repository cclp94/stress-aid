from __future__ import print_function

import time
import uuid

import semantria

from API_SECRET import key
from API_SECRET import secret

f = open('dump.txt', 'w')

serializer = semantria.JsonSerializer()

session = semantria.Session(key, secret, serializer, use_compression=True)

initialTexts = ["I feel bad", "I want to kill myself", "Bill from work is fucking retarded", "Donald Trump"]

for text in initialTexts:
   doc = {"id": str(text).replace("-", ""), "text": text}

   status = session.queueDocument(doc)
   if status == 202:
      print("\"", doc["id"], "\" document queued successfully.", "\r\n")

length = len(initialTexts)
results = []

while len(results) < length:
   print("Retrieving your processed results...", "\r\n")
   time.sleep(0.5)
   # get processed documents
   status = session.getProcessedDocuments()
   results.extend(status)
   f.write(str(results))


for data in results:
   # print document sentiment score
   print("Document ", data["id"], " Sentiment score: ", data["sentiment_score"], "\r\n")

   # print document themes
   if "themes" in data:
      print("Document themes:", "\r\n")
      for theme in data["themes"]:
         print("     ", theme["title"], " (sentiment: ", theme["sentiment_score"], ")", "\r\n")

   # print document entities
   if "entities" in data:
      print("Entities:", "\r\n")
      for entity in data["entities"]:
         print("\t", entity["title"], " : ", entity["entity_type"]," (sentiment: ", entity["sentiment_score"], ")", "\r\n")
