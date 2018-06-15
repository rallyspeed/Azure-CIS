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

def check11():
    print("Processing 11...")
    return "Check not available with azure CLI"

def check12():
    print("Processing 12...")
    return "Check not available with azure CLI"

def check13():
    print("Processing 13...")
    name=""
    try:
        query13='az ad user list --query "[?additionalProperties.userType==\'Guest\']"'
        json_cis=query_az(query13)
        for i in range(len(json_cis)):
            print(json_cis)
            name=json_cis[i][0]
            name=name+name
        return name
    except Exception as e:
        logger.error('Failed to Query Users' + str(e))
        return ["Failed to Query Userss"]

def check14():
    print("Processing 14...")
    return "Check not available with azure CLI"

def check15():
    print("Processing 15...")
    return "Check not available with azure CLI"

def check16():
    print("Processing 16...")
    return "Check not available with azure CLI"

def check17():
    print("Processing 17...")
    return "Check not available with azure CLI"

def check18():
    print("Processing 18...")
    return "Check not available with azure CLI"

def check19():
    print("Processing 19...")
    return "Check not available with azure CLI"

def check110():
    print("Processing 110...")
    return "Check not available with azure CLI"

def check111():
    print("Processing 111...")
    return "Check not available with azure CLI"

def check112():
    print("Processing 112...")
    return "Check not available with azure CLI"

def check113():
    print("Processing 113...")
    return "Check not available with azure CLI"

def check114():
    print("Processing 114...")
    return "Check not available with azure CLI"

def check115():
    print("Processing 115...")
    return "Check not available with azure CLI"

def check116():
    print("Processing 116...")
    return "Check not available with azure CLI"

def check117():
    print("Processing 117...")
    return "Check not available with azure CLI"

def check118():
    print("Processing 118...")
    return "Check not available with azure CLI"

def check119():
    print("Processing 119...")
    return "Check not available with azure CLI"

def check120():
    print("Processing 120...")
    return "Check not available with azure CLI"

def check121():
    print("Processing 121...")
    return "Check not available with azure CLI"

def check122():
    print("Processing 122...")
    return ["Check not available with azure CLI"]

def check123():
    print("Processing 123...")
    st123=""
    passvalue123 = 0
    failvalue123 = 0
    totalvalue123 = 0
    score123=""
    passed123='<font color="green">Passed </font>'
    try:
        query123='az role definition list --query [*][roleName,assignableScopes,permissions[].actions]'
        json_cis=query_az(query123)
        if (len(json_cis)>0):
            #iteration through roles
            for i in range(len(json_cis)):
                role = json_cis[i][0]
                scope= json_cis[i][1][0]
                actions = json_cis[i][2][0]
                #iteration through actions
                if (len(actions)>0):
                    for j in range(len(actions)):
                        if (scope=="/"  and actions[j]=="*"):
                            st123=st123+('Role <b>%s</b> with unrestricted access <br>\n' % role)
                            passed123='<font color="red">Failed </font>'
                            failvalue123=failvalue123+1
                    totalvalue123 = totalvalue123+1
                    passvalue123 = totalvalue123 - failvalue123
                else:
                    st123=st123+('No actions found for role <b>%s</b> with unrestricted access <br>\n' % role)
        else:
            st123="Roles not found"
        score123=[st123,passvalue123,totalvalue123,passed123]
        return score123
    except Exception as e:
        logger.error("Exception in check123: %s %s" %(type(e), str(e.args)))
        st123="Failed to query definition role"
        passed123='<font color="orange">UNKNOWN </font>'
        totalvalue123 = 1
        score123=[st123,passvalue123,totalvalue123,passed123]
        return score123