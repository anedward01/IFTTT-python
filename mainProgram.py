# IFTTT: Allows Google Home integration with a computer
# Copyright (C) 2019  Anguianoewi

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>

import os
import datetime
import sys
import os.path
import time
import subprocess
from shutil import copyfile
import configparser
import remStartup as rem
import runCommand as run

# Sets up settings reader
config = configparser.ConfigParser()
config.read('files.ini')

# Sets up save interval
saveMarker = 0
saveInt = int(config.get('MISC','SAVE_INTERVAL'))
runInt = int(config.get('MISC','SLEEP_TIME'))
licRead = int(config.get('MISC', "LICENSE_READ"))

if licRead == 0:
    print('IFTTT: Allows Google Home integration with a computer'
    'Copyright (C) 2019  Anguianoewi\n\n'
    'You should have received a copy of the GNU General Public License\n'
    'along with this program.  If not, see <http://www.gnu.org/licenses/>\n\n'
    'To get rid of this notification, modify files.ini [MISC] LICENSE_READ to 1\n')

else:
    None

# Sets up save location
saveLoc = open('Log.txt', 'a+')
writeLog = saveLoc.write

# Writes separator and pushes text into file
writeLog('\n------------------------------------------------------------\n')
writeLog(datetime.datetime.now().isoformat(' ','seconds') + ': Log start date\n')
saveLoc.flush()

# Try creating backups, if specified.
try:
    for i in range(100):
        num = str(i)
        copyfile('Log.txt',config.get('MISC','LOG_BACKUP_'
        + num))

# If error; ignore()
except:
    pass

# Startup script runs
rem.rem()

# Infinite loop to keep system up and running
while True:

    # Starts time interval between run check
    time.sleep(runInt)

    # Increases save token
    saveMarker + 1
    
    # Run commands script
    run.run()

    # checks to see if save token is equal to save integer
    if saveMarker == saveInt:

        #resets save token
        saveMarker = 0

        try:
            for i in range(100):
                num = str(i)
                copyfile('Log.txt',config.get('MISC','LOG_BACKUP_'
                + num))
        except:
            pass
