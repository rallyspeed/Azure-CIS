#!/usr/bin/python3
# @Author Mathieu Durand
# Version 1.0

import subprocess
import sys
import datetime
import os
from include import check1,check2,check3,check4,check5,check6,check7,check8,subscription
from html.parser import HTMLParser


################ CSV EXPORT HELPERS ###################
# Use HTML Parser
class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.strict = False
        self.convert_charrefs= True
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

# Strip HTML tags
def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()

# Process a CSV Column: strip HTML tags, wrap with double-quotes, replace double-quotes with single-quotes, replace line breaks with newline
def c(text):
    #return '"'+ str(text).strip().replace("<br>", "\n").replace("<b>","'").replace("</b>","'").replace('"',"'") + '",'
    return '"'+ str(text).strip().replace("<br>", "\n").replace('"',"'") + '",'

# Process a CSV Row: Add Subscription name column, add newline
subname=""
def r(text):
    return '"' + subname + '",' + text + "\n"

################ HTML HEADER ###################
def generate_report(subid,name,cloudname):
    global subname
    subname=name

    html_start = """
<html>
<head>
<title>Azure CIS Benchmark</title>
</head>
<body>
<h1><center>Azure CIS Benchmark for """+name+"""</center></h1>
<font size="-1">
"""
    html_end = """
</body>
</html>
"""

    start_list="<li><b>\n"
    end_list="</h3></li></b>\n"

################ HTML 1.x ##############
    content1 = """
<h2>CIS Azure 1.x</h2>
<ul>
"""
    content11="1.1 Ensure that multi-factor authentication is enabled for all privileged users"
    content12="1.2 Ensure that multi-factor authentication is enabled for all nonprivileged users"
    content13="1.3 Ensure that there are no guest users"
    content14="1.4 Ensure that 'Allow users to remember multi-factor authentication on devices they trust' is 'Disabled'"
    content15="1.5 Ensure that 'Number of methods required to reset' is set to '2'"
    content16="1.6 Ensure that 'Number of days before users are asked to re-confirm their authentication information' is not set to '0"
    content17="1.7 Ensure that 'Notify users on password resets?' is set to 'Yes'"
    content18="1.8 Ensure that 'Notify all admins when other admins reset their password?' is set to 'Yes'"
    content19="1.9 Ensure that 'Users can consent to apps accessing company data on their behalf' is set to 'No'"
    content110="1.10 Ensure that 'Users can add gallery apps to their Access Panel' is set to 'No'"
    content111="1.11 Ensure that 'Users can register applications' is set to 'No'"
    content112="1.12 Ensure that 'Guest users permissions are limited' is set to 'Yes'"
    content113="1.13 Ensure that 'Members can invite' is set to 'No'"
    content114="1.14 Ensure that 'Guests can invite' is set to 'No'"
    content115="1.15 Ensure that 'Restrict access to Azure AD administration portal' is set to 'Yes'"
    content116="1.16 Ensure that 'Self-service group management enabled' is set to 'No'"
    content117="1.17 Ensure that 'Users can create security groups' is set to 'No'"
    content118="1.18 Ensure that 'Users who can manage security groups' is set to 'None'"
    content119="1.19 Ensure that 'Users can create Office 365 groups' is set to 'No'"
    content120="1.20 Ensure that 'Users who can manage Office 365 groups' is set to 'None'"
    content121="1.21 Ensure that 'Enable 'All Users' group' is set to 'Yes'"
    content122="1.22 Ensure that 'Require Multi-Factor Auth to join devices' is set to 'Yes'"
    content123="1.23 Ensure that no custom subscription owner roles are created"

    result11=check1.check11(subid)
    #sys.exit(0)
    result12=check1.check12()
    result13=check1.check13()
    result110=check1.check110()
    result111=check1.check111()
    result112=check1.check112()
    result113=check1.check113()
    result114=check1.check114()
    result115=check1.check115()
    result116=check1.check116()
    result117=check1.check117()
    result118=check1.check118()
    result119=check1.check119()
    result120=check1.check120()
    result121=check1.check121()
    result122=check1.check122()
    result123=check1.check123()
    content1_1 = '<h3 id="content11">'+start_list+content11+end_list+result11[0]+'<h3 id="content12">'+start_list+content12+end_list+result12[0]+'<h3 id="content13">'+start_list+content13+end_list+result13[0]
    #14-15-16 content1_2 = '<h3 id="content11">'+start_list+content11+end_list+check1.check11()+'<h3 id="content12">'+start_list+content12+end_list+result12[0]+'<h3 id="content13">'+start_list+content13+end_list+result13[0]
    #17-18-19 content1_3 = '<h3 id="content11">'+start_list+content11+end_list+check1.check11()+'<h3 id="content12">'+start_list+content12+end_list+result12[0]+'<h3 id="content13">'+start_list+content13+end_list+result13[0]
    content1_4 = '<h3 id="content110">'+start_list+content110+end_list+result110[0]+'<h3 id="content111">'+start_list+content111+end_list+result111[0]+'<h3 id="content112">'+start_list+content112+end_list+result112[0]
    content1_5 = '<h3 id="content113">'+start_list+content113+end_list+result113[0]+'<h3 id="content114">'+start_list+content114+end_list+result114[0]+'<h3 id="content115">'+start_list+content115+end_list+result115[0]
    content1_6 = '<h3 id="content116">'+start_list+content116+end_list+result116[0]+'<h3 id="content117">'+start_list+content117+end_list+result117[0]+'<h3 id="content118">'+start_list+content118+end_list+result118[0]
    content1_7 = '<h3 id="content119">'+start_list+content119+end_list+result119[0]+'<h3 id="content120">'+start_list+content120+end_list+result120[0]+'<h3 id="content121">'+start_list+content121+end_list+result121[0]
    content1_8 = '<h3 id="content122">'+start_list+content122+end_list+result122[0]+'<h3 id="content123">'+start_list+content123+end_list+result123[0]

    content1=content1+content1_1+content1_4+content1_5+content1_6+content1_7+content1_8 

