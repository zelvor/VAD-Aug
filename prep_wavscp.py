import os
import pandas as pd
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="Generate wav.scp file")
    parser.add_argument(
        "--audio_dir",
        '-d',
        type=str,
        default=None,
        help="The path to the input audio directory",
    )

    parser.add_argument(
        "--metadata_file",
        '-f',
        type=str,
        default=None,
        help="The path to the metadata file",
    )

    args = parser.parse_args()
    return args

def gen_wav_scp(audio_directory):
    args = parse_args()
    # get all the files in the audio directory, save with format name, path
    wav_scp_df = pd.DataFrame(columns=['filename', 'path'])
    for root, dirs, files in os.walk(audio_directory):
        for file in files:
            if file.endswith(".wav"):
                filename = file.split('.')[0]
                path = os.path.join(root, file)
                wav_scp_df = wav_scp_df.append({'filename': filename, 'path': path}, ignore_index=True)
    # pathfolder = os.path.dirname(args.metadata_file)
    wav_scp_df.to_csv(os.path.join(os.path.dirname(args.metadata_file), 'wav.scp'), header=None, index=None, sep=' ')


def main():
    args = parse_args()
    gen_wav_scp(args.audio_dir)

if __name__ == "__main__":
    main()