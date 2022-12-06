import argparse 
import subprocess
import time 

def getGraphName(input_directory):
    input_dir = args.input 
    file_path = input_dir.split('/')
    filename = file_path[len(file_path)-1]
    filename = filename.replace('.csv', '')
    return filename

if __name__ == "__main__":
    
    start_time = time.time()
    # Parse command line arguments  
    parser = argparse.ArgumentParser(description = "Demofile ArgsParser")
    parser.add_argument('--input', type = str, default = 'dataset/git_web_ml/musae_git_edges.csv', help = 'output from community detection')
    args = parser.parse_args()

    # Get the graph name for future saving purposes
    filename = getGraphName(args.input)

    # Run the full pipeline

    # Step 1:  Run Label Propagation
    print("\n")
    print("--------Step 1-1: Running Label Propagation for Community Detection--------")
    print("\n")
    subprocess.run(["python", "label_propagation/label_propagation.py", "--input", args.input, "--output", "outputs/output_LP/" + filename + ".json",]) 
    print("\n")

    # Step 1-2: Preprocess output of Label Propagation to be ready for KL
    print("--------Step 1-2: Preprocessing output of Label Propagation to be ready for KL--------")
    print("\n")
    subprocess.run(["python", "preprocess/preprocess_LP.py", "--input", "outputs/output_LP/" + filename + ".json", "--output", "outputs/output_preprocess/processed_" + filename + ".txt", "--original_edges", args.input])
    print("\n")

    # Step 2: Run KL graph partitioning algorithm 
    print("--------Step 2: Running KL graph partitioning algorithm--------")
    print("\n")
    subprocess.run(["python", "baseline/kl_partitioning/kl.py", "--input", "outputs/output_preprocess/processed_" + filename + ".txt", "--output", "outputs/output_KL/partitioned_" + filename + ".txt",])
    print("\n")

    # Step 3: Uncoarsen graph to original form
    print("--------Step 3: Uncoarsen the graph to produced the final output--------")
    subprocess.run(["python", "uncoarsen/uncoarsen.py", "--LP", "outputs/output_LP/" + filename + ".json", "--KL", "outputs/output_KL/partitioned_" + filename + ".txt", "--output", "outputs/output_uncoarsened/uncoarsened_" + filename + ".json",])
    print("\n")

    print("--------Total Running Time: %s seconds--------" % (time.time() - start_time))
    print("\n")
    print("-------- Partitioned Graph is saved in: outputs/output_uncoarsened/uncoarsened_" + filename + ".json   --------")
