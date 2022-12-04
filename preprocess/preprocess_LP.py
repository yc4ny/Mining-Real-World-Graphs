import json 
import csv
from tqdm import tqdm
import argparse
import time 

parser = argparse.ArgumentParser(description = "Preprocess ArgsParser")
parser.add_argument('--input', type = str, default = 'output/sample_data.json', help = 'output from community detection')
parser.add_argument('--original_edges', type = str, default = 'data/custom/sample_data.csv', help = 'original input with all edges')
parser.add_argument('--output', type = str, default = 'data/processed_communityDetection/processed_sample_data.txt', help = 'processed data, ready for KL algorithm')
args = parser.parse_args()

# function to return key for any value
def get_key(dic, val):
    for key, value in dic.items():
        if val in value:
            return key
 
    return "key doesn't exist"

# Load Community Detection Output
with open(args.input, 'r') as f:   
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
with open(args.original_edges) as fp:
    reader = csv.reader(fp, delimiter=",", quotechar='"')
    data_read = [row for row in reader]

# Create clustered graph into a txt file
string = ""
key_list = list(temp.keys())
val_list = list(temp.values())
for i in tqdm(range(len(data_read))):
    val_1 = data_read[i][0]
    val_2 = data_read[i][1]
    a = get_key(temp, val_1)
    b = get_key(temp, val_2)
    if a == b:
        continue
    string += (str(a) + "," + str(b) + "\n")

# Save File 
with open(args.output, "w") as text_file:
    text_file.write(string)

