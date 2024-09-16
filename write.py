f = open("someText.txt", 'w') #     'w' mode --> writing & 'r' mode --> reading
try: 
    f.write("I am writing in the file")
    print("done!!")
except: 
    print("Could not write in the file")
f.close()
