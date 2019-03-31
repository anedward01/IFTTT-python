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

config = configparser.ConfigParser()
config.read('files.ini')

saveMarker = 0
saveInt = int(config.get('MISC','SAVE_INTERVAL'))
runInt = int(config.get('MISC','SLEEP_TIME'))
saveLoc = open('Log.txt', 'a+')
writeLog = saveLoc.write

writeLog('\n------------------------------------------------------------\n')
writeLog(datetime.datetime.now().isoformat(' ','seconds') + ': Log start date\n')
saveLoc.flush()
try:
    for i in range(100):
        num = str(i)
        copyfile('Log.txt',config.get('MISC','LOG_BACKUP_'
        + num))
except:
    pass


rem.rem()

while True:
    time.sleep(runInt)
    saveMarker + 1
    run.run()
    if saveMarker == saveInt:
        saveMarker = 0
        try:
            for i in range(100):
                num = str(i)
                copyfile('Log.txt',config.get('MISC','LOG_BACKUP_'
                + num))
        except:
            pass
