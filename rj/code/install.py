#!/usr/bin/env python
"""
Author: Ariel Anders
Install packages for dynamics class using conda
"""

try:
    import conda.cli
except:
    print """
    Cannot install packages without miniconda
    Install miniconda from https://conda.io/miniconda.html
    """
    raise SystemExit

packages = """\
-c anaconda numpy
-c anaconda scipy 
-c anaconda matplotlib 
-c anaconda jupyter 
-c https://conda.anaconda.org/kne pybox2d
-c cogsci pygame
"""

pkgs = packages.strip().split("\n")

for pkg in pkgs:

    try:
        cmd = "conda install -y %s" % pkg
        cmd = cmd.strip().split(" ")
        print "attempting to install %s " % pkg
        conda.cli.main(*cmd)
    except:
        print "Warning could not install %s " % pkg
    
success = 0

for pkg in pkgs:
    name = pkg.strip().split(" ")[-1]
    if name == "pybox2d":
        name = "Box2D"
    cmd = "import %s " % name
    try:
        exec(cmd)
        success +=1
    except:
        print "Import of package %s failed! "% name

if success == len(pkgs):
    print "Success: Done installing packages for dynamics!"
else:
    print "Warning could not install all packages"
