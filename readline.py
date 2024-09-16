camelot_lines = []
with open("camelot.txt", 'r') as f: 
    for line in f: 
        camelot_lines.append(line.strip()) # strip() : remove leading and trailing whitespace
print(camelot_lines)