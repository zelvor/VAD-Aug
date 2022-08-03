#gen wav.scp and save it in metadata.csv's parent directory
python prep_wavscp.py \
    --audio_dir D:/_CV/VAD-Aug/VAD-Aug/audio_output \
    --metadata_file D:/_CV/VAD-Aug/VAD-Aug/iocsv/metadata.csv\ 

#create the segment manifest file
python D:/_CV/VAD-Aug/voxseg/voxseg/main.py -M D:/_CV/VAD-Aug/voxseg/VAD-Aug/features/new-vad.h5 D:/_CV/VAD-Aug/VAD-Aug/iocsv D:/_CV/VAD-Aug/VAD-Aug/output\

#create metadata.csv
python create_metadata.py \
    --output_dir D:/_CV/VAD-Aug/VAD-Aug/output \
    --metadata_file D:/_CV/VAD-Aug/VAD-Aug/iocsv/metadata.csv \
    --audio_output_dir D:/_CV/VAD-Aug/VAD-Aug/speech\

#4. create audio_segment
#.\create_segment_manifest.sh 1, do this, else dont.
if [ $1 -eq 1 ]
then
    echo "Saving segments..."
    python create_segments.py \
        --metadata_file D:/_CV/VAD-Aug/VAD-Aug/iocsv/metadata.csv\

fi