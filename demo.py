import argparse 
import os
import subprocess

def getGraphName(input_directory):
    input_dir = args.input 
    file_path = input_dir.split('/')
    filename = file_path[len(file_path)-1]
    filename = filename.replace('.csv', '')
    return filename

if __name__ == "__main__":
    # Parse command line arguments  
    parser = argparse.ArgumentParser(description = "Age Classification")
    parser.add_argument('--input', type = str, default = 'datasets/facebook_clean_data/artist_edges.csv', help = 'output from community detection')
    args = parser.parse_args()

    # Get the graph name for future saving purposes
    filename = getGraphName(args.input)

    # subprocess.run(["ls", "-l"])
