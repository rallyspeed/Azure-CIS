########################################################################
#!/usr/bin/python3

import os
import json
import logging


logger = logging.Logger('catch_all')

def query_az(query):
    json_cis=os.popen(query).read()
    return json.loads(json_cis)

def check70(subid):
    print("Processing 7x...")
    chk71=""
    chk72="Disk Encryption Disabled"
    chk73="Disk Encryption Disabled"
    chk74=""
    chk75=""
    chk76=""
    passvalue71 = 0
    totalvalue71 = 0
    passvalue72 = 0
    totalvalue72 = 0
    passvalue73 = 0
    totalvalue73 = 0
    passvalue73 = 0
    totalvalue73 = 0
    passvalue74 = 0
    totalvalue74 = 0
    passvalue75 = 0
    totalvalue75 = 0
    passvalue76 = 0
    totalvalue76 = 0
    passed71='<font color="red">Failed </font>'
    passed72='<font color="red">Failed </font>'
    passed73='<font color="red">Failed </font>'
    passed74='<font color="red">Failed </font>'
    passed75='<font color="red">Failed </font>'
    passed76='<font color="green">Passed </font>'
    try:
        query70='az vm list --query "[*][resourceGroup,name]"'
        #query70=('az vm list --query "[?contains(id,\'%s\')].[resourceGroup,name]"' % subid)
        json_cis=query_az(query70)
        #i iteration per VM
        if (len(json_cis)>0):
            for i in range(len(json_cis)):
                rg = json_cis[i][0]
                vm = json_cis[i][1]
                print("Checking VM: %s within RG %s" % (vm,rg))
                try:
                    json_cis2=query_az("az vm show -g %s --n %s --query resources" % (rg,vm,))
                    for j in range(len(json_cis2)):
                        VMExt= json_cis2[j]['virtualMachineExtensionType']
                        if ("MicrosoftMonitoringAgent" in VMExt):
                            chk71=chk71+('VM: %s %s<br></li>' % (vm,VMExt,))
                            passvalue71=passvalue71+1
                            passed71='<font color="green">Passed </font>'
                        else:
                            chk71=chk71+('VM: <b>%s</b> is missing the VM Agent<br></li>' % vm )
                        if ("Antimalware" in VMExt):
                            chk76=chk76+('VM: <b>%s</b> has End Point Protection <font color="blue">Enabled</font><br></li>\n' %vm )
                            passvalue76=passvalue76+1
                        else:
                            chk76=chk76+('VM: <b>%s</b> has End Point Protection Disabled<br></li>\n' % vm)
                            passed76='<font color="red">Failed </font>'
                        chk74=chk74+('VM: <b>%s</b> installed extenion: <font color="blue">%s</font><br></li>\n' %(vm,json_cis2[j]['virtualMachineExtensionType'],))
                except:
                    chk71=chk71+('VM: <b>%s</b> has no resources configured<br></li>\n' % vm)
                    chk74=chk74+('VM: <b>%s</b> has no extension configured<br></li>\n' % vm )
                #try:
                    #json_cis3=query_az("az vm encryption show --resource-group %s --name %s --query osDisk" % (rg,vm,))
                    #chk72=chk72+str(json_cis3)
                #except:
                    #chk72=chk72+('VM: <b>%s</b> has no OSDisk encryption configured<br></li>' % vm )
                #try:
                    #json_cis4=query_az("az vm encryption show --resource-group %s --name %s --query dataDisk" % (rg,vm,))
                    #chk73=chk73+str(json_cis4)
                #except:
                    #chk73=chk73+('VM: <b>%s</b> has no dataDisk encryption configured<br></li>\n' % vm)
                totalvalue71 = totalvalue71+1
                totalvalue72 = totalvalue71
                totalvalue73 = totalvalue71
                totalvalue74 = totalvalue71
                totalvalue75 = totalvalue71
                totalvalue76 = totalvalue71
            chk75=chk75+"Check Not possible via Azure CLI</li>\n"
            score71=[passvalue71,totalvalue71,passed71]
            score72=[passvalue72,totalvalue72,passed72]
            score73=[passvalue73,totalvalue73,passed73]
            score74=[passvalue74,totalvalue74,passed74]
            score75=[passvalue75,totalvalue75,passed75]
            score76=[passvalue76,totalvalue76,passed76]
            return [chk71,chk72,chk73,chk74,chk75,chk76,score71,score72,score73,score74,score75,score76]
        else:
            return ["No VM Found"]
    except Exception as e:
        logger.error("Exception in check62: %s %s" %(type(e), str(e.args)))
        return ["Failed to query for VM"]