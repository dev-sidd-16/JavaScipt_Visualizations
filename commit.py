#!/usr/bin/env python
from os import *
from sys import *
from datetime import*
try:
    message = argv[1]
except:
    message = str(datetime.now().time())

system("git add *")
cmd = "git commit -m \""+message+"\""
#print cmd
system(cmd)
system("git push -u origin master")
