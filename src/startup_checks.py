import os
import sys


# Perform checks before running the program.
def startup_checks(args):
    # Check that the user has the required packages installed.
    required_packages = ['dvr_scan']
    for package in required_packages:
        try:
            __import__(package)
        except ImportError as e:
            print(f"You are missing the package {package}.")
            print("Please install it before running this program.")
            print(f"Error: {e}")
            sys.exit(1)

    # Check that ffmpeg is installed on the system.
    try:
        import subprocess
        subprocess.run(['ffmpeg', '-version'], stdout=subprocess.DEVNULL)
    except FileNotFoundError:
        print("You are missing the package ffmpeg.")
        print("Please install it before running this program.")
        sys.exit(1)

    # check that input file exists
    if not os.path.isfile(args.input_video_path):
        print(f'Input file "{args.input_video_path}" does not exist.')
        sys.exit(1)
