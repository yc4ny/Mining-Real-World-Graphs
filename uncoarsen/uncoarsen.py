import json
import argparse

# function to return key for any value
def get_key(dic, val):
    for key, value in dic.items():
        if val in value:
            return key
 
    return "None"

if __name__ == "__main__":
    # Parse command line arguments  
    parser = argparse.ArgumentParser(description = "Uncoarsen ArgParser")
    parser.add_argument('--LP', type = str, default = 'outputs/output_LP/artist.json', help = 'output from community detection')
    parser.add_argument('--KL', type = str, default = 'outputs/output_KL/partitioned_artist.txt', help = 'output from partitioning')
    parser.add_argument('--output', type = str, default = 'outputs/output_uncoarsened/uncoarsened_artist.json', help = 'output from uncoarsening')

    args = parser.parse_args()

    # Read in LP output
    with open(args.LP, 'r') as f:   
        # Key: Node #
        # Value: Community #
        json_data = json.load(f)

    # Read in KL output
    f = open(args.KL)
    content = f.read()
    f.close()

    # Track of which communities are in which partition
    track = {}
    partitioned = content.split("\n")
    for i in range(len(partitioned)-1): 
        community, group = partitioned[i].split(", ")
        if group in track.keys():
            track[group].append(community)
        else:
            track[group] = [community]

    # Uncoarsen with the given information
    for key, value in json_data.items():
        which = get_key(track, str(value))
        track[which].append(str(key))

    # Save final partitioned output 
    with open(args.output, 'w') as fp:
        json.dump(track, fp)