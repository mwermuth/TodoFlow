#!/usr/bin/python
from config import should_print_path as should_print
from config import projects_path
import topy

t = topy.from_file(projects_path)
if int(open(should_print).read()):
    print t.as_plain_text(colored=True, indent=True)
else:
    print 'BLA'
