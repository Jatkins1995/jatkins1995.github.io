#!/usr/bin/python

# uses https://github.com/xiaoxu193/PyTeaser

from pyteaser import SummarizeUrl
f = open('testFile', 'r')
for line in f:   
   if line[0] != '*':
      url = line
      summaries = SummarizeUrl(url)
      if summaries is not None:
         print url
         for i in summaries:
            print i
      else:
         print "Error with " + url
   else:
      print line [1:]

   print "\n\n"
