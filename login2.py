#!/bin/env python
import pexpect
import sys
import time
import csv

username = raw_input("User: ")
adduser = "set account name " + username



f = open('ips')
for line in f:
        string = line.replace("\n","")

        if len(username) > 0:
               #login
                option_ssh = "-o \"ConnectTimeout=3\" -o \"StrictHostKeyChecking no\" "
                p = pexpect.spawn('ssh ' + option_ssh + string.split()[1] + string.split()[2])
                p.logfile = open("mylog", "a")
                i = p.expect([pexpect.EOF, '[Pp]assword: '])
                if i == 0:
                        print 'No SSH connection for or invalid IP : %s(%s - %s)' % (string.split()[0],string.split()[2],string.split()[4])

                if i == 1:

                        p.sendline (string.split()[3])
                        
                        t = p.expect(['Permission denied, please try again.', 'admin:']) 
                        if t == 0:
                                print 'Wrong password for host: %s(%s - %s)' % (string.split()[0],string.split()[2],string.split()[4])
                                #sys.exit (1)
                        if t == 1:

                                p.sendline(adduser)

                                k = p.expect(['Account name already exists', 'Please enter the privilege level :'])

                                if k == 0:
                                        print 'User %s already exists: %s(%s - %s)' % (username,string.split()[0],string.split()[2],string.split()[4])

                                if k == 1:
                                        p.sendline('1')
                                        p.expect ('Please enter the password :')

                                        p.sendline(password)
                                        p.expect ('re-enter to confirm :')

                                        p.sendline(password)
                                        p.expect ('admin:')

                                        time.sleep(5)
                                        p.sendline('exit')
                       
                                        print "Username %s was successfuly create:  %s(%s - %s)"   % (username,string.split()[0],string.split()[2],string.split()[4])


        else:

                print "Your input is empty...TRY AGAIN"

f.close()
