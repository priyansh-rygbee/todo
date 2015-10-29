import sys
import os
home_dir = os.path.join(os.path.expanduser("~"))
if '.todorc' in os.listdir(home_dir):
	print "Found config file. Reading content, setting up user."

print "Welcome to todo, the unofficial command line interface for Todoist.\nTo store your user settings and other preferences, we would need to create a '.todorc' file in your home directory.\n"
if raw_input("Do you allow it? [y/n]")[0].lower() == 'y':
	print "Creating .todorc"
	config_file = open(os.path.join(os.path.expanduser("~"), '.todorc'),'w+')
	

