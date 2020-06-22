source_path = 'MagickSlicer-master'
output_path = 'output'
input_path = 'input'

# INSTRUCTIONS: 
# 1) Place all input jpg files in the input folder.
# 2) Run this Python-2.7 script from the command-line.
# 3) Wait for the script to finish (up to several seconds per individual file).
# 4) Look in the output folder for the result.

import os
import subprocess

def rm_extension(fn, extension): return fn[:fn.find(extension)]

filenames = os.listdir(input_path)
filenames.sort()

for fn in filenames:

	# skip hidden macOS stuff like .DS_Store
	if fn[0] == '.': continue

	run_arg = os.path.join(source_path, 'magick-slicer.sh')
	input_arg = os.path.join(input_path, fn)
	output_arg = os.path.join(output_path, rm_extension(fn, '.jpg'))
	command = "%s %s %s" % (run_arg, input_arg, output_arg)
	print "command: ", command
	subprocess.call(command, shell='True')