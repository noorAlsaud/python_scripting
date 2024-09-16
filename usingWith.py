# syntax that open the file and automatically close it: 
# WITH 

with open('sometext.txt', 'r') as f : 
    file_data = f.read() # reading the whole file

    print(file_data)