################ HTML 2.x ##############
    content2 = """
<h2>CIS Azure 2.x</h2>
<ul>
"""
    content21="2.1 Ensure that standard pricing tier is selected"
    content22="2.2 Ensure that 'Automatic provisioning of monitoring agent' is set to 'On'"
    content23="2.3 Ensure that 'System updates' is set to 'On'"
    content24="2.4 Ensure that 'Security Configurations' is set to 'On'"
    content25="2.5 Ensure that 'Endpoint protection' is set to 'On'"
    content26="2.6 Ensure that 'Disk encryption' is set to 'On'"
    content27="2.7 Ensure that 'Network security groups' is set to 'On'"
    content28="2.8 Ensure that 'Web application firewall' is set to 'On'"
    content29="2.9 Ensure that 'Next generation firewall' is set to 'On'"
    content210="2.10 Ensure that 'Vulnerability assessment' is set to 'On'"
    content211="2.11 Ensure that 'Storage Encryption' is set to 'On'"
    content212="2.12 Ensure that 'JIT Network Access' is set to 'On'"
    content213="2.13 Ensure that 'Adaptive Application Controls' is set to 'On'"
    content214="2.14 Ensure that 'SQL auditing & Threat detection' is set to 'On'"
    content215="2.15 Ensure that 'SQL Encryption' is set to 'On'"
    content216="2.16 Ensure that 'Security contact emails' is set"
    content217="2.17 Ensure that security contact 'Phone number' is set"
    content218="2.18 Ensure that 'Send me emails about alerts' is set to 'On'"
    content219="2.19 Ensure that 'Send email also to subscription owners' is set to 'On'"

    result21=check2.check21()
    result22=check2.check22(subid)
    content2_1 = '<h3 id="content21">'+start_list+content21+end_list+result21+'<h3 id="content22">'+start_list+content22+end_list+result22[0]+'<h3 id="content23">'+start_list+content23+end_list+result22[1]
    content2_2 = '<h3 id="content24">'+start_list+content24+end_list+result22[2]+'<h3 id="content25">'+start_list+content25+end_list+result22[3]+'<h3 id="content26">'+start_list+content26+end_list+result22[4]+'<h3 id="content27">'+start_list+content27+end_list+result22[5]+'<h3 id="content28">'+start_list+content28+end_list+result22[6]
    content2_3 = '<h3 id="content29">'+start_list+content29+end_list+result22[7]+'<h3 id="content210">'+start_list+content210+end_list+result22[8]+'<h3 id="content211">'+start_list+content211+end_list+result22[9]
    content2_4 = '<h3 id="content212">'+start_list+content212+end_list+result22[10]+'<h3 id="content213">'+start_list+content213+end_list+result22[11]+'<h3 id="content214">'+start_list+content214+end_list+result22[12]
    content2_5 = '<h3 id="content215">'+start_list+content215+end_list+result22[13]+'<h3 id="content216">'+start_list+content216+end_list+result22[14]+'<h3 id="content217">'+start_list+content217+end_list+result22[15]
    content2_6 = '<h3 id="content218">'+start_list+content218+end_list+result22[16]+'<h3 id="content219">'+start_list+content219+end_list+result22[17]
    content2 = content2 + content2_1 + content2_2 + content2_3 + content2_4 + content2_5+ content2_6

    ############ HTML 3.x ##############
    content3 = """
<h2>CIS Azure 3.x</h2>
<ul>
"""
    result31=check3.check31()
    result32=check3.check32()
    result33=check3.check33()
    result34=check3.check34()
    result35=check3.check35()
    result36=check3.check36()
    result37=check3.check37()
    content31="3.1 Ensure that 'Secure transfer required' is set to 'Enabled'"
    content32="3.2 Ensure that 'Storage service encryption' is set to Enabled for Blob Service"
    content33="3.3 Ensure that storage account access keys are periodically regenerated"
    content34="3.4 Ensure that shared access signature tokens expire within an hour"
    content35="3.5 Ensure that shared access signature tokens are allowed only over https"
    content36="3.6 Ensure that 'Storage service encryption' is set to Enabled for File Service"
    content37="3.7 Ensure that 'Public access level' is set to Private for blob containers"
    

    content3_1 = '<h3 id="content31">'+start_list+content31+end_list+result31[0]
    content3_2 = '<h3 id="content32">'+start_list+content32+end_list+result32[0]
    content3_3 = '<h3 id="content33">'+start_list+content33+end_list+result33[0]
    content3_4 = '<h3 id="content34">'+start_list+content34+end_list+result34+'<h3 id="content35">'+start_list+content35+end_list+result35+'<h3 id="content36">'+start_list+content36+end_list+result36[0]+'<h3 id="content37">'+start_list+content37+end_list+result37[0]
    content3 = content3+content3_1+content3_2+content3_3+content3_4

################ HTML 4.x ##############
    content4 = """
<h2>CIS Azure 4.x</h2>
<ul>
"""
    content411="4.1.1 Ensure that 'Auditing' is set to 'On'"
    content412="4.1.2 Ensure that 'Threat Detection' is set to 'On'"
    content413="4.1.3 Ensure that 'Threat Detection types' is set to 'All'"
    content414="4.1.4 Ensure that 'Send alerts to' is set"
    content415="4.1.5 Ensure that 'Email service and co-administrators' is 'Enabled'"
    content416="4.1.6 Ensure that 'Auditing' Retention is 'greater than 90 days'"
    content417="4.1.7 Ensure that 'Threat Detection' Retention is 'greater than 90 days'"
    content418="4.1.8 Ensure that Azure Active Directory Admin is configured"

    result41 = check4.check41(subid)
    content41_1 = start_list+content411+end_list#+check41()+start_list+content412+end_list+check41()+start_list+content413+end_list+check41()+end_list
    content41_2 = start_list+content414+end_list#+check41()+start_list+content415+end_list+check41()+start_list+content416+end_list+check41()+start_list+content417+end_list+check41()+start_list+content418+end_list+check41()
    content41 = content41_1+content41_2

    
    content421="4.2.1 Ensure that 'Auditing' is set to 'On'"
    content422="4.2.2 Ensure that 'Threat Detection' is set to 'On'"
    content423="4.2.3 Ensure that 'Threat Detection types' is set to 'All'"
    content424="4.2.4 Ensure that 'Send alerts to' is set"
    content425="4.2.5 Ensure that 'Email service and co-administrators' is 'Enabled'"
    content426="4.2.6 Ensure that 'Data encryption' is set to 'On'"
    content427="4.2.7 Ensure that 'Auditing' Retention is 'greater than 90 days'"
    content428="4.2.8 Ensure that 'Threat' Retention is 'greater than 90 days'"

    result42 = check4.check42(subid)

    content42_1 = '<h3 id="content421">'+start_list+content421+end_list+result42[0][0]+'<h3 id="content422">'+start_list+content422+end_list+result42[1][0]+'<h3 id="content423">'+start_list+content423+end_list+result42[2][0]
    content42_2 = '<h3 id="content424">'+start_list+content424+end_list+result42[3][0]+'<h3 id="content425">'+start_list+content425+end_list+result42[4][0]+'<h3 id="content426">'+start_list+content426+end_list+result42[5][0]
    content42_3 = '<h3 id="content427">'+start_list+content427+end_list+result42[6][0]+'<h3 id="content428">'+start_list+content428+end_list+result42[7][0]
    content42 = content42_1+content42_2+content42_3

    content4 = content4 + content41 + content42


