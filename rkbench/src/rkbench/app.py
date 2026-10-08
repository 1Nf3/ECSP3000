""" app.py
Author : Elliott Jelbert
University : University Of Southampton
Email : ej1g24@soton.ac.uk

Purpose : Is the main entry function for rkbench
"""



import argparse
from pathlib import Path


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("testDirectory", help="Please specify a directory", type=Path)
    args = parser.parse_args()

    if not args.testDirectory.is_dir():
        parser.error(f"not a directory {args.testDirectory}")

    print("Hello from rkbench!")
    print("By Elliott Jelbert - ej1g24@soton.ac.uk")

    print("Initialising...")

    # Will run initialise.py to handle all pre-test checks including checking hashes, the environment, all disclaimers etc.
    # - the errors handled here will likely be raised here s.t the hashes not matching and then an error thrown which will be caught here and then exit out

    # After that returns and is valid we will run the orchestrator (the main experiment logic) which will spin up all the sessions and collate the results
    # - Errors that fire in the individual experiments will be caught by the orchestrator and added to the results matrix

    # Then we will probably use a smart wasy of reading the results set.
