#File name: backup_v1.py
#This script is used to backup the important files

import os
import time

#1. The files and directories to be backed up are specified in a list:
source = ['/Users/david/Documents/workspace/Python']

#2. The backup must be stored in a main backup directory
target_dir = '/Users/david/Documents/workspace/'

#3. The files are backed up into a zip file.
#4. The name of the zip archive is the current date and time
target = target_dir + 'py_source_' + time.strftime('%Y%m%d%H%M%S') + '.zip'

#5. We use the zip command(in Unix/Linux) to put the files in a zip archive
zip_command = "zip -qr '%s' %s" % (target, ' '.join(source))

#Run the backup
if os.system(zip_command) == 0:
    print 'Successfully backup to',target
else:
    print 'Backup failed'

