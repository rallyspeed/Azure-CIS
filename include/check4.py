################################## 2222222222222222222 #####################################
#!/usr/bin/python3

import os
import json
import logging
import requests
import sys


logger = logging.Logger('catch_all')

def query_az(query):
    json_cis=os.popen(query).read()
    return json.loads(json_cis)
	
def check41(subid):
    print("Processing 41...")
    return ["SQL Server Checks not implemented"]
'''
    try:
        query41=('az account get-access-token --subscription %s --query [accessToken]' % subid)
        json_cis20=query_az(query41)
        access_token=json_cis20[0]
        headers = {"Authorization": 'Bearer ' + access_token}
        request = ('https://management.azure.com/subscriptions/%s/providers/Microsoft.Sql/servers?api-version=2015-05-01-preview' % subid)
        try:
            json_output = requests.get(request, headers=headers).json()
            # Query through Azure Server
            for i in range(len(json_output)):
                id = json_output['value'][0][i]['id']
                print(id)
        except Exception as e:
            logger.error('Failing ' + str(e))
            return ["Failed to Query SQL Servers"]
    except Exception as e:
            logger.error('Failing' + str(e))
            return ["Failed to Get Access Token"]

    try:
        json_cis41=os.popen('Get-AzureRmSqlServer | ConvertTo-Json').read()
        #iteration through sql servers
        for i in range(len(json_cis41)):
            RG=json_cis41[i]['ResourceGroupName']
            SRV=json_cis41[i]['ServerName']
            query411=('Get-AzureRmSqlServerAuditing -ResourceGroupName %s -ServerName %s | ConvertTo-Json' % (RG,SRV))
            print(query411)
            json_cis411=os.popen(query411).read()
            print(json_cis411)
    except Exception as e:
        logger.error('Failing ' + str(e))
        return "Failed to Query SQL Servers"
'''	

