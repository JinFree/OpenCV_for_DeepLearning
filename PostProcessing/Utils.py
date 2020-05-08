import os

def path_function(rel_path_to_object):
	filePath = os.path.dirname(os.path.realpath(__file__))
	abs_path_to_object = filePath + rel_path_to_object
	return abs_path_to_object