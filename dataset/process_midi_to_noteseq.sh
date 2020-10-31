#!/bin/bash

INPUT_DIRECTORY=lofi
OUTPUT_FILE=lofi.tfrecord

python convert_dir_to_note_sequences.py \
	--input_dir=$INPUT_DIRECTORY \
	--output_file=$OUTPUT_FILE \
	--log=INFO
