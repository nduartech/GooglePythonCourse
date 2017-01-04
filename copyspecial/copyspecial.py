#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them
def get_special_paths(dir):
  folder = os.path.abspath(dir)
  filenames = os.listdir(folder)
  abs_paths = []
  for e in filenames:
    match = re.search(r'_[a-zA-Z0-9]+_', e)
    if match:
      abs_paths.append(folder+'/'+e)
  if len(abs_paths) == 0:
    sys.exit(1)
  else:
    return abs_paths


def copy_to(paths, dir):
  if not os.path.exists(dir):
    os.mkdir(dir)
  abs_path = os.path.abspath(dir)
  for p in paths:
    shutil.copy(p, abs_path)


def zip_to(paths, zip_path):
  cmd = "zip -j " + zip_path
  for l in paths:
    cmd += (" " + l)
  (status, output) = commands.getstatusoutput(cmd)
  if status:
    sys.stderr.write(output)
    sys.exit(1)
  print output



def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]

  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)

  spec_paths = get_special_paths(args[0])
  if todir:
    copy_to(spec_paths, todir)
  elif tozip:
    zip_to(spec_paths, tozip)
  else:
    for f in spec_paths:
      print f
  
if __name__ == "__main__":
  main()
