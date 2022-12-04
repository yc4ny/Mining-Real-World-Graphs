import argparse 

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = "Age Classification")
    parser.add_argument('--input', type = str, default = 'datasets/facebook_clean_data/artist_edges.csv', help = 'output from community detection')
    args = parser.parse_args()