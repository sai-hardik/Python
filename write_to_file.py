####################################
#code 1:
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
        
#####################################
#code 2:
f="sample.txt"
try:
        open(f,"a")
    except FileNotFoundError:
        print("File not found")
    except Exception as error:
        print("Permissions denied")

    else: 
        f.write("world")
        f.close()