################ HTML 5.x ##############
    content5 = """
<h2>CIS Azure 5.x</h2>
<ul>
"""
    content51="5.1 Ensure that a Log Profile exists"
    content52="5.2 Ensure that Activity Log Retention is set 365 days or greater"
    content53="5.3 Ensure that Activity Log Alert exists for Create Policy Assignment"
    content54="5.4 Ensure that Activity Log Alert exists for Create or Update Network Security Group"
    content55="5.5 Ensure that Activity Log Alert exists for Delete Network Security Group"
    content56="5.6 Ensure that Activity Log Alert exists for Create or Update Network Security Group Rule"
    content57="5.7 Ensure that Activity Log Alert exists for Delete Network Security Group Rule"
    content58="5.8 Ensure that Activity Log Alert exists for Create or Update Security Solution"
    content59="5.9 Ensure that Activity Log Alert exists for Delete Security Solution"
    content510="5.10 Ensure that Activity Log Alert exists for Create or Update SQL Server Firewall Rule"
    content511="5.11 Ensure that Activity Log Alert exists for Delete SQL Server Firewall Rule"
    content512="5.12 Ensure that Activity Log Alert exists for Update Security Policy"
    content513="5.13 Ensure that logging for Azure KeyVault is 'Enabled'"

    result5=check5.check50(subid)

    content5_1 = '<h3 id="content51">'+start_list+content51+end_list+result5[0]+'<h3 id="content52">'+start_list+content52+end_list+result5[1]+'<h3 id="content53">'+start_list+content53+end_list+result5[2]
    content5_2 = '<h3 id="content54">'+start_list+content54+end_list+result5[3]+'<h3 id="content55">'+start_list+content55+end_list+result5[4]+'<h3 id="content56">'+start_list+content56+end_list+result5[5]+'<h3 id="content57">'+start_list+content57+end_list+result5[6]+'<h3 id="content58">'+start_list+content58+end_list+result5[7]
    content5_3 = '<h3 id="content59">'+start_list+content59+end_list+result5[8]+'<h3 id="content510">'+start_list+content510+end_list+result5[9]+'<h3 id="content511">'+start_list+content511+end_list+result5[10]
    content5_4 = '<h3 id="content512">'+start_list+content512+end_list+result5[11]+'<h3 id="content513">'+start_list+content513+end_list+result5[12]
    content50 = content5_1 + content5_2 + content5_3 + content5_4
    content5 = content5 + content50

################ HTML 6.x ##############
    content6 = """
<h2>CIS Azure 6.x</h2>
<ul>
"""
    result62=check6.check62(subid)
    result63=check6.check63()
    result64=check6.check64(subid)
    result65=check6.check65(subid)
    content61="6.1 Ensure that RDP access is restricted from the internet"
    content62="6.2 Ensure that SSH access is restricted from the internet"
    content63="6.3 Ensure that SQL server access is restricted from the internet"
    content64="6.4 Ensure that Network Security Group Flow Log retention period is greater than 90 days"
    content65="6.5 Ensure that Network Watcher is Enabled"
    
    content6_1 = '<h3 id="content61">'+start_list+content61+end_list+result62[0][0]+'<h3 id="content62">'+start_list+content62+end_list+result62[1][0]+'<h3 id="content63">'+start_list+content63+end_list+result63[0]
    content6_2 = '<h3 id="content64">'+start_list+content64+end_list+result64[0]
    content6_3 = '<h3 id="content65">'+start_list+content65+end_list+result65[0]

    content6=content6+content6_1+content6_2+content6_3

################ HTML 7.x ##############
    content7 = """
<h2>CIS Azure 7.x</h2>
<ul>
"""

    content71="7.1 Ensure that VM agent is installed"
    content72="7.2 Ensure that 'OS disk' are encrypted"
    content73="7.3 Ensure that 'Data disks' are encrypted"
    content74="7.4 Ensure that only approved extensions are installed"
    content75="7.5 Ensure that the latest OS Patches for all Virtual Machines are applied"
    content76="7.6 Ensure that the endpoint protection for all Virtual Machines is installed"

    result7=check7.check70(subid)

    content7_1 = '<h3 id="content71">'+start_list+content71+end_list+result7[0]+'<h3 id="content72">'+start_list+content72+end_list+result7[1]+'<h3 id="content73">'+start_list+content73+end_list+result7[2]
    content7_2 = '<h3 id="content74">'+start_list+content74+end_list+result7[3]+'<h3 id="content75">'+start_list+content75+end_list+result7[4]+'<h3 id="content76">'+start_list+content76+end_list+result7[5]
    content7=content7+content7_1+content7_2


################ HTML 8.x ##############
    content8 = """
<h2>CIS Azure 8.x</h2>
<ul>
"""
    
    content81="8.1 Ensure that the expiry date is set on all Keys"
    content82="8.2 Ensure that the expiry date is set on all Secrets"
    content83="8.3 Ensure that Resource Locks are set for mission critical Azure resources"
    
    result80=check8.check80()
    result83=check8.check83()
    content8 = content8+'<h3 id="content81">'+start_list+content81+end_list+result80[0][0]+'<h3 id="content82">'+start_list+content82+end_list+result80[1][0]+'<h3 id="content83">'+start_list+content83+end_list+result83
    
    print("Finished Queries")
    print("Generating Report")
############## Summary Table ##########
    summary0 = """
<h1 id="Summary">1 - Score Summary</h1>
<style>
table, th, td {
    border: 1px solid black;
    border-collapse: collapse;
}
th, td {
    padding: 5px;
    font-size: small;
th {
    text-align: left;
}
</style>
<table style="width:80%">
<tr>
    <th>Check Description</th> 
    <th>Tests</th>
    <th>Score</th>
    <th>Comments</th>
</tr>
"""
########################################################################################################################
############################################################ Summary 1 #################################################
########################################################################################################################
#Calculate % Passed

    perc13=round(100*result13[1]/result13[2],2)
    perc123=round(100*result123[1]/result123[2],2)

    calc1=(perc13+perc123)/2
    score1= round(calc1,2)

    summary1 = """
<tr>
    <td><b>1 Identity and Access Management</b></td> 
    <td></td>
    <td><b>"""+str(score1)+"""%</b></td>
    <td></td>
</tr>
<tr>
    <td><a href="#content13">"""+content13+"""</a></td> 
    <td>"""+result13[3]+str(result13[1])+"""/"""+str(result13[2])+"""</td>
    <td>"""+str(perc13)+"""%</td>
    <td></td>
</tr>
<tr>
    <td><a href="#content14">"""+content14+"""</a></td> 
    <td>Unavailable</td>
    <td>Unavailable</td>
    <td></td>
</tr>
<tr>
    <td><a href="#content15">"""+content15+"""</a></td> 
    <td>Unavailable</td>
    <td>Unavailable</td>
    <td></td>
</tr>
<tr>
    <td><a href="#content16">"""+content16+"""</a></td> 
    <td>Unavailable</td>
    <td>Unavailable</td>
    <td></td>
</tr>
<tr>
    <td><a href="#content17">"""+content17+"""</a></td> 
    <td>Unavailable</td>
    <td>Unavailable</td>
    <td></td>
</tr>
<tr>
    <td><a href="#content18">"""+content18+"""</a></td> 
    <td>Unavailable</td>
    <td>Unavailable</td>
    <td></td>
</tr>
<tr>
    <td><a href="#content19">"""+content19+"""</a></td> 
    <td>Unavailable</td>
    <td>Unavailable</td>
    <td></td>
</tr>
<tr>
    <td><a href="#content110">"""+content110+"""</a></td> 
    <td>Unavailable</td>
    <td>Unavailable</td>
    <td></td>
</tr>
<tr>
    <td><a href="#content111">"""+content111+"""</a></td> 
    <td>Unavailable</td>
    <td>Unavailable</td>
    <td></td>
</tr>
<tr>
    <td><a href="#content112">"""+content112+"""</a></td> 
    <td>Unavailable</td>
    <td>Unavailable</td>
    <td></td>
</tr>
<tr>
    <td><a href="#content113">"""+content113+"""</a></td> 
    <td>Unavailable</td>
    <td>Unavailable</td>
    <td></td>
</tr>
<tr>
    <td><a href="#content114">"""+content114+"""</a></td> 
    <td>Unavailable</td>
    <td>Unavailable</td>
    <td></td>
</tr>
<tr>
    <td><a href="#content115">"""+content115+"""</a></td> 
    <td>Unavailable</td>
    <td>Unavailable</td>
    <td></td>
</tr>
<tr>
    <td><a href="#content116">"""+content116+"""</a></td> 
    <td>Unavailable</td>
    <td>Unavailable</td>
    <td></td>
</tr>
<tr>
    <td><a href="#content117">"""+content117+"""</a></td> 
    <td>Unavailable</td>
    <td>Unavailable</td>
    <td></td>
</tr>
<tr>
    <td><a href="#content118">"""+content118+"""</a></td> 
    <td>Unavailable</td>
    <td>Unavailable</td>
    <td></td>
</tr>
<tr>
    <td><a href="#content119">"""+content119+"""</a></td> 
    <td>Unavailable</td>
    <td>Unavailable</td>
    <td></td>
</tr>
<tr>
    <td><a href="#content120">"""+content120+"""</a></td> 
    <td>Unavailable</td>
    <td>Unavailable</td>
    <td></td>
</tr>
<tr>
    <td><a href="#content121">"""+content121+"""</a></td> 
    <td>Unavailable</td>
    <td>Unavailable</td>
    <td></td>
</tr>
<tr>
    <td><a href="#content122">"""+content122+"""</a></td> 
    <td>Unavailable</td>
    <td>Unavailable</td>
    <td></td>
</tr>
<tr>
    <td><a href="#content123">"""+content123+"""</a></td> 
    <td>"""+result123[3]+str(result123[1])+"""/"""+str(result123[2])+"""</td>
    <td>"""+str(perc123)+"""%</td>
    <td></td>
</tr>
"""

