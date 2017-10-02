#!/bin/env python
import pexpect

username = raw_input("User: ")
password = "passw"
adduser = "set account name " + username
t = 250


f = open('ips')
for line in f:
    if t > 10:

        #login
        login = "ssh -o \"StrictHostKeyChecking no\" admin@"+line
        child = pexpect.spawn (login)
        child.expect ('.*password:')
        child.sendline ('pass')
        child.expect ('admin:')


        #adding user
        child.sendline(adduser)
        child.expect ('Please enter the privilege level :')
        child.sendline('1')
                
        child.expect ('Please enter the password :')
        child.sendline(password)    
        child.expect ('re-enter to confirm :')

        child.sendline(password)
        child.expect ('admin:')

        child.sendline('exit')

        print "Username %s was successfuly create in %s"   % (username,line)


    else:
        print "bad luck"
f.close()
