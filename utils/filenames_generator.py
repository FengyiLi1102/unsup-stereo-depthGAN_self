import argparse
import glob
from tqdm import tqdm
import os

def main(opts):
    """
    Generate a txt file like the ones in the filenames folder for training.
    Content format in txt:
    2011_09_30/2011_09_30_drive_0028_sync/image_02/data/0000001562.jpg
    2011_09_30/2011_09_30_drive_0028_sync/image_03/data/0000001562.jpg

    My txt:
    left/tl4_2022-02-09_13A/image_0001_left.png right/tl_2022-02-09_13A/image_0001_right.png
    """
    # Obtain the folder names containing the videos
    left_img_path = os.listdir(os.path.join(opts.data_path, "left"))
    right_img_path = os.listdir(os.path.join(opts.data_path, "right"))
    print(f"Find {left_img_path} videos in the folder...")

    # Trim the folder names to match the same videos in two angles





if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate dataset for rectified clouds data")

    parser.add_argument("-data_path", type=str, help="Root path to the training data",            required=True)
    parser.add_argument("-out_path",  type=str, help="Path to the directory to store the frames", required=True)

    opts = parser.parse_args()

    main(opts)