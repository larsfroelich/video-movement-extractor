import os.path

from src.extract_video import extract_video
from src.parse_args import parse_program_args
from src.startup_checks import startup_checks

args = parse_program_args()
print(f'Config: {args}\n')
src_video_path = args.input_video_path

print(f'source video path: "{src_video_path}"')


# perform startup checks
startup_checks()

# extract video
extract_video(src_video_path)