########################################################################################################################
############################################################ Summary 2 #################################################
########################################################################################################################
#Calculate % Passed, check 21 is ignored

    calc2=100*(result22[18][1]+result22[19][1]+result22[20][1]+result22[21][1]+result22[22][1]+result22[23][1]+result22[24][1]+result22[25][1]+result22[26][1]+result22[27][1]+result22[28][1]+result22[29][1]+result22[30][1]+result22[31][1]+result22[32][1]+result22[33][1]+result22[34][1]+result22[35][1])/18
    
    score2= round(calc2,2)

    summary2 = """
<tr>
    <td><b>2 Security Center</b></td> 
    <td></td>
    <td><b>"""+str(score2)+"""%</b></td>
    <td></td>
</tr>
<tr>
    <td><a href="#content21">"""+content21+"""</a></td> 
    <td>Unavailable</td>
    <td>Unavailable</td>
    <td>Unavailable</td>
</tr>
<tr>
    <td><a href="#content22">"""+content22+"""</a></td> 
    <td>"""+result22[18][0]+"""</td>
    <td>"""+str(100*result22[18][1])+"""%</td>
    <td></td>
</tr>
<tr>
    <td><a href="#content23">"""+content23+"""</a></td> 
    <td>"""+result22[19][0]+"""</td>
    <td>"""+str(100*result22[19][1])+"""%</td>
    <td></td>
</tr>
<tr>
    <td><a href="#content24">"""+content24+"""</a></td> 
    <td>"""+result22[20][0]+"""</td>
    <td>"""+str(100*result22[20][1])+"""%</td>
    <td></td>
</tr>
<tr>
    <td><a href="#content25">"""+content25+"""</a></td> 
    <td>"""+result22[21][0]+"""</td>
    <td>"""+str(100*result22[21][1])+"""%</td>
    <td></td>
</tr>
<tr>
    <td><a href="#content26">"""+content26+"""</a></td> 
    <td>"""+result22[22][0]+"""</td>
    <td>"""+str(100*result22[22][1])+"""%</td>
    <td></td>
</tr>
<tr>
    <td><a href="#content27">"""+content27+"""</a></td> 
    <td>"""+result22[23][0]+"""</td>
    <td>"""+str(100*result22[23][1])+"""%</td>
    <td></td>
</tr>
<tr>
    <td><a href="#content28">"""+content28+"""</a></td> 
    <td>"""+result22[24][0]+"""</td>
    <td>"""+str(100*result22[24][1])+"""%</td>
    <td></td>
</tr>
<tr>
    <td><a href="#content29">"""+content29+"""</a></td> 
    <td>"""+result22[25][0]+"""</td>
    <td>"""+str(100*result22[25][1])+"""%</td>
    <td></td>
</tr>
<tr>
    <td><a href="#content210">"""+content210+"""</a></td> 
    <td>"""+result22[26][0]+"""</td>
    <td>"""+str(100*result22[26][1])+"""%</td>
    <td></td>
</tr>
<tr>
    <td><a href="#content211">"""+content211+"""</a></td> 
    <td>"""+result22[27][0]+"""</td>
    <td>"""+str(100*result22[27][1])+"""%</td>
    <td></td>
</tr>
<tr>
    <td><a href="#content212">"""+content212+"""</a></td> 
    <td>"""+result22[28][0]+"""</td>
    <td>"""+str(100*result22[28][1])+"""%</td>
    <td></td>
</tr>
<tr>
    <td><a href="#content213">"""+content213+"""</a></td> 
    <td>"""+result22[29][0]+"""</td>
    <td>"""+str(100*result22[29][1])+"""%</td>
    <td></td>
</tr>
<tr>
    <td><a href="#content214">"""+content214+"""</a></td> 
    <td>"""+result22[30][0]+"""</td>
    <td>"""+str(100*result22[30][1])+"""%</td>
    <td></td>
</tr>
<tr>
    <td><a href="#content215">"""+content215+"""</a></td> 
    <td>"""+result22[31][0]+"""</td>
    <td>"""+str(100*result22[31][1])+"""%</td>
    <td></td>
</tr>
<tr>
    <td><a href="#content216">"""+content216+"""</a></td> 
    <td>"""+result22[32][0]+"""</td>
    <td>"""+str(100*result22[32][1])+"""%</td>
    <td></td>
</tr>
<tr>
    <td><a href="#content217">"""+content217+"""</a></td> 
    <td>"""+result22[33][0]+"""</td>
    <td>"""+str(100*result22[33][1])+"""%</td>
    <td></td>
</tr>
<tr>
    <td><a href="#content218">"""+content218+"""</a></td> 
    <td>"""+result22[34][0]+"""</td>
    <td>"""+str(100*result22[34][1])+"""%</td>
    <td></td>
</tr>
<tr>
    <td><a href="#content219">"""+content219+"""</a></td> 
    <td>"""+result22[35][0]+"""</td>
    <td>"""+str(100*result22[35][1])+"""%</td>
    <td></td>
</tr>
"""
    print("Finished Summary 2")

