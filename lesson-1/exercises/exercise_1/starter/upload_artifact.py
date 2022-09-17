"""
Summary:
    Weights and Balances example for creating a run and adding an artifact.
Author:
    Nikolas Hunt
Date:
    September 2022
"""
import argparse
import logging
import pathlib

import wandb

# initialize logging
logging.basicConfig(level=logging.INFO, format="%(asctime)-15s %(message)s")
logger = logging.getLogger()


def go(args):
    """Creates a wandb run and adds a file artifact.
    Args:
        args (Namespace): arguments given by the user in the command line.
    """

    # Initialize a wandb run
    logger.info("Creating run exercise_1")
    run = wandb.init(project="exercise_1", job_type="upload_file")

    # Create an instance of the class ``wandb.Artifact``
    artifact = wandb.Artifact(
        name=args.artifact_name,
        type=args.artifact_type,
        description=args.artifact_description,
    )

    # Attach file to artifact and log it
    artifact.add_file(args.input_file)
    run.log_artifact(artifact)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Upload an artifact to W&B", fromfile_prefix_chars="@"
    )

    parser.add_argument(
        "--input_file",
        type=pathlib.Path,
        help="Path to the input file",
        required=True,
    )

    parser.add_argument(
        "--artifact_name",
        type=str,
        help="Name for the artifact",
        required=True,
    )

    parser.add_argument(
        "--artifact_type",
        type=str,
        help="Type for the artifact",
        required=True,
    )

    parser.add_argument(
        "--artifact_description",
        type=str,
        help="Description for the artifact",
        required=True,
    )

    args = parser.parse_args()

    go(args)
