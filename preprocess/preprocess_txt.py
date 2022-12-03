import pandas as pd
f = open('data/sample_data.txt')
new = ""
track = 0

while 1:
    line = f.readline()
    if not line:
        break 
    a,b = line.split()
    new = new + a + "," + b + "\n"
    track = track + 1
    print(track)

#open text file
text_file = open("data/sample_data.txt", "w")

#write string to file
text_file.write(new)

#close file
text_file.close()

