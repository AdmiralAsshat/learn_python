#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import sys
import urllib

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""


def read_urls(filename):
  """Returns a list of the puzzle urls from the given log file,
  extracting the hostname from the filename itself.
  Screens out duplicate urls and returns the urls sorted into
  increasing order."""
  # +++your code here+++
  images = []
  f = open(filename, 'rU')
  # Strip all before underscore from filename to get URL
  source_url = filename.split('_')[1]
  for line in f:
    match = re.search(r'GET (\S*puzzle\S*) HTTP', line)
    if (match):  
      to_add = 'http://' + source_url + match.group(1)
      if to_add not in images:
        images.append(to_add)
  return sorted(images)

def download_images(img_urls, dest_dir):
  """Given the urls already in the correct order, downloads
  each image into the given directory.
  Gives the images local filenames img0, img1, and so on.
  Creates an index.html in the directory
  with an img tag to show each local image file.
  Creates the directory if necessary.
  """
  # +++your code here+++
  filenum = 0
  if not os.path.exists(os.path.abspath(dest_dir)):
      print "Directory %s did not exist. Creating..." % (dest_dir)
      os.mkdir(dest_dir)
  index = open(os.path.join(dest_dir,'index.html'), 'w')
  index.write('<html>\n<body>\n')
  for url in img_urls:
    img_name = "img" + str(filenum)
    img = urllib.urlretrieve(url, os.path.join(dest_dir, img_name))
    print "Retrieving...", url
    index.write('<img src="%s">' % (img_name))
    filenum +=1
  index.write('\n</body>\n</html>')
  index.close()

def main():
  args = sys.argv[1:]

  if not args:
    print 'usage: [--todir dir] logfile '
    sys.exit(1)

  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  img_urls = read_urls(args[0])

  if todir:
    download_images(img_urls, todir)
  else:
    print '\n'.join(img_urls)

if __name__ == '__main__':
  main()