def check42(subid):
    print("Processing 42...")
    chk421=""
    chk422=""
    chk423=""
    chk424=""
    chk425=""
    chk426=""
    chk427=""
    chk428=""
    totalDBI42 = 1 #Default Master
    passvalue421= 0
    score421=""
    passed421='<font color="green">Passed (</font>'
    passvalue422= 0
    score422=""
    passed422='<font color="green">Passed (</font>'
    passvalue423= 0
    score423=""
    passed423='<font color="green">Passed (</font>'
    passvalue424= 0
    score424=""
    passed424='<font color="green">Passed (</font>'
    passvalue425= 0
    score425=""
    passed425='<font color="green">Passed (</font>'
    passvalue426= 0
    score426=""
    passed426='<font color="green">Passed (</font>'
    passvalue427= 0
    score427=""
    passed427='<font color="green">Passed (</font>'
    passvalue428= 0
    score428=""
    passed428='<font color="red">Failed (</font>'
    try:
        query42='az sql server list --query "[*].[resourceGroup,name]"'
        json_cis=query_az(query42)
        if (len(json_cis)!=0):
            #iteration through sql servers
            for i in range(len(json_cis)):         
                RG=str(json_cis[i][0])
                SRV=str(json_cis[i][1])
                try: 
                    query421=("az sql db list --resource-group %s --server %s --query  [*].[name]" % (RG,SRV))
                    json_cis2=query_az(query421)
                    #iteration through db instances
                    for j in range(len(json_cis2)):
                        DB=str(json_cis2[j])
                        DB = DB.replace('[\'','')
                        DB = DB.replace('\']','')
                        if DB != "master":
                            query422=('az sql db audit-policy show --resource-group %s --server %s --name %s --query [retentionDays,state]' % (RG,SRV,DB))
                            query423=('az sql db threat-policy show --resource-group %s --server %s --name %s --query [retentionDays,state,disabledAlerts,emailAddresses,emailAccountAdmins]' % (RG,SRV,DB))
                            query424=('az sql db tde show --resource-group %s --server %s --database %s --query [status]' % (RG,SRV,DB))
                            json_cis3=query_az(query422)
                            json_cis4=query_az(query423)
                            json_cis5=query_az(query424)
                            chk421=chk421+('Instance <b>%s</b> on server %s in resource group %s state: <font color="blue"><b>%s</b></font><br>\n' % (DB,SRV,RG,json_cis3[1]))
                            if (json_cis3[1]=="Enabled"):
                                passed421='<font color="green">Passed (</font>'
                                passvalue421=passvalue421+1
                            else:
                                passed421='<font color="red">Failed (</font>'
                            chk422=chk422+('Instance <b>%s</b> on server %s in resource group %s state: <font color="blue"><b>%s</b></font><br>\n' % (DB,SRV,RG,json_cis4[1]))
                            if (json_cis4[1]=="Enabled"):
                                passed422=='<font color="green">Passed  (</font>'
                                passvalue422=passvalue422+1
                            else:
                                passed422='<font color="red">Failed (</font>'                        
                            chk423=chk423+('Instance <b>%s</b> on server %s in resource group %s disabledAlerts: <font color="blue"><b>%s</b></font><br>\n' % (DB,SRV,RG,json_cis4[2]))
                            if (json_cis4[2]!=""):
                                passed423=='<font color="green">Passed  (</font>'
                                passvalue423=passvalue423+1
                            else:
                                passed423='<font color="red">Failed (</font>'                          
                            chk424=chk424+('Instance <b>%s</b> on server %s in resource group %s emailAdd: <font color="blue"><b>%s</b></font><br>\n' % (DB,SRV,RG,json_cis4[3]))
                            if (json_cis4[3]!=""):
                                passed424=='<font color="green">Passed  (</font>'
                                passvalue424=passvalue424+1
                            else:
                                passed424='<font color="red">Failed (</font>'  
                            chk425=chk425+('Instance <b>%s</b> on server %s in resource group %s emailAdmins: <font color="blue"><b>%s</b></font><br>\n' % (DB,SRV,RG,json_cis4[4]))
                            if (json_cis4[4]=="Enabled"):
                                passed425=='<font color="green">Passed  (</font>'
                                passvalue425=passvalue425+1
                            else:
                                passed425='<font color="red">Failed (</font>'  
                            chk426=chk426+('Instance <b>%s</b> on server %s in resource group %s tde: <font color="blue"><b>%s</b></font><br>\n' % (DB,SRV,RG,json_cis5[0]))
                            if (json_cis5[0]=="Enabled"):
                                passed426=='<font color="green">Passed  (</font>'
                                passvalue426=passvalue426+1
                            else:
                                passed426=='<font color="red">Failed  (</font>'
                            chk427=chk427+('Instance <b>%s</b> on server %s in resource group %s retentionDays: <font color="blue"><b>%d</b></font><br>\n' % (DB,SRV,RG,json_cis3[0]))
                            if (json_cis3[0]>=90):
                                passed427=='<font color="green">Passed  (</font>'
                                passvalue427=passvalue427+1
                            else:
                                passed427='<font color="red">Failed (</font>'  
                            chk428=chk428+('Instance <b>%s</b> on server %s in resource group %s retentionDays: <font color="blue"><b>%d</b></font><br>\n' % (DB,SRV,RG,json_cis4[0]))
                            if (json_cis4[0]>=90):
                                passed428=='<font color="green">Passed  (</font>'
                                passvalue428=passvalue428+1
                            else:
                                passed428='<font color="red">Failed (</font>'  
                        totalDBI42 = totalDBI42+1
                except Exception as e:
                    #failed="Failed to Query DB"
                    logger.error('Failing ' + str(e))
                    return ["Failed to Query DB"]
                #Minus 1 to remove Master DB which comes by default
                totalDBI42 = totalDBI42 -1
                score421=[chk421,passvalue421,totalDBI42,passed421]
                score422=[chk422,passvalue422,totalDBI42,passed422]
                score423=[chk423,passvalue423,totalDBI42,passed423]
                score424=[chk424,passvalue424,totalDBI42,passed424]
                score425=[chk425,passvalue425,totalDBI42,passed425]
                score426=[chk426,passvalue426,totalDBI42,passed426]
                score427=[chk427,passvalue427,totalDBI42,passed427]
                score428=[chk428,passvalue428,totalDBI42,passed428]
                return [score421,score422,score423,score424,score425,score426,score427,score428]
        else:
            return ["N/A No SQL Servers Found"]
    except Exception as e:
        logger.error('Failing ' + str(e))
        return ["Failed to Query Server"]