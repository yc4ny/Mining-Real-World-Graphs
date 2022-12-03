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
                        default="data/custom/test_1.csv",
	                help="Input graph path.")

    parser.add_argument("--assignment-output",
                        nargs="?",
                        default="./output/test_1.json",
	                help="Assignment path.")

    parser.add_argument("--weighting",
                        nargs="?",
                        default="overlap",
	                help="Overlap weighting.")

    parser.add_argument("--rounds",
                        type=int,
                        default=30,
	                help="Number of iterations. Default is 30.")

    parser.add_argument("--seed",
                        type=int,
                        default=42,
	                help="Random seed. Default is 42.")

    return parser.parse_args()
