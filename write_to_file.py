import os

f="sample.txt"
if os.path.isfile(f):
    try:
        open(f,"a")
    except Exception as error:
        print("Permissions denied")

    else: 
        f.write("world")
        f.close()