########################################################################################################################
############################################################ Summary 3 #################################################
########################################################################################################################
#Calculate % Passed, 34 and 35 ignored

    perc31=round(100*result31[1]/result31[2],2)
    perc32=round(100*result32[1]/result32[2],2)
    perc33=round(100*result33[1]/result33[2],2)
    perc36=round(100*result36[1]/result36[2],2)
    perc37=round(100*result37[1]/result37[2],2)

    calc3=(perc31+perc32+perc36+perc37)/4
    score3= round(calc3,2)

    summary3 = """
<tr>
    <td><b>3 Storage Accounts</b></td> 
    <td></td>
    <td><b>"""+str(score3)+"""%</b></td>
    <td></td>
</tr>
<tr>
    <td><a href="#content31">"""+content31+"""</a></td> 
    <td>"""+result31[3]+str(result31[1])+"""/"""+str(result31[2])+"""</td>
    <td>"""+str(perc31)+"""%</td>
    <td></td>
</tr>
<tr>
    <td><a href="#content32">"""+content32+"""</a></td> 
    <td>"""+result32[3]+str(result32[1])+"""/"""+str(result32[2])+"""</td>
    <td>"""+str(perc32)+"""%</td>
    <td>By default, data is encrypted using Microsoft Managed Keys for Azure Blobs, Tables, Files and Queues.</td>
</tr>
<tr>
    <td><a href="#content33">"""+content33+"""</a></td> 
    <td>"""+result33[3]+str(result33[1])+"""/"""+str(result33[2])+"""</td>
    <td>Not Scored</td>
    <td></td>
</tr>
<tr>
    <td><a href="#content34">"""+content34+"""</a></td> 
    <td>Not Scored</td>
    <td>Not Scored</td>
    <td></td>
</tr>
<tr>
    <td><a href="#content35">"""+content35+"""</a></td> 
    <td>Unavailable</td>
    <td>Unavailable</td>
    <td></td>
</tr>
<tr>
    <td><a href="#content36">"""+content36+"""</a></td> 
    <td>"""+result36[3]+str(result36[1])+"""/"""+str(result36[2])+"""</td>
    <td>"""+str(perc36)+"""%</td>
    <td>By default, data is encrypted using Microsoft Managed Keys for Azure Blobs, Tables, Files and Queues.</td>
</tr>
<tr>
    <td><a href="#content37">"""+content37+"""</a></td> 
    <td>"""+result37[3]+str(result37[1])+"""/"""+str(result37[2])+"""</td>
    <td>"""+str(perc37)+"""%</td>
    <td></td>
</tr>
"""

    print("Finished Summary3")

########################################################################################################################
############################################################ Summary 4 #################################################
########################################################################################################################
#Calculate % Passed

    if (len(result41)>1):
        print("To be done")
        score41 = 0
        summary41 = """
<tr>
    <td><b>4.1 SQL Servers</b></td> 
    <td></td>
    <td><b>"""+str(score41)+"""%</b></td> 
</tr>
"""
    else:
        score41 = 100
        summary41 = """
<tr>
    <td><b>4.1 SQL Servers</b></td> 
    <td></td>
    <td><b></b></td> 
    <td></td>
</tr>
<tr>
    <td><a href="#content411">"""+content411+"""</a></td> 
    <td>Unavailable</td>
    <td>Unavailable</td>
    <td></td>
</tr>
<tr>
    <td><a href="#content412">"""+content412+"""</a></td> 
    <td>Unavailable</td>
    <td>Unavailable</td>
    <td></td>
</tr>
<tr>
    <td><a href="#content413">"""+content413+"""</a></td> 
    <td>Unavailable</td>
    <td>Unavailable</td>
    <td></td>
</tr>
<tr>
    <td><a href="#content414">"""+content414+"""</a></td> 
    <td>Unavailable</td>
    <td>Unavailable</td>
    <td></td>
</tr>
<tr>
    <td><a href="#content415">"""+content415+"""</a></td> 
    <td>Unavailable</td>
    <td>Unavailable</td>
    <td></td>
</tr>
<tr>
    <td><a href="#content416">"""+content416+"""</a></td> 
    <td>Unavailable</td>
    <td>Unavailable</td>
    <td></td>
</tr>
<tr>
    <td><a href="#content417">"""+content417+"""</a></td> 
    <td>Unavailable</td>
    <td>Unavailable</td>
    <td></td>
</tr>
<tr>
    <td><a href="#content418">"""+content418+"""</a></td> 
    <td>Unavailable</td>
    <td>Unavailable</td>
    <td></td>
</tr>
"""

    #if (len(result42)>1):
    calc42=100*(result42[0][1]+result42[0][1]+result42[1][1]+result42[2][1]+result42[3][1]+result42[4][1]+result42[5][1]+result42[6][1]+result42[7][1])/8

    perc421=round(100*result42[0][1]/result42[0][2],2)
    perc422=round(100*result42[1][1]/result42[1][2],2)
    perc423=round(100*result42[2][1]/result42[2][2],2)
    perc424=round(100*result42[3][1]/result42[3][2],2)
    perc425=round(100*result42[4][1]/result42[4][2],2)
    perc426=round(100*result42[5][1]/result42[5][2],2)
    perc427=round(100*result42[6][1]/result42[6][2],2)
    perc428=round(100*result42[7][1]/result42[7][2],2)

    calc42=(perc421+perc422)/2
    score42 = round(calc42,2)
    score4= (score41+score42)/2
    summary42 = """
<tr>
    <td><b>4.2 SQL Databases</b></td> 
    <td></td>
    <td><b>"""+str(score4)+"""%</b></td>
    <td></td>
</tr>
<tr>
    <td><a href="#content421">"""+content421+"""</a></td> 
    <td>"""+result42[0][3]+str(result42[0][1])+"""/"""+str(result42[0][2])+"""</td>
    <td>"""+str(perc421)+"""%</td>
    <td></td>
</tr>
<tr>
    <td><a href="#content422">"""+content422+"""</a></td> 
    <td>"""+result42[1][3]+str(result42[1][1])+"""/"""+str(result42[1][2])+"""</td>
    <td>"""+str(perc422)+"""%</td>
    <td>Turn on Advanced Threat Protection for all databases on this server, at the cost of 15 USD/server/month</td>
</tr>
<tr>
    <td><a href="#content423">"""+content423+"""</a></td> 
    <td>"""+result42[2][3]+str(result42[2][1])+"""/"""+str(result42[2][2])+"""</td>
    <td>"""+str(perc423)+"""%</td>
    <td>Turn on Advanced Threat Protection for all databases on this server, at the cost of 15 USD/server/month</td>
</tr>
<tr>
    <td><a href="#content424">"""+content424+"""</a></td> 
    <td>"""+result42[3][3]+str(result42[3][1])+"""/"""+str(result42[3][2])+"""</td>
    <td>"""+str(perc424)+"""%</td>
    <td>Turn on Advanced Threat Protection for all databases on this server, at the cost of 15 USD/server/month</td>
</tr>
<tr>
    <td><a href="#content425">"""+content425+"""</a></td> 
    <td>"""+result42[4][3]+str(result42[4][1])+"""/"""+str(result42[4][2])+"""</td>
    <td>"""+str(perc425)+"""%</td>
    <td>Turn on Advanced Threat Protection for all databases on this server, at the cost of 15 USD/server/month</td>
</tr>
<tr>
    <td><a href="#content426">"""+content426+"""</a></td> 
    <td>"""+result42[5][3]+str(result42[5][1])+"""/"""+str(result42[5][2])+"""</td>
    <td>"""+str(perc426)+"""%</td>
    <td></td>
</tr>
<tr>
    <td><a href="#content427">"""+content427+"""</a></td> 
    <td>"""+result42[6][3]+str(result42[6][1])+"""/"""+str(result42[6][2])+"""</td>
    <td>"""+str(perc427)+"""%</td>
    <td></td>
</tr>
<tr>
    <td><a href="#content428">"""+content428+"""</a></td> 
    <td>"""+result42[7][3]+str(result42[7][1])+"""/"""+str(result42[7][2])+"""</td>
    <td>"""+str(perc428)+"""%</td>
    <td>Turn on Advanced Threat Protection for all databases on this server, at the cost of 15 USD/server/month</td>
</tr>
"""

    score4= (score41+score42)/2
    summary4 = """
<tr>
    <td><b>4 SQL Services</b></td> 
    <td></td>
    <td><b>"""+str(score4)+"""%</b></td> 
</tr>
"""
    summary4=summary4+summary41+summary42
    print("Finished Summary 4")

