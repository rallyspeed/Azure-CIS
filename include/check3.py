################################## 2222222222222222222 #####################################
#!/usr/bin/python3

import os
import json
import logging
import datetime
import sys

logger = logging.Logger('catch_all')

def query_az(query):
    json_cis=os.popen(query).read()
    return json.loads(json_cis)

def check31():
    print("Processing 31...")
    st31=""
    passvalue31 = 0
    totalvalue31 = 0
    passed31='<font color="red">Failed </font>('
    try:
        query31='az storage account list --query [*].[name,enableHttpsTrafficOnly]'
        json_cis=query_az(query31)
     #iteration through Storage Account
        for i in range(len(json_cis)):
            st31=st31+('Storage Account: <b>%s</b> status: <font color="blue"><b>%s</b></font><br>\n' % (json_cis[i][0],json_cis[i][1]))
            #st32=st32+('Storage Account: <b>%s</b> status: <font color="blue"><b>%s</b></font><br>\n' % (json_cis[i][0],json_cis[i][2]))
            if (json_cis[i][1] is True):
                passvalue31=passvalue31+1
                passed31='<font color="red">Passed </font>('
            else:
                passed31='<font color="red">Failed </font>('  
            totalvalue31 = totalvalue31+1
        score31=[st31,passvalue31,totalvalue31,passed31]
        return score31
    except Exception as e:
        logger.error('Failed to Query Storage Accounts' + str(e))
        return ["Failed to Query Storage Accounts "]
		
def check32():
    print("Processing 32...")
    st32=""
    passvalue32 = 0
    totalvalue32 = 0
    score32=""
    passed32='<font color="red">Failed </font>('
    try:
        query32='az storage account list --query [*].[name,encryption.services.blob.enabled]'
        json_cis=query_az(query32)
        #iteration through Storage Account
        for i in range(len(json_cis)):
            st32=st32+('Storage Account: <b>%s</b> status: <font color="blue"><b>%s</b></font><br>\n' % (json_cis[i][0],json_cis[i][1]))
            if (json_cis[i][1] is True):
                passvalue32=passvalue32+1
                passed32='<font color="green">Passed </font>('
            else:
                passed32='<font color="red">Failed </font>('  
            totalvalue32 = totalvalue32+1
        score32=[st32,passvalue32,totalvalue32,passed32]
        return score32
    except Exception as e:
        logger.error('Failed to Query Storage Accounts' + str(e))
        return ["Failed to Query Storage Accounts "]
		
def check33():
    print("Processing 33...")
    st33=""
    st331=""
    passvalue33 = 0
    totalvalue33 = 0
    score33=""
    passed33='<font color="green">Passed </font>('
    #query for the past 90 days. calculating today minus 90 days
    format = "%Y-%m-%dT%H:%M:%SZ"
    today = datetime.datetime.utcnow()
    pastdays = datetime.timedelta(days=90)
    todayminus90 = today - pastdays
    todayminus90 = todayminus90.strftime(format)
    try:
        query33='az storage account list --query [*].[resourceGroup,name]'
        json_cis=query_az(query33)
        #iteration through storage account Resource Group
        for i in range(len(json_cis)):
            RG = json_cis[i][0]
            StorageName = json_cis[i][1]
            found=0
            notfound=0
            try:
                query331='az monitor activity-log list --resource-group %s --start-time %s --query [*].[authorization.action,resourceId]' % (RG,todayminus90)
                json_cis2=query_az(query331)
                #iteration through event logs
                for j in range(len(json_cis2)):
                    if ("Microsoft.Storage/storageAccounts/regenerateKey/action" in json_cis2[j][0]):
                        st331=('key regenerartion found for storage <b>%s</b> in resource group <b>%s</b><br>\n' % (StorageName,RG))
                        found=1
                        passvalue33=passvalue33+1
                        passed33='<font color="green">Passed </font>('
                    else:
                        notfound=1
                if (found==0 and notfound==1):
                    st331=('No key regenerartion found for storage <b>%s</b> in resource group <b>%s</b><br>\n' % (StorageName,RG))
                    passed33='<font color="red">Failed </font>('  
                totalvalue33 = totalvalue33+1
                st33=st33+st331
            except Exception as e:
                logger.error('Failing event logs iteration' + str(e))
        score33=[st33,passvalue33,totalvalue33,passed33]
        return score33
    except Exception as e:
        logger.error('Failed to Query Storage Accounts' + str(e))
        return ["Failed to Query Storage Accounts "]


def check34():
    print("Processing 34...")
    return "Check not available with azure CLI"

def check35():
    print("Processing 35...")
    return "Check not available with azure CLI"

def check36():
    print("Processing 36...")
    st36=""
    passvalue36 = 0
    totalvalue36 = 0
    score36=""
    passed36='<font color="red">Failed </font>('
    try:
        query36='az storage account list --query [*].[name,encryption.services.file.enabled]'
        json_cis=query_az(query36)
        #iteration through Storage Account
        for i in range(len(json_cis)):
            st36=st36+('Storage Account: <b>%s</b> status: <font color="blue"><b>%s</b></font><br>\n' % (json_cis[i][0],json_cis[i][1]))
            if (json_cis[i][1] is True):
                passvalue36=passvalue36+1
                passed36='<font color="green">Passed </font>('
            else:
                passed36='<font color="red">Failed </font>('  
            totalvalue36 = totalvalue36+1
        score36=[st36,passvalue36,totalvalue36,passed36]
        return score36
    except Exception as e:
        logger.error('Failed to Query Storage Accounts' + str(e))
        return ["Failed to Query Storage Accounts "]

def check37():
    print("Processing 37...")
    st37=""
    passvalue37 = 0
    totalvalue37 = 0
    score37=""
    passed37='<font color="green">Passed </font>('
    try:
        query37='az storage account list --query [*].[name,resourceGroup]'
        json_cis=query_az(query37)
        #iteration through Storage Account
        for i in range(len(json_cis)):
            SN=json_cis[i][0]
            RG=json_cis[i][1]
            try:
                query371=('az storage account keys list --account-name %s --resource-group %s --query [0].[value]' % (SN,RG))
                json_cis2=query_az(query371)
                KEY=json_cis2[0]
                try:
                    query372=('az storage container list  --account-name %s --account-key %s --query [*].[properties.publicAccess,name]' % (SN,KEY))
                    json_cis3=query_az(query372)
                    #iteration through containers
                    for j in range(len(json_cis3)):
                        CT=json_cis3[j][1]
                        if (json_cis3[j][0] is None):
                            st37=st37+('Private access for <b>%s</b> container in storage <b>%s</b><br>\n' % (CT,SN))
                            passvalue37=passvalue37+1
                        else:
                            st37=st37+('<font color="blue"><b>Public</b></font> access for <b>%s</b> container in storage <b>%s</b><br>\n' % (CT,SN))
                            passed37='<font color="red">Failed (</font>' 
                        totalvalue37 = totalvalue37+1
                except Exception as e:
                    logger.error('Failing iteration through containers (' + str(e))
                    return ["Failed iteration through containers"]
            except Exception as e:
                logger.error('Failing iteration through storage account (' + str(e))
                return ["Failed iteration through storage account "]
        score37=[st37,passvalue37,totalvalue37,passed37]
        return score37
    except Exception as e:
        logger.error('Failed to Query Storage Accounts (' + str(e))
        return ["Failed to Query Storage Accounts "]