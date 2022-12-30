f="sample.txt"
try:
    open(f)
except Exception as error:
    print("Permissions denied")
    
f.write("world")
f.close()