########################################################################
#!/usr/bin/python3

import os
import json
import logging


logger = logging.Logger('catch_all')

def query_az(query):
    json_cis=os.popen(query).read()
    return json.loads(json_cis)

def check80():
    print("Processing 81 and 82...")
    chk81=""
    chk82=""
    passvalue81 = 0
    totalvalue81 = 0
    score81=""
    passed81='<font color="green">Passed </font>'
    passvalue82 = 0
    totalvalue82 = 0
    score82=""
    passed82='<font color="green">Passed </font>'
    try:
        query80='az keyvault list --query [*].[name]'
        json_cis=query_az(query80)
        #iteration through keyvault
        if (len(json_cis)>0):
            try:
                for i in range(len(json_cis)):
                    query81=('az keyvault key list --vault-name %s --query [*].[kid,attributes.expires]' % json_cis[i][0])
                    json_cis2=query_az(query81)
                    #iteration through vault
                    for j in range(len(json_cis2)):
                        chk81=chk81+('Expiry date: <b>%s</b> for kid %s in key vault <b>%s</b><br>\n' % (json_cis2[j][1],json_cis2[j][0],json_cis[i][0]))
                        if (json_cis2[j][1]!=""):
                            passvalue81=passvalue81+1
                        totalvalue81 = totalvalue81+1
                    query82=('az keyvault secret list --vault-name %s --query [*].[id,attributes.expires]' % json_cis[i][0])
                    json_cis3=query_az(query82)
                    #iteration through vault
                    for j in range(len(json_cis3)):
                        chk82=chk82+('Expiry date: <b>%s</b> for id %s in key vault <b>%s</b><br>\n' % (json_cis3[j][1],json_cis3[j][0],json_cis[i][0]))
                        if (json_cis3[j][1]!=""):
                            passvalue82=passvalue82+1
                        totalvalue82 = totalvalue82+1
                score81=[chk81,passvalue81,totalvalue81,passed81]
                score82=[chk82,passvalue82,totalvalue82,passed82]
                return [score81,score82]     
            except Exception as e:
                logger.error("Exception in check80: %s %s" %(type(e), str(e.args)))
                return ["Failed to iterate through keyvault for VM"]
        else:
            return ["No KeyVault Configured"]
    except Exception as e:
        logger.error("Exception in check80: %s %s" %(type(e), str(e.args)))
        return ["Failed to query keyvault"]

def check83():
    print("Processing 83...")
    chk83=""
    try:
        query83='az lock list --query [*].[level,name,resourceGroup]'
        json_cis=query_az(query83)
        if (len(json_cis)>0):
            #iteration through lock
            for i in range(len(json_cis)):
                chk83=chk83+('Lock status: <font color="blue"><b>%s</b></font> for lock <b><b>%s</b></b> in resource group <b>%s</b>s<br>\n' % (json_cis[i][0],json_cis[i][1],json_cis[i][2]))
        else:
            chk83="No Lock configured"
        return chk83
    except Exception as e:
        logger.error("Exception in check83: %s %s" %(type(e), str(e.args)))
        return "Failed to query lock"