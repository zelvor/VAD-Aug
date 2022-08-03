import os
from time import sleep
import pandas as pd
import argparse
from pydub import AudioSegment
from requests import head

def parse_args():
    parser = argparse.ArgumentParser(description="Generate audio")
    parser.add_argument(
        "--metadata_file",
        '-f',
        type=str,
        default=None,
        help="The path to the metadata file",
    )
    args = parser.parse_args()
    return args

def gen_segment_audio(metadata_file):
    metadata = pd.read_csv(metadata_file)
    metadata.columns = ['segment_id', 'path', 'start', 'end']
    for index, row in metadata.iterrows():
        segment_id = row['segment_id']
        path = row['path']
        start = row['start']
        end = row['end']
        #read audio file
        audio = AudioSegment.from_wav(path)
        #slice audio file
        audio = audio[start * 1000:end * 1000]
        #save audio file
        audio.export(segment_id+'.wav', format='wav')

def main():
    args = parse_args()
    gen_segment_audio(args.metadata_file)
    

if __name__ == "__main__":
    main()