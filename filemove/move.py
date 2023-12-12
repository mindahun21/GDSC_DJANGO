import os
from datetime import datetime, timedelta
import shutil

current_dir=os.getcwd()
print(os.listdir(current_dir))


current_time=datetime.now()
treshold_time=current_time-timedelta(hours=24)
last24hours_path=os.path.join(current_dir, 'last24_hours')


os.makedirs(last24hours_path,exist_ok=True)


for file in os.listdir(current_dir):

    file_path=os.path.join(current_dir,file)

    if file=="move.py":
        continue
    
    file_stat=os.stat(file_path)
    file_mtime=datetime.fromtimestamp(file_stat.st_mtime)
    file_ctime=datetime.fromtimestamp(file_stat.st_ctime)

    if os.path.isfile(file_path) and (file_mtime>treshold_time or file_ctime>treshold_time):
        shutil.move(file_path,last24hours_path)






