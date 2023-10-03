#Script to extract tar archives into a specific directory

import tarfile 
import argparse
import os
import sys

parser = argparse.ArgumentParser(description="Extract the tar archives into a directory")
parser.add_argument('-f', '--filename', type=str, required=True, help="Provide the name/path of the tar file you need to extract")
parser.add_argument('-d', '--directory', type=str, required=True, help="Provide the name/path of the directory")
args = parser.parse_args()

#Function to extract the tar archive into a directory

def process_path(path):

	'''
	Function checks if the directory path given is absolute or relative. 
	'''

	if os.path.isabs(path) == False:
		current_working_dir = os.getcwd()
		abs_path = os.path.join(current_working_dir, path)
		return abs_path

	else:
		return path


def process_files(file):

	'''
	Function will process the user input for the filename
	'''
	path = process_path(file)

	if os.path.exists(path):
		return path
	else:
		print("[+++] Log file does not exist. Please provide a correct path.")
		exit()


def extract_tar(filename, directory):

	'''
	Function extracts the tar.gz file and extracts the files into a given directory.

	'''
	filename = process_files(filename)
	directory = process_path(directory)
	
	file = tarfile.open(filename)
	file.extractall(directory)
	file.close()


def extract_xz():

	'''
	This function will extract the compressed xz files
	'''
	log_directory = 'sc/run/janus/'
	directory = process_path(args.directory)
	path = os.path.join(directory, log_directory)
	os.chdir(path)


	try:
		import lzma
	except ImportError:
		from backports import lzma

	for file in os.listdir():
		if file.endswith(".xz"):
			with lzma.open(file,'r') as fid:
					with open(f'{file}.txt', 'wt') as fout:
						fout.write(fid.read().decode("utf-8"))
			os.remove(file)
	
ex1 = extract_tar(args.filename, args.directory)	
ex2 = extract_xz()