########################################################################################################################
############################################################ Summary 5 #################################################
########################################################################################################################
#Calculate % Passed, 51 and 52 ignored

    calc5=100*(result5[13][1]+result5[14][1]+result5[15][1]+result5[16][1]+result5[17][1]+result5[18][1]+result5[19][1]+result5[20][1]+result5[21][1]+result5[22][1]+result5[23][1]+result5[24][1]+result5[22][1])/13
    score5= round(calc5,2)

    summary5 = """
<tr>
    <td><b>5 Logging and Monitoring</b></td> 
    <td></td>
    <td><b>"""+str(score5)+"""%</b></td>
    <td></td>
</tr>
<tr>
    <td><a href="#content51">"""+content51+"""</a></td> 
    <td>"""+result5[13][0]+"""</td>
    <td>"""+str(100*result5[13][1])+"""%</td>
    <td></td>
</tr>
<tr>
    <td><a href="#content52">"""+content52+"""</a></td> 
    <td>"""+result5[14][0]+"""</td>
    <td>"""+str(100*result5[14][1])+"""%</td>
    <td></td>
</tr>
<tr>
    <td><a href="#content53">"""+content53+"""</a></td> 
    <td>"""+result5[15][0]+"""</td>
    <td>"""+str(100*result5[15][1])+"""%</td>
    <td></td>
</tr>
<tr>
    <td><a href="#content54">"""+content54+"""</a></td> 
    <td>"""+result5[16][0]+"""</td>
    <td>"""+str(100*result5[16][1])+"""%</td>
    <td></td>
</tr>
<tr>
    <td><a href="#content55">"""+content55+"""</a></td> 
    <td>"""+result5[17][0]+"""</td>
    <td>"""+str(100*result5[17][1])+"""%</td>
    <td></td>
</tr>
<tr>
    <td><a href="#content56">"""+content56+"""</a></td> 
    <td>"""+result5[18][0]+"""</td>
    <td>"""+str(100*result5[18][1])+"""%</td>
    <td></td>
</tr>
<tr>
    <td><a href="#content57">"""+content57+"""</a></td> 
    <td>"""+result5[19][0]+"""</td>
    <td>"""+str(100*result5[19][1])+"""%</td>
    <td></td>
</tr>
<tr>
    <td><a href="#content58">"""+content58+"""</a></td> 
    <td>"""+result5[20][0]+"""</td>
    <td>"""+str(100*result5[20][1])+"""%</td>
    <td></td>
</tr>
<tr>
    <td><a href="#content59">"""+content59+"""</a></td> 
    <td>"""+result5[21][0]+"""</td>
    <td>"""+str(100*result5[21][1])+"""%</td>
    <td></td>
</tr>
<tr>
    <td><a href="#content510">"""+content510+"""</a></td> 
    <td>"""+result5[22][0]+"""</td>
    <td>"""+str(100*result5[22][1])+"""%</td>
    <td></td>
</tr>
<tr>
    <td><a href="#content511">"""+content511+"""</a></td> 
    <td>"""+result5[23][0]+"""</td>
    <td>"""+str(100*result5[23][1])+"""%</td>
    <td></td>
</tr>
<tr>
    <td><a href="#content512">"""+content512+"""</a></td> 
    <td>"""+result5[24][0]+"""</td>
    <td>"""+str(100*result5[24][1])+"""%</td>
    <td></td>
</tr>
<tr>
    <td><a href="#content513">"""+content513+"""</a></td> 
    <td>"""+result5[25][0]+"""</td>
    <td>"""+str(100*result5[25][1])+"""%</td>
    <td></td>
</tr>
"""

    print("Finished Summary 5")

########################################################################################################################
############################################################ Summary 6 #################################################
########################################################################################################################
#Calculate % Passed, ignored 6.3


    perc61=round(100*result62[0][1]/result62[0][2],2)
    perc62=round(100*result62[1][1]/result62[1][2],2)
    perc63=round(100*result63[1]/result63[2],2)
    perc64=round(100*result64[1]/result64[2],2)
    perc65=round(100*result65[1]/result65[2],2)

    calc6=(perc61+perc62+perc63+perc64+perc65)/4
    score6= round(calc6,2)

    summary6 = """
<tr>
    <td><b>6 Networking</b></td> 
    <td></td>
    <td><b>"""+str(score6)+"""%</b></td>
    <td></td>
</tr>
<tr>
    <td><a href="#content61">"""+content61+"""</a></td> 
    <td>"""+result62[0][3]+str(result62[0][1])+"""/"""+str(result62[0][2])+"""</td>
    <td>"""+str(perc61)+"""%</td>
    <td></td>
</tr>
<tr>
    <td><a href="#content62">"""+content62+"""</a></td> 
    <td>"""+result62[1][3]+str(result62[1][1])+"""/"""+str(result62[1][2])+"""</td>
    <td>"""+str(perc62)+"""%</td>
    <td></td>
</tr>
<tr>
    <td><a href="#content63">"""+content63+"""</a></td> 
    <td>"""+result63[3]+str(result63[1])+"""/"""+str(result63[2])+"""</td>
    <td>"""+str(perc63)+"""%</td>
    <td></td>
</tr>
<tr>
    <td><a href="#content64">"""+content64+"""</a></td> 
    <td>"""+result64[3]+str(result64[1])+"""/"""+str(result64[2])+"""</td>
    <td>"""+str(perc64)+"""%</td>
    <td></td>
</tr>
<tr>
    <td><a href="#content65">"""+content65+"""</a></td> 
    <td>"""+result65[3]+str(result65[1])+"""/"""+str(result65[2])+"""</td>
    <td>"""+str(perc65)+"""%</td>
    <td></td>
</tr>
"""
    print("Finished Summary6")

