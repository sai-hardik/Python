####################################
#code 1:
import os
path="C:\Users\babut\OneDrive\Desktop\sample.txt"
f="sample.txt"
if os.path.isfile(path):
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
