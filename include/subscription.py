################################## 2222222222222222222 #####################################
#!/usr/bin/python3

import os
import json
import logging
import requests

logger = logging.Logger('catch_all')

def query_az(query):
    json_cis=os.popen(query).read()
    return json.loads(json_cis)

def sub():
    print("Processing Checking subscription...")
    subid=[]
    cloudname=[]
    subname=[]
    try:
        querysub='az account list --query [*].[id,cloudName,name]'
        json_cis=query_az(querysub)
        #with open('subtest.txt') as f:
        #    json_cis = json.load(f)
        #iteration through Storage Account
        for i in range(len(json_cis)):
            subid.append(json_cis[i][0])
            cloudname.append(json_cis[i][1])
            subname.append(json_cis[i][2])
        return [subid,cloudname,subname]
    except Exception as e:
        logger.error('Failing ' + str(e))
        return ["No Id","No CloudName","No Name"]