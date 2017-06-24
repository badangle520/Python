#File name: backup_v3.py
#This script is used to backup the important files

import os
import time

#1. The files and directories to be backed up are specified in a list:
source = ['/Users/david/Documents/workspace/Python']

#2. The backup must be stored in a main backup directory
target_dir = '/Users/david/Documents/workspace/'

#3. The files are backed up into a zip file.
#4. The current day is the name of the sub directory in the main directory
today = target_dir + time.strftime('%Y%m%d')

# The current time is the name of the zip archive
now = time.strftime('%H%M%S')

# Take a comment from the user to create the name of the zip file 
comment = raw_input('Enter a comment --> ')
if len(comment) == 0: 
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' + comment.replace(' ', '_') + '.zip'

# Create the subdirectory if it isn't already there 
if not os.path.exists(today):
    os.mkdir(today)
    print 'Successfully created directory', today


#5. We use the zip command(in Unix/Linux) to put the files in a zip archive
zip_command = "zip -qr '%s' %s" % (target, ' '.join(source))

#Run the backup
if os.system(zip_command) == 0:
    print 'Successfully backup to',target
else:
    print 'Backup failed'

