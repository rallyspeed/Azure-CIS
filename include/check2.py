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

def check21():
    print("Processing 21...")
    return "Check not available with azure CLI"

def check22(subid):
    print("Processing 22...")
    try:
        query20=('az account get-access-token --subscription %s --query [accessToken]' % subid)
        score22=['<font color="red">Failed</font>',0]
        score23=['<font color="red">Failed</font>',0]
        score24=['<font color="red">Failed</font>',0]
        score25=['<font color="red">Failed</font>',0]
        score26=['<font color="red">Failed</font>',0]
        score27=['<font color="red">Failed</font>',0]
        score28=['<font color="red">Failed</font>',0]
        score29=['<font color="red">Failed</font>',0]
        score210=['<font color="red">Failed</font>',0]
        score211=['<font color="red">Failed</font>',0]
        score212=['<font color="red">Failed</font>',0]
        score213=['<font color="red">Failed</font>',0]
        score214=['<font color="red">Failed</font>',0]
        score215=['<font color="red">Failed</font>',0]
        score216=['<font color="red">Failed</font>',0]
        score217=['<font color="red">Failed</font>',0]
        score218=['<font color="red">Failed</font>',0]
        score219=['<font color="red">Failed</font>',0]
        json_cis20=query_az(query20)
        access_token=json_cis20[0]
        headers = {"Authorization": 'Bearer ' + access_token}
        request = ('https://management.azure.com/subscriptions/%s/providers/microsoft.Security/policies?api-version=2015-06-01-preview' % subid)
        try:
            json_output = requests.get(request, headers=headers).json()
            value22=json_output['value'][0]['properties']['logCollection']
            value23=json_output['value'][0]['properties']['recommendations']['patch']
            value24=json_output['value'][0]['properties']['recommendations']['baseline']
            value25=json_output['value'][0]['properties']['recommendations']['antimalware']
            value26=json_output['value'][0]['properties']['recommendations']['diskEncryption']
            value27=json_output['value'][0]['properties']['recommendations']['nsgs']
            value28=json_output['value'][0]['properties']['recommendations']['waf']
            value29=json_output['value'][0]['properties']['recommendations']['ngfw']
            value210=json_output['value'][0]['properties']['recommendations']['vulnerabilityAssessment']
            value211=json_output['value'][0]['properties']['recommendations']['storageEncryption']
            value212=json_output['value'][0]['properties']['recommendations']['jitNetworkAccess']
            value213=json_output['value'][0]['properties']['recommendations']['appWhitelisting']
            value214=json_output['value'][0]['properties']['recommendations']['sqlAuditing']
            value215=json_output['value'][0]['properties']['recommendations']['sqlTde']
            value216=json_output['value'][0]['properties']['securityContactConfiguration']['securityContactEmails']
            value217=json_output['value'][0]['properties']['securityContactConfiguration']['securityContactPhone']
            value218=json_output['value'][0]['properties']['securityContactConfiguration']['areNotificationsOn']
            value219=json_output['value'][0]['properties']['securityContactConfiguration']['sendToAdminOn']
            if (value22=="On"):
                score22=['<font color="green">Passed</font>',1]
            if (value23=="On"):
                score23=['<font color="green">Passed</font>',1]
            if (value24=="On"):
                score24=['<font color="green">Passed</font>',1]
            if (value25=="On"):
                score25=['<font color="green">Passed</font>',1]
            if (value26=="On"):
                score26=['<font color="green">Passed</font>',1]
            if (value27=="On"):
                score27=['<font color="green">Passed</font>',1]
            if (value28=="On"):
                score28=['<font color="green">Passed</font>',1]
            if (value29=="On"):
                score29=['<font color="green">Passed</font>',1]
            if (value210=="On"):
                score210=['<font color="green">Passed</font>',1]
            if (value211=="On"):
                score211=['<font color="green">Passed</font>',1]
            if (value212=="On"):
                score212=['<font color="green">Passed</font>',1]
            if (value213=="On"):
                score213=['<font color="green">Passed</font>',1]
            if (value214=="On"):
                score214=['<font color="green">Passed</font>',1]
            if (value215=="On"):
                score215=['<font color="green">Passed</font>',1]
            if (value216!=""):
                score216=['<font color="green">Passed</font>',1]
            if (value217!=""):
                score217=['<font color="green">Passed</font>',1]
            if (value218):
                score218=['<font color="green">Passed</font>',1]
            if (value219):
                score219=['<font color="green">Passed</font>',1]                                                                        
            chk22=('Current Setting: <font color="blue"> %s</b></font>' % value22)
            chk23=('Current Setting: <font color="blue"> %s</b></font>' % value23)
            chk24=('Current Setting: <font color="blue"> %s</b></font>' % value24)
            chk25=('Current Setting: <font color="blue"> %s</b></font>' % value25)
            chk26=('Current Setting: <font color="blue"> %s</b></font>' % value26)
            chk27=('Current Setting: <font color="blue"> %s</b></font>' % value27)
            chk28=('Current Setting: <font color="blue"> %s</b></font>' % value28)
            chk29=('Current Setting: <font color="blue"> %s</b></font>' % value29)
            chk210=('Current Setting: <font color="blue"> %s</b></font>' % value210)
            chk211=('Current Setting: <font color="blue"> %s</b></font>' % value211)
            chk212=('Current Setting: <font color="blue"> %s</b></font>' % value212)
            chk213=('Current Setting: <font color="blue"> %s</b></font>' % value213)
            chk214=('Current Setting: <font color="blue"> %s</b></font>' % value214)
            chk215=('Current Setting: <font color="blue"> %s</b></font>' % value215)
            chk216=('Current Setting: <font color="blue"> %s</b></font>' % value216)
            chk217=('Current Setting: <font color="blue"> %s</b></font>' % value217)
            chk218=('Current Setting: <font color="blue"> %s</b></font>' % value218)
            chk219=('Current Setting: <font color="blue"> %s</b></font>' % value219)
            return [chk22,chk23,chk24,chk25,chk26,chk27,chk28,chk29,chk210,chk211,chk212,chk213,chk214,chk215,chk216,chk217,chk218,chk219,score22,score23,score24,score25,score26,score27,score28,score29,score210,score211,score212,score213,score214,score215,score216,score217,score218,score219]
        except:
            return "Failed to make API call"
    except Exception as e:
        logger.error('Failing ' + str(e))
        return "Failed to Query"
################################## 333333333333333333333333 #####################################