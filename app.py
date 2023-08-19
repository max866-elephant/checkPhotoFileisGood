# -*- coding: utf-8 -*- 
import os
from PIL import Image
import time
from datetime import datetime
import glob

start_time = time.time()

def main():
    i = 0
    checklists = [r"G:\\Camera Uploads\\*.*"]

    for dirPathPattern in checklists:
        result = glob.glob(dirPathPattern)
        for file_name in result:
            try:
                img = Image.open(file_name)
                #print(file_name+' -- ok')

            except:
                print(file_name+' -- NG')
                # os.remove(file_name)
                filters = ['jpg', 'png']
                if str(file_name)[-3:].lower() in filters: 
                    print(file_name+' -- '+str(file_name)[-3:])
                    with open   ('.\\lists_NG_Files.txt', 'a', encoding='utf-8', newline='') as w:
                        w.write(str(file_name)+'\n')
            i = i+1
    print('總共檢查照片張數:'+str(i))



if __name__ == '__main__':
    main()
    print('------------')
    print(datetime.now())
    print('run time : ')
    print(time.time()-start_time)