"""Parsing the parameters."""

import argparse

def parameter_parser():
    """
    A method to parse up command line parameters.
    The default hyperparameters give a good quality clustering. Default weighting happens by neighborhood overlap.
    """
    parser = argparse.ArgumentParser(description="Run Label Propagation.")

    parser.add_argument("--input",
                        nargs="?",
                        default="datasets/facebook_clean_data/artist_edges.csv",
	                help="Input graph path.")

    parser.add_argument("--output",
                        nargs="?",
                        default="outputs/output_LP /artist.json",
	                help="Output path.")

    parser.add_argument("--weighting",
                        nargs="?",
                        default="overlap",
	                help="Overlap weighting.")

    parser.add_argument("--rounds",
                        type=int,
                        default=50,
	                help="Number of iterations.")

    parser.add_argument("--seed",
                        type=int,
                        default=50,
	                help="Random seed.")

    return parser.parse_args()
