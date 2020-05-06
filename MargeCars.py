import time

ara = (u'في حال واجهتك مشكلة راسلني على الخاص')
ara2 = (u'تم الانتهاء من ضغط السيارات بنجاح')

print(f"By ! TankOsama#1792\n {ara}")


print('Whit 5 Sec...')
time.sleep(2.5)


print('Program is run')

import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()
Old_filepath = filedialog.askdirectory()

New_filePath = filedialog.askdirectory()

import os

arr = os.listdir(rf"{Old_filepath}")
d = 0
#print(arr)
#for i in arr:
 #   d = d +1
  #  b = str(d)
   # os.rename(rf"C:\Users\iosam\Desktop\كل ما يتعلف بفايف ام\marrigecars\TankFBI{i}",rf'C:\Users\iosam\Desktop\كل ما يتعلف بفايف ام\marrigecars\TankFBI\TankCars{i}'+b)
fd = (fr"{New_filePath}\__resource.lua")
old = []
for j in arr:
    d = d +1
    b = str(d)
    arry=(os.listdir(rf"{Old_filepath}\{j}"))
    for i in arry:
        if i == 'stream' or i == '__resource.lua' or i == 'Stream':
            continue
        os.rename(rf"{Old_filepath}\{j}\{i}",rf'{New_filePath}\{b}{i}')
        arryd =(os.listdir(rf"{Old_filepath}\{j}\stream"))
        for z in arryd:
            try:

                os.rename(rf"{Old_filepath}\{j}\stream\{z}",rf'{New_filePath}\stream\{z}')
                print(f'suuccfule{z}')
            except:
                print(f"Error{j,z}")



f = open(rf"{New_filePath}\__resource.lua", "a")
ttd = 0
f.write("""resource_manifest_version '77731fab-63ca-442c-a67b-abc70f28dfa5'\n\n\n\n""")
f.write("files {")
for r in arr:
    ttd = ttd +1
    tt = str(ttd)
    f.write(f"""\n    '{tt}vehicles.meta',\n    '{tt}carvariations.meta',\n    '{tt}carcols.meta',\n    '{tt}handling.meta',""")
   # f.write(f"""'{tt}vehicles.meta',\n'{tt}carvariations.meta',\n'{tt}carcols.meta',\n'{tt}handling.meta' \n\n\n\n data_file 'HANDLING_FILE' '{tt}handling.meta' \n
#data_file 'VEHICLE_METADATA_FILE''{tt}vehicles.meta'\ndata_file 'CARCOLS_FILE' '{tt}carcols.meta'  \ndata_file 'VEHICLE_VARIATION_FILE' '{tt}carvariations.meta'  """)
f.write("\n}")
tred = 0
for q in arr:
    tred = tred +1
    tre = str(tred)
    f.write(f"""\n\n\ndata_file 'HANDLING_FILE' '{tre}handling.meta' \ndata_file 'VEHICLE_METADATA_FILE''{tre}vehicles.meta'\ndata_file 'CARCOLS_FILE' '{tre}carcols.meta'  \ndata_file 'VEHICLE_VARIATION_FILE' '{tre}carvariations.meta'\n\n\n""")
f.close()


print(f'----------{ara2}----------')

