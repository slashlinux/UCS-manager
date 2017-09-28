#!/bin/env python
import pexpect

username = "peter"
password = "tgztgztgz"
adduser = "useradd " + username
change_password = "passwd " + username 
check = 'cat /etc/group | grep %s' % username
priv_root = 'sudo su'

#login
child = pexpect.spawn ('ssh vagrant@10.152.77.138')
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



#listing 
child.sendline (check)
child.expect ('vagrant#')

print child.check


#print child.before

#print "Successfully test user create"
print test
