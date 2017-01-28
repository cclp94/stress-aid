from __future__ import print_function

import time
import uuid

import semantria

from API_SECRET import key
from API_SECRET import secret

def analyse(txtInput):
    serializer = semantria.JsonSerializer()
    session = semantria.Session(key, secret, serializer, use_compression=True)
    doc = {"id": str(txtInput).replace("-", ""), "text": txtInput}
    status = session.queueDocument(doc)
    if status == 202:
        print("\"", doc["id"], "\" document queued successfully.", "\r\n")
   
    results = []

    while len(results) != 1:
        print("Retrieving your processed results...", "\r\n")
        time.sleep(0.1)
        # get processed documents
        status = session.getProcessedDocuments()
        results.extend(status)
    for data in results:
        response = {'score':data["sentiment_score"], 'sentiment':str(data["sentiment_polarity"])}
    return response

    # for data in results:
    #     # print document sentiment score
    #     print("Document ", data["id"], " Sentiment score: ", data["sentiment_score"], "\r\n")

    #     # print document themes
    #     if "themes" in data:
    #         print("Document themes:", "\r\n")
    #         for theme in data["themes"]:
    #             print("     ", theme["title"], " (sentiment: ", theme["sentiment_score"], ")", "\r\n")

    #     # print document entities
    #     if "entities" in data:
    #         print("Entities:", "\r\n")
    #         for entity in data["entities"]:
    #             print("\t", entity["title"], " : ", entity["entity_type"]," (sentiment: ", entity["sentiment_score"], ")", "\r\n")

    # return str(results)
#####################################################################################

print (str(analyse("I am sad")))