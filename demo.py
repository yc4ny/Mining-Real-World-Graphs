import argparse 
import os
import subprocess

def getGraphName(path):
    input_dir = args.input 
    file_path = input_dir.split('/')
    filename = file_path[len(file_path)-1]
    filename = filename.replace('.csv', '')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = "Age Classification")
    parser.add_argument('--input', type = str, default = 'datasets/facebook_clean_data/artist_edges.csv', help = 'output from community detection')
    args = parser.parse_args()
    
    filename = getGraphName(args.input)

    print(filename)
    # subprocess.run(["ls", "-l"])
