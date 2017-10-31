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


if egrep ":|style|table|Device" index.txt > send_mail.html; then

        mailx -s "$(echo -e "BGP Network Issues\nContent-Type: text/html")" -r from_user@mail.com to_user@mail.com < send_mail.html
else
        exit 0
fi
