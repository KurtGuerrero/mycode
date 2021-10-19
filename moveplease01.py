#!/usr/bin/env python3
""" sample script for moving and renaming a file """

# standard library imports
import shutil
import os

def main():
    """ called at runtime """
    # Force the Python program to 'start' in the home user directory
    os.chdir('/home/student/mycode/')

    # move the file to the path destination
    shutil.move('raynor.obj', 'ceph_storage/')

    # for safety, we don't want to overwrite the file if it's already there
    xname = input('What is the new name for kerrigan.obj? ')
    shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)

main()
