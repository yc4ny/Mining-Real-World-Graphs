import json 
import csv

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
    # next(reader, None)  # skip the headers
    data_read = [row for row in reader]

print(temp)