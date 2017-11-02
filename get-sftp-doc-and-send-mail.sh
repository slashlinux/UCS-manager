#!/bin/bash

#Variables 
SFTPHOSTNAME="192.168.1.1"
SFTPUSERNAME="user"
SFTPPASSWORD="password"
FOLDER="/home/$USER/sftp"
#SFTP CONNECTION
output=$(sshpass -p $SFTPPASSWORD sftp $SFTPUSERNAME@$SFTPHOSTNAME << !
    cd $FOLDER
    get index.txt
 exit
!);


#!/bin/bash
if egrep ":" index.txt ; then

          cat index.txt | egrep ":|style|table|Device"  | mailx -s "$(echo -e "BGP Session Uptime \nContent-Type: text/html")" -r from_monitoring@yahoo.com to_user@domain.com
else
        exit 0
fi
