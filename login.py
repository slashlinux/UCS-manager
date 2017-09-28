#!/bin/env python
import pexpect

username = raw_input("User: ")
password = "tgztgztgz"
adduser = "useradd " + username
change_password = "passwd " + username
check = 'cat /etc/group | grep %s' % username
priv_root = 'sudo su'
t = 250


f = open('ips')
for line in f:
    if t > 10:

        #login
        login = "ssh vagrant@"+line
        child = pexpect.spawn (login)
        child.expect ('.*password:')
        child.sendline ('vagrant')
        child.expect ('.*64:')


        #root login
        child.sendline (priv_root)
        child.expect ('vagrant#')


        #adding user
        child.sendline(adduser)
        child.expect ('vagrant#')

        #create password
        child.sendline (change_password)
        child.expect ('password:')
        child.sendline (password)
        child.expect ('password:')
        child.sendline (password)
        child.expect ('vagrant#')
	print "Username %s was successfuly create in %s"   % (username,line)  


    else:
        print "bad luck"
f.close()

