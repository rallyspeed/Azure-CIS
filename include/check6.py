########################################################################
#!/usr/bin/python3

import os
import json
import logging


logger = logging.Logger('catch_all')

def query_az(query):
    json_cis=os.popen(query).read()
    return json.loads(json_cis)

def check62(subid):
    print("Processing 61 and 62...")
    acl61=""
    acl62=""
    failvalue61 = 0
    totalvalue61 = 0
    score61=""
    passed61='<font color="green">Passed </font>'
    failvalue62 = 0
    totalvalue62 = 0
    score62=""
    passed62='<font color="green">Passed </font>'
    try:
        query62='az network nsg list --query [*].[name,securityRules]'
        #query62=('az network nsg list --query "[?contains(id,\'%s\')].[name,securityRules]"' % subid)
        json_cis=query_az(query62)
        #i iteration number of NSG
        for i in range(len(json_cis)):
            #j iteration of ACL per NSG
            if (len(json_cis[i][1])>0):
                for j in range(len(json_cis[i][1])):
                    protocol=str(json_cis[i][1][j]['protocol'])
                    dport=str(json_cis[i][1][j]['destinationPortRange'])
                    action=str(json_cis[i][1][j]['access'])
                    src=str(json_cis[i][1][j]['sourceAddressPrefix'])
                    direction=str(json_cis[i][1][j]['direction'])
                    ## Check For Inbound RDP Access. Need to check for Port Range and list
                    ## Protocol TCP, UDP or *
                    if (protocol!="UDP" and ("3389" in dport) and action=="Allow" and src=="*" and direction=="Inbound"):
                        acl61=acl61+('Inbound RDP Allowed on nsg <b>%s</b><br>\n' % (str(json_cis[i][0])))
                        passed61='<font color="red">Failed </font>'
                        failvalue61=failvalue61+1
                    ## Check For Inbound SSH Access. Need to check for Port Range and list
                    if (protocol !="UDP" and ("22" in dport) and action=="Allow" and src=="*" and direction=="Inbound"):
                        acl62=acl62+('Inbound SSH Allowed on nsg <b>%s</b><br>\n' % (str(json_cis[i][0])))
                        passed62='<font color="red">Failed </font>'
                        failvalue62=failvalue62+1
            # If No ACL defined for NSG, assumed RDP/SSH not allowed
            else:
                acl61=('No Inbound RDP Allowed on any nsg <b>%s</b><br>\n' % (str(json_cis[i][0])))
                acl62=('No Inbound SSH Allowed on any nsg <b>%s</b><br>\n' % (str(json_cis[i][0])))
            totalvalue61 = totalvalue61+1
            totalvalue62 = totalvalue62+1                
            passvalue61=totalvalue61-failvalue61
            passvalue62=totalvalue62-failvalue62

        score61=[acl61,passvalue61,totalvalue61,passed61]
        score62=[acl62,passvalue62,totalvalue62,passed62]
        return [score61,score62]
    except Exception as e:
        logger.error('Failed to query for NSG ' + str(e))
        return ["Failed to query for NSG or SSH/RDP not allowed "]

def check63():
    print("Processing 63...")
    return ["Check not available with azure CLI"]

def check64(subid):
    print("Processing 64...")
    st64=""
    passvalue64 = 0
    totalvalue64 = 0
    score64=""
    passed64='<font color="green">Passed </font>'
    try:
        query64='az network nsg list --query [*][resourceGroup,name]'
        #query64=('az network nsg list --query "[?contains(id,\'%s\')].[resourceGroup,name]"' % subid)
        json_cis=query_az(query64)
        #iteration through NSG
        for i in range(len(json_cis)):
            RG = json_cis[i][0]
            NSG = json_cis[i][1]
            queryrp=("az network watcher flow-log show --resource-group %s --nsg %s" % (RG,NSG))
            try:
                json_cis2=query_az(queryrp)
                status=str(json_cis2['retentionPolicy']['enabled'])
                days=json_cis2['retentionPolicy']['days']
                if (days<90 or status is False):
                    passed64='<font color="red">Failed </font>'   
                else:
                    passvalue64=passvalue64+1
                totalvalue64 = totalvalue64+1
                st64=st64+('NSG: <b>%s</b> Enabled: <font color="blue"><b>%s</b></font> Days <font color="blue"><b>%d</b></font><br></li>\n' % (NSG,status,days))
            except Exception as e:
                logger.error('Failed to query for network watcher flow-log ' + str(e))
                return ["Failed to query for network watcher flow-log "]
        score64=[st64,passvalue64,totalvalue64,passed64]
        return score64
    except Exception as e:
        logger.error('Failed to query NSG ' + str(e))
        return ["Failed to query for NSG "]


def check65(subid):
    print("Processing 65...")
    passed65='<font color="red">Failed </font>'
    numberegions=0
    try:
        query65='az network watcher list'
        #query65=('az network watcher list --query "[?contains(id,\'%s\')]"' % subid)
        json_cis=query_az(query65)
        if (len(json_cis)>0):
            #iteration through existing regions
            for i in range(len(json_cis)):
                totalregions = 27
                numberegions = numberegions+1
                region = json_cis[i]['location']
                state = json_cis[i]['provisioningState']
            if (numberegions==27):
                passed65='<font color="green">Passed </font>'
            st65=('Enabled on <font color="blue"><b>%d</b></font>/%dregions</li>' % (numberegions, totalregions,))
            score65=[st65,numberegions,totalregions,passed65]
            return score65
        else:
            return ["Network Watcher not found"]
    except Exception as e:
        logger.error('Failed to query for network watcher ' + str(e))
        return ["Failed to query for network watcher "]