########################################################################################################################
############################################################ Summary 7 #################################################
########################################################################################################################
#Calculate % Passed. 74,75 Not scored

    perc76=round(100*result7[11][0]/result7[11][1],2)
    perc73=round(100*result7[8][0]/result7[8][1],2)
    perc72=round(100*result7[7][0]/result7[7][1],2)
    perc71=round(100*result7[6][0]/result7[6][1],2)

    calc7=(perc71+perc72+perc73+perc76)/4
    score7= round(calc7,2)
    summary7 = """
<tr>
    <td><b>7 Virtual Machines</b></td> 
    <td></td>
    <td><b>"""+str(score7)+"""%</b></td>
    <td></td>
</tr>
<tr>
    <td><a href="#content71">"""+content71+"""</a></td> 
    <td>"""+result7[6][2]+str(result7[6][0])+"""/"""+str(result7[6][1])+"""</td>
    <td>"""+str(perc71)+"""%</td>
    <td></td>
</tr>
<tr>
    <td><a href="#content72">"""+content72+"""</a></td> 
    <td>"""+result7[7][2]+str(result7[7][0])+"""/"""+str(result7[7][1])+"""</td>
    <td>"""+str(perc72)+"""%</td>
    <td></td>
</tr>
<tr>
    <td><a href="#content73">"""+content73+"""</a></td> 
    <td>"""+result7[8][2]+str(result7[8][0])+"""/"""+str(result7[8][1])+"""</td>
    <td>"""+str(perc73)+"""%</td>
    <td></td>
</tr>
<tr>
    <td><a href="#content74">"""+content74+"""</a></td> 
    <td>Not Scored</td>
    <td>Not Scored</td>
    <td></td>
</tr>
<tr>
    <td><a href="#content75">"""+content75+"""</a></td> 
    <td>Not Scored</td>
    <td>Not Scored</td>
    <td></td>
</tr>
<tr>
    <td><a href="#content76">"""+content76+"""</a></td> 
    <td>"""+result7[11][2]+str(result7[11][0])+"""/"""+str(result7[11][1])+"""</td>
    <td>"""+str(perc76)+"""%</td>
    <td></td>
</tr>
"""

    print("Finished Summary 7")
########################################################################################################################
############################################################ Summary 8 #################################################
########################################################################################################################
#Calculate % Passed. 83 Not scored

    perc81=round(100*result80[0][1]/result80[0][2],2)
    perc82=round(100*result80[1][1]/result80[1][2],2)

    calc8=(perc81+perc82)/2
    score8= round(calc8,2)
    summary8 = """
<tr>
    <td><b>8 Other Security Considerations</b></td> 
    <td></td>
    <td><b>"""+str(score8)+"""%</b></td>
    <td></td>
</tr>
<tr>
    <td><a href="#content81">"""+content81+"""</a></td> 
    <td>"""+result80[0][3]+str(result80[0][1])+"""/"""+str(result80[0][2])+"""</td>
    <td>"""+str(perc81)+"""%</td>
    <td></td>
</tr>
<tr>
    <td><a href="#content82">"""+content82+"""</a></td> 
    <td>"""+result80[1][3]+str(result80[1][1])+"""/"""+str(result80[1][2])+"""</td>
    <td>"""+str(perc82)+"""%</td>
    <td></td>
</tr>
<tr>
    <td><a href="#content83">"""+content83+"""</a></td> 
    <td>Not Scored</td>
    <td>Not Scored</td>
    <td></td>
</tr>
"""

    print("Finished Summary 8")
########################################################################################################################
############################################################ Total  ####################################################
########################################################################################################################


    calcfinal=(score2+score3+score4+score5+score6+score7+score8)/7
    finalscore=round(calcfinal,2)
    total = """
<tr>
    <td><b><font color="blue">Total</font></b></td> 
    <td></td>
    <td><b><font color="blue">"""+str(finalscore)+"""%</font></b></td>
</tr>
</table> 
"""

############## detailed Results ##########
    html_content = """
<h1 id="Details">2 - Detailed</h1>
""" + content1+"</ul>"+content2+"</ul>"+content3+"</ul>"+content4+"</ul>"+content5+"</ul>"+content6+"</ul>"+content7+"</ul>"+content8

    html_summary=summary0+summary1+summary2+summary3+summary4+summary5+summary6+summary7+summary8+total
