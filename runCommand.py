import os
import sys
from datetime import datetime
import os.path
import time
import subprocess
from shutil import copyfile
import configparser

def run():
    # config gets information from file,
    # configRaw get amount from group
    config = configparser.ConfigParser()
    configRaw = configparser.RawConfigParser()

    # Read them files
    config.read('files.ini')
    configRaw.read('files.ini')
    
    # Gets defines system path for command files
    sysPath = config.get('MISC', 'FILES_LOCATION')

    saveLoc = open('Log.txt', 'a+')
    writeLog = saveLoc.write

    # Gets commands and then is converted into command amounts
    items = configRaw.items('FILES')
    cmdAmt = len(items)

    # Similar to remStartup, this command will check for command
    # files and launch those commands.
    for i in range(cmdAmt):

        cmdNum = str(i)
        f = config.get('FILES', cmdNum)
        cmd = config.get('COMMANDS', cmdNum)
        append = config.get('MISC', 'FILE_APPEND')
        path = (sysPath + f.lower() + append)
        if os.path.exists(path):
            var1 = 1

            # Declare file was found
            writeLog(datetime.now().isoformat(' ', 'seconds')
            + ': Run - '
            + f
            + ' file found.\n')
            
            # Hopefully run the command successfully
            subprocess.run(cmd, shell=False)
            writeLog(datetime.now().isoformat(' ', 'seconds')
            + ': Run - '
            + f 
            + ' command executed.\n')

            #Delete trigger file
            os.remove(path)
            writeLog(datetime.now().isoformat(' ', 'seconds')
            + ': Run - '
            + f 
            + ' file deleted.\n')
            
            #Hopefully save log
            saveLoc.flush()

            # Save log to backup locations. Stops when error occurs,
            # then continues as normal
            try:
                for i in range(100):
                    num = str(i)
                    copyfile('Log.txt',config.get('MISC','LOG_BACKUP_'
                    + num))
            except:
                pass