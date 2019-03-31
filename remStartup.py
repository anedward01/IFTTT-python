# NOTE: This script deletes files that are found in home folder
# to prevent event loops and potentially cause a system to become
# unmanageable. It is recommended to not remove this file from the
# code.

import configparser
from datetime import datetime
import os
from shutil import copyfile

def rem():
    
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

    # Checks for potential files that can cause loops at start.
    var1 = 0
    for i in range(cmdAmt):
        cmdNum = str(i)
        f = config.get('FILES', cmdNum)
        append = config.get('MISC', 'FILE_APPEND')
        path = (sysPath + f.lower() + append)
        if os.path.exists(path):
            var1 = 1

            writeLog(datetime.now().isoformat(' ', 'seconds')
            + ': Startup - '
            + f
            + ' file found.\n')

            os.remove(path)
            writeLog(datetime.now().isoformat(' ', 'seconds')
            + ': Startup - '
            + f 
            + ' file deleted.\n')
            
            saveLoc.flush()
            try:
                for i in range(100):
                    num = str(i)
                    copyfile('Log.txt',config.get('MISC','LOG_BACKUP_'
                    + num))
            except:
                pass

        else:
            continue
    # This is for when no files are found at startup.
    if var1 == 0:
        writeLog(datetime.now().isoformat(' ', 'seconds')
        + ': Startup - No potential loop files declared found.\n')
        saveLoc.flush()
        try:
            for i in range(100):
                num = str(i)
                copyfile('Log.txt',config.get('MISC','LOG_BACKUP_'
                + num))
        except:
            pass
    
    # This is for when all files listed in files.ini are found
    if var1 == 1:
        writeLog(datetime.now().isoformat(' ', 'seconds')
        + ': Startup - All potential loop files declared are deleted.\n')
        saveLoc.flush()
        try:
            for i in range(100):
                num = str(i)
                copyfile('Log.txt',config.get('MISC','LOG_BACKUP_'
                + num))
        except:
            pass

    


