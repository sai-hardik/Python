f="sample.txt"
try:
    open(f,"a")
except Exception as error:
    print("Permissions denied")
    
else: 
    f.write("world")
    f.close()
