short
=====

manage aliases in bash

Making aliases more useful. '-v' option hides an alias
unless we are run w/ -v.  This is for aliases that we need to be reminded 
of less often.  Tags can be used to group aliases.  'tag=fun' allows
all fun tagged commands only to be shown.  Specifying a tag
will override -v only. aliases without descriptions are ignored.

In file start aliases to parse with separator: 
    '#alias_definitions:'

Now add an alias:

    #desc [n <file>] nano with word warp, smooth scroll
    alias n="nano -wES"

Run this script and see help:

    n              -- [n <file>] nano with word warp, smooth scroll

Make an alias only show up with '-v':

    n              -- [n <file>] nano with word warp, smooth scroll -v  

Run this script and see:

    Nothing....all aliases are -v style only now need -v

Run this script with '-v':
    n              -- [n <file>] nano with word warp, smooth scroll -v  

Group aliases by tags:

    #desc git add tag=git
    alias ga='git add'
    #desc git log tag=git
    alias gl='git log'

Show me defined tags, run with literal 'tag' argument

    root@vm-rush:~/short# short git
    Tagged: git
    ga             -- git add  
    gl             -- git log
