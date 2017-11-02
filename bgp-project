#!/bin/env python
import re
import csv
from datetime import datetime
import pexpect
import sys
import time


#Variabile
ip_nexus = '192.168.1.1'
n1kswi01 = "N7K-01"


if len(ip_nexus) > 0:
               #login
                login = "ssh -o \"StrictHostKeyChecking no\" checks@"+ip_nexus
                child = pexpect.spawn (login)
                child.logfile = open("n1k01_"+datetime.now().strftime("%Y-%m-%d"), "w")
                i = child.expect([pexpect.TIMEOUT, '[Pp]assword: '])
                if i == 0:
                        print 'No SSH connection for %s or invalid IP' % (ip_nexus)

                if i == 1:
                        child.sendline ('password')
                        child.expect ('.*#')


                #commands
                        child.sendline('term len 0')
                        child.expect ('.*#')



                        child.sendline('sh bgp sessions vrf all')
                        child.expect ('.*#')
                        time.sleep(5)


                        time.sleep(5)
                        child.sendline('exit')


else:

                print "Your input is empty...TRY AGAIN"




otr="<tr>"
ctr="</tr>"
otd="<td align = \"center\">"
ctd="</td>"
tblo= "<table>"
tblc= "</table>"
otrbg = "<tr bgcolor=Gray>"
otd_red = "<td align = \"center\" bgcolor=Red>"
otd_green = "<td align = \"center\" bgcolor=Lime>"



print tblo

print otrbg+otd+"Device Name"+ctd,
print otd+"Neighbor"+ctd,
print otd+"ASN"+ctd,
print otd+"Flaps"+ctd,
print otd+"BGP Session uptime"+ctd+ctr

var = "\d[0-9]{1,2}:\d[0-9]{1,2}:\d[0-9]{1,2}"

file = open("n1k01_"+datetime.now().strftime("%Y-%m-%d"))
for line in file:
        string = line.replace("\n","")
        if (re.match('[\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}]|VRF',string)):
                bgp_session = string.replace("|", " ").replace(",","")

                print otr+otd+n1kswi01+ctd,
                print otd+bgp_session.split()[0]+ctd,
                print otd+bgp_session.split()[1]+ctd,
                print otd+bgp_session.split()[2]+ctd,
                if (re.match('[0-9]{1,2}:\d[0-9]{1,2}:\d[0-9]{1,2}',bgp_session.split()[3])):
                        print ("%s") % (otd_red+bgp_session.split()[3]+ctd+ctr)
                else:
                        print ("%s") % (otd_green+bgp_session.split()[3]+ctd+ctr)

print tblc
