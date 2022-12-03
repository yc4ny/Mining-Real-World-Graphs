import json 
import csv
import tqdm as tqdm 

# function to return key for any value
def get_key(dic, val):
    for key, value in dic.items():
        if val in value:
            return key
 
    return "key doesn't exist"

# Load Community Detection Output
with open('output/sample_data.json', 'r') as f:   
    # Key: Node #
    # Value: Community #
    json_data = json.load(f)

# Create a dictionary for storing communities
temp = {}
for key, value in json_data.items():
    if value in temp.keys():
        temp[value].append(key)
    else:
        temp[value] = [key]

# Read input CSV file (original graph connections)
with open("data/custom/sample_data.csv") as fp:
    reader = csv.reader(fp, delimiter=",", quotechar='"')
    data_read = [row for row in reader]

# Create clustered graph into a txt file
string = ""
key_list = list(temp.keys())
val_list = list(temp.values())
for connections in data_read:
    val_1 = connections[0]
    val_2 = connections[1]
    a = get_key(temp, val_1)
    b = get_key(temp, val_2)
    string += (str(a) + "," + str(b) + "\n")

# Save File 
with open("data/processed_communityDetection/processed_sample_data.txt", "w") as text_file:
    text_file.write(string)
