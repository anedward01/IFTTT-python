# Hash Generator - Creates a hash using multiple methods
# Copyright (C) 2019  Anguianoewi

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>

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
    # configRaw gets amount in group
    config = configparser.ConfigParser()
    configRaw = configparser.RawConfigParser()

    # Read them files
    config.read('files.ini')
    configRaw.read('files.ini')
    
    # Gets defines system path for command files
    sysPath = config.get('MISC', 'FILES_LOCATION')

    #defines save location
    saveLoc = open('Log.txt', 'a+')
    writeLog = saveLoc.write

    # Gets commands and then is converted into command amounts
    items = configRaw.items('FILES')
    cmdAmt = len(items)


    var1 = 0

    # Checks for potential files that can cause loops at start.
    for i in range(cmdAmt):

        # assigns variable with string of a number to check for number
        cmdNum = str(i)
        f = config.get('FILES', cmdNum)

        # Adds file append in case append varies
        append = config.get('MISC', 'FILE_APPEND')

        # Assigns file path by mixing a very lovely cocktail of abomination
        path = (sysPath + f.lower() + append)

        # Checks to see if file exists
        if os.path.exists(path):
            var1 = 1

            # Declares file found in log
            writeLog(datetime.now().isoformat(' ', 'seconds')
            + ': Startup - '
            + f
            + ' file found.\n')

            # Deletes file
            os.remove(path)

            # Declares file deleted in log
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

    


