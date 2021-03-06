#!/usr/bin/python
import os, sys
from os.path import expanduser
import subprocess

alias_files = ['.bash_aliases', 
               '.bash_profile']

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

    def disable(self):
        self.HEADER = ''
        self.OKBLUE = ''
        self.OKGREEN = ''
        self.WARNING = ''
        self.FAIL = ''
        self.ENDC = ''

def extract_command(line, tag, verbose):
    if 'desc' not in line:
        return
    try:
        desc = aliases[aliases.index(line)]
        cmd = aliases[aliases.index(line) + 1]
    except ValueError, e:
        print "Error: %s invalid" % line
        return

    if tag and not 'tag=%s' % tag in desc:
        return
    if not tag:
        if not verbose and '-v' in line:
            return
    return (parse_cmd(cmd), parse_desc(desc))

def parse_cmd(command):
    return command.split('=')[0].split()[1]

def parse_desc(desc, tagonly=False):
    if 'tag=' in desc:
        desc, tag = desc.split('tag=')
    if tagonly:
        return tag.split()[0]
    return desc.split('desc ', 1)[1]

def bold(text):
    return '\033[1m' + text

def blue(text):
    return bcolors.OKBLUE  + text + bcolors.ENDC

def print_usage(alias):
    print "%-27s -- %-50s" % (bold(blue(alias[0])), alias[1])

def user_home():
    return expanduser("~")

#return first found defined alias file
for f in alias_files:
    aliases = os.path.join(user_home(), f)
    if os.path.exists(aliases):
        shortfile = aliases
        break

def set_opts():
    if not len(sys.argv) >= 2:
        return None, None
    verbose = False
    if '-v' in sys.argv:
        verbose = True
    if sys.argv[1] == '-v':
        return verbose, None
    else:
        return verbose, sys.argv[1]

def extract_tags(line):
    if 'tag=' in line:
        return parse_desc(line, tagonly=True)

v, tag = set_opts()

if tag:
    print "Tagged:", tag

if v:
    print "Verbose included"

aliases = open(shortfile).read().split('alias_definitions:')[1].splitlines()
#if special 'tag' literal then pull out defined tags from file
if tag == 'tag':
    for tag in set(filter(None, map(extract_tags, aliases))):
        print "%s" % (bold(blue(tag)))
else:
    map(print_usage, filter(None, map(lambda a: extract_command(a, tag, v), aliases)))
