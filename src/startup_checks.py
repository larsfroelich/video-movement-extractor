import sys


def startup_checks():
    """Check that the user has the required packages installed."""
    # Check that the user has the required packages installed.
    required_packages = ['dvr-scan']
    for package in required_packages:
        try:
            __import__(package)
        except ImportError:
            print("You are missing the package {}.".format(package))
            print("Please install it before running this program.")
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
    if not os.path.isfile(src_video_path):
        print(f'Input file "{src_video_path}" does not exist.')
        sys.exit(1)
