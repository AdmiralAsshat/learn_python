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

# Write functions and modify main() to call them

def get_special_paths(dir):
  filenames = os.listdir(dir)
  specials = []
  for filename in filenames:
    if re.search(r'__\w+__', filename):
      specials.append(os.path.abspath(os.path.join(dir, filename)))
  return specials

def copy_to(paths, to_dir):
  if not os.path.exists(os.path.abspath(to_dir)):
    print "Directory %s did not exist. Creating..." % (to_dir)
    os.mkdir(to_dir)
  for path in paths:
    file = os.path.basename(path)
    shutil.copy(path, os.path.join(to_dir, file))

def zip_to(paths, zippath):
  cmd = 'zip -j ' + zippath + ' ' + ' '.join(paths)
  print "Command to run:", cmd
  (status, output) = commands.getstatusoutput(cmd)
  if status:
    sys.stderr.write(output)
    sys.exit(1)
  print output
  return


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

  # +++your code here+++
  # Call your functions
  paths = []
  for path in args:
    paths.extend(get_special_paths(path))
  if todir:
    copy_to(paths, todir)
  elif tozip:
    zip_to(paths, tozip)
 
if __name__ == "__main__":
  main()
