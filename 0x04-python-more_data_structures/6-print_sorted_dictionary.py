#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
	for _dict in sorted(a_dictionary):
		print("{}: {}".format(_dict, a_dictionary[_dict]))
