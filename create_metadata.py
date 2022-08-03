import os
import pandas as pd
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="Generate audio")
    parser.add_argument(
        "--output_dir",
        '-o',
        type=str,
        default=None,
        help="The path to the output directory",
    )

    parser.add_argument(
        "--metadata_file",
        '-f',
        type=str,
        default=None,
        help="The path to the metadata file",
    )

    parser.add_argument(
        "--audio_output_dir",
        '-d',
        type=str,
        default=None,
        help="The path to the audio output directory",
    )

    args = parser.parse_args()
    return args

def gen_metadata_csv(output_dir, metadata_file, audio_output_dir):
    #read wav.scp and segments in output_dir
    wav_scp = pd.read_csv(os.path.join(output_dir, 'wav.scp'), sep=' ', header=None)
    segments = pd.read_csv(os.path.join(output_dir, 'segments'), sep=' ',  header=None)
    wav_scp.columns = ['filename', 'path']
    segments.columns = ['segment_id', 'filename', 'start', 'end']

    #merge wav.scp and segments by filename
    metadata = pd.merge(wav_scp, segments, on='filename')
    print(metadata.head())
    #add audio_output_dir before segment_id
    metadata['segment_id'] = metadata['segment_id'].apply(lambda x: os.path.join(audio_output_dir, x))
    #save metadata['segment_id', 'path', 'start', 'end'] to csv
    metadata = metadata[['segment_id', 'path', 'start', 'end']]
    metadata.to_csv(metadata_file, index=None, header=['segment_id', 'path', 'start', 'end'])


def main():
    args = parse_args()
    gen_metadata_csv(args.output_dir, args.metadata_file, args.audio_output_dir)
    

if __name__ == "__main__":
    main()