#### Create the HTML File #####
    
    filename = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    reportname=("CIS-Azure-%s-%s.html" % (name,filename))
    with open(reportname,"w") as cis_result:
        cis_result.write(html_start)
        cis_result.write(html_summary)
        cis_result.write(html_content)
        cis_result.write(html_end)
    print("Report %s was Created" % reportname)


    ################ CSV EXPORT ###################
    sep = ","
    csv_content_hdr = '"SUBSCRIPTION","CHECK","RESULT","DETAILS"\n'

    csv_content1_3  = r(c(content13)+c(result13[3]+str(result13[1])+"""/"""+str(result13[2]))+c(result13[0]))
    csv_content12_3  = r(c(content123)+c(result123[3]+str(result123[1])+"""/"""+str(result123[2]))+c(result123[0]))

    csv_content2_1  = r(c(content22)+c(result22[18][0])+c(result22[0]))   +r(c(content23)+c(result22[19][0])+c(result22[1]))
    csv_content2_2  = r(c(content24)+c(result22[20][0])+c(result22[2]))   +r(c(content25)+c(result22[21][0])+c(result22[3]))     +r(c(content26)+c(result22[22][0])+c(result22[4])) + \
                      r(c(content27)+c(result22[23][0])+c(result22[5]))   +r(c(content28)+c(result22[24][0])+c(result22[6]))
    csv_content2_3  = r(c(content29)+c(result22[25][0])+c(result22[7]))   +r(c(content210)+c(result22[26][0])+c(result22[8]))    +r(c(content211)+c(result22[27][0])+c(result22[9]))
    csv_content2_4  = r(c(content212)+c(result22[28][0])+c(result22[10])) +r(c(content213)+c(result22[29][0])+c(result22[11]))   +r(c(content214)+c(result22[30][0])+c(result22[12]))
    csv_content2_5  = r(c(content215)+c(result22[31][0])+c(result22[13])) +r(c(content216)+c(result22[32][0])+c(result22[14]))   +r(c(content217)+c(result22[33][0])+c(result22[15]))
    csv_content2_6  = r(c(content218)+c(result22[34][0])+c(result22[16])) +r(c(content219)+c(result22[35][0])+c(result22[17]))
    csv_content3_1  = r(c(content31)+c(result31[3]+str(result31[1])+"""/"""+str(result31[2]))+c(result31[0]))
    csv_content3_2  = r(c(content32)+c(result32[3]+str(result32[1])+"""/"""+str(result32[2]))+c(result32[0]))
    csv_content3_3  = r(c(content33)+c(result33[3]+str(result33[1])+"""/"""+str(result33[2]))+c(result33[0]))
    csv_content3_4  = r(c(content34)+c("")+c(result34))                   +r(c(content35)+c("")+c(result35))                     +r(c(content36)+c(result36[3]+str(result36[1])+"""/"""+str(result36[2]))+c(result36[0])) + \
                      r(c(content37)+c(result37[3]+str(result37[1])+"""/"""+str(result37[2]))+c(result37[0]))
    csv_content41_1 = r(c(content411))
    csv_content41_2 = r(c(content414))
    csv_content42_1 = r(c(content421)+c(result42[0][3]+str(result42[0][1])+"""/"""+str(result42[0][2]))+c(result42[0][0]))       +r(c(content422)+c(result42[1][3]+str(result42[1][1])+"""/"""+str(result42[1][2]))+c(result42[1][0])) + \
                      r(c(content423)+c(result42[2][3]+str(result42[2][1])+"""/"""+str(result42[2][2]))+c(result42[2][0]))
    csv_content42_2 = r(c(content424)+c(result42[3][3]+str(result42[3][1])+"""/"""+str(result42[3][2]))+c(result42[3][0]))       +r(c(content425)+c(result42[4][3]+str(result42[4][1])+"""/"""+str(result42[4][2]))+c(result42[4][0])) + \
                      r(c(content426)+c(result42[5][3]+str(result42[5][1])+"""/"""+str(result42[5][2]))+c(result42[5][0]))
    csv_content42_3 = r(c(content427)+c(result42[6][3]+str(result42[6][1])+"""/"""+str(result42[6][2]))+c(result42[6][0]))       +r(c(content428)+c(result42[7][3]+str(result42[7][1])+"""/"""+str(result42[7][2]))+c(result42[7][0]))
    csv_content5_1  = r(c(content51)+c(result5[13][0])+c(result5[0]))     +r(c(content52)+c(result5[14][0])+c(result5[1]))       +r(c(content53)+c(result5[15][0])+c(result5[2]))
    csv_content5_2  = r(c(content54)+c(result5[16][0])+c(result5[3]))     +r(c(content55)+c(result5[17][0])+c(result5[4]))       +r(c(content56)+c(result5[18][0])+c(result5[5]))       +r(c(content57)+c(result5[19][0])+c(result5[6])) + \
                      r(c(content58)+c(result5[20][0])+c(result5[7]))
    csv_content5_3  = r(c(content59)+c(result5[21][0])+c(result5[8]))     +r(c(content510)+c(result5[22][0])+c(result5[9]))      +r(c(content511)+c(result5[23][0])+c(result5[10]))
    csv_content5_4  = r(c(content512)+c(result5[24][0])+c(result5[11]))   +r(c(content513)+c(result5[25][0])+c(result5[12]))
    csv_content6_1  = r(c(content61)+c(result62[0][3]+str(result62[0][1])+"""/"""+str(result62[0][2]))+c(result62[0][0]))        +r(c(content62)+c(result62[1][3]+str(result62[1][1])+"""/"""+str(result62[1][2]))+c(result62[1][0])) + \
                      r(c(content63)+c("")+c(result63[0]))
    csv_content6_2  = r(c(content64)+c(result64[3]+str(result64[1])+"""/"""+str(result64[2]))+c(result64[0]))
    csv_content6_3  = r(c(content65)+c(result65[3]+str(result65[1])+"""/"""+str(result65[2]))+c(result65[0]))
    csv_content7_1  = r(c(content71)+c(result7[6][2]+str(result7[6][0])+"""/"""+str(result7[6][1]))+c(result7[0]))               +r(c(content72)+c(result7[7][2]+str(result7[7][0])+"""/"""+str(result7[7][1]))+c(result7[1])) + \
                      r(c(content73)+c(result7[8][2]+str(result7[8][0])+"""/"""+str(result7[8][1]))+c(result7[2]))
    csv_content7_2  = r(c(content74)+c("")+c(result7[3]))                 +r(c(content75)+c("")+c(result7[4]))                   +r(c(content76)+c(result7[11][2]+str(result7[11][0])+"""/"""+str(result7[11][1]))+c(result7[5]))

    csv_content41   = csv_content41_1 + csv_content41_2
    csv_content42   = csv_content42_1 + csv_content42_2 + csv_content42_3
    csv_content50   = csv_content5_1  + csv_content5_2  + csv_content5_3  + csv_content5_4

    csv_content1 = csv_content1_3 + csv_content12_3
    csv_content2 = csv_content2_1 + csv_content2_2 + csv_content2_3 + csv_content2_4 + csv_content2_5 + csv_content2_6
    csv_content3 = csv_content3_1 + csv_content3_2 + csv_content3_3 + csv_content3_4
    csv_content4 = csv_content41  + csv_content42
    csv_content5 = csv_content50
    csv_content6 = csv_content6_1 + csv_content6_2 + csv_content6_3
    csv_content7 = csv_content7_1 + csv_content7_2
    csv_content8 = r(c(content81)+c(result80[0][3]+str(result80[0][1])+"""/"""+str(result80[0][2]))+c(result80[0][0])) + r(c(content82)+c(result80[1][3]+str(result80[1][1])+"""/"""+str(result80[1][2]))+c(result80[1][0])) + \
                   r(c(content83)+c("")+c(result83))

    reportname=("CIS-Azure-%s-%s.csv" % (name,filename))
    with open(reportname,"w") as cis_result:
        cis_result.write(csv_content_hdr)
        cis_result.write(strip_tags(csv_content1))
        cis_result.write(strip_tags(csv_content2))
        cis_result.write(strip_tags(csv_content3))
        cis_result.write(strip_tags(csv_content4))
        cis_result.write(strip_tags(csv_content5))
        cis_result.write(strip_tags(csv_content6))
        cis_result.write(strip_tags(csv_content7))
        cis_result.write(strip_tags(csv_content8))
    print("Report %s was Created" % reportname)


print("Azure CIS Checks")

try:
    subs=subscription.sub()
    menu_item = 0
    namelist = []
    available_subscriptions=[]

    menu_item=True
    while menu_item:
        print("--------------------")
        for i in range(0,len(subs[0])):
            print("%d. %s" % (i,subs[2][i]))
        print("A. All Subscriptions")
        print("Q. Quit")
        menu_item = input("Select a subscription from the menu: ")
        if menu_item=="Q":
            print("Q")
            break
        elif menu_item=="A":
            print("A")
            for j in range(0,len(subs[0])):
                print("Starting CIS Benchmark for: %s" % subs[2][j])
                os.popen('az account set --subscription "%s"' % subs[2][j])
                generate_report(subs[0][j],subs[2][j],subs[1][j])
            break
        elif (menu_item.isdigit() and int(menu_item) in range(0,len(subs[0]))):
            print("Starting CIS Benchmark for: %s" % subs[2][int(menu_item)])
            os.popen('az account set --subscription "%s"' % subs[2][int(menu_item)])
            generate_report(subs[0][int(menu_item)],subs[2][int(menu_item)],subs[1][int(menu_item)])
        else:
            print("\n Not Valid Choice Try again") 

    print("\nDone\n")
except Exception as e:
    print("Exception in main: %s %s" % (type(e), str(e.args)))
    # except:
    # print("Not Connected to Azure. Run 'az login' command first and relaunch the program")
    sys.exit(0)

