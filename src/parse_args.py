import argparse


def parse_program_args():
    parser = argparse.ArgumentParser(
        prog='Video-Movement-Extractor',
        description='Reduces a video to the parts containing visual movement',
    )
    # Standard options
    parser.version = "00.01"
    parser.add_argument('-v', '--verbose', action='store_true')  # on/off flag
    parser.add_argument('--version', action='version')

    # General arguments
    parser.add_argument('input_video_path')  # positional argument

    args = parser.parse_args()
    return args
