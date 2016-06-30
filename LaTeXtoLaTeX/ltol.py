#!/usr/bin/env python

import sys
import re
import os
import glob

import component
import myoperations

#################################
# First use the command-line arguments to set up the
# input and output files.
#################################

if not len(sys.argv) == 3:
    print 'To convert a LaTeX file to a different form, do either:'
    print './ltol.py inputfile outputfile'
    print 'to convert one file, or'
    print './ltol.py inputdirectory outputdirectory'
    print 'to convert all the .html files in a directory.  The outputdirectory must already exist.'
    sys.exit()

component.inputname = sys.argv[1]
component.outputname = sys.argv[2]

if component.inputname == component.outputname:
    print "must have input distinct from output"
    print "try again"
    sys.exit()

if os.path.isfile(component.inputname) and not os.path.isdir(component.outputname):
    component.iofilepairs.append([component.inputname,component.outputname])
    print "converting one file:",component.inputname

elif os.path.isdir(component.inputname) and os.path.isdir(component.outputname):
    inputdir = component.inputname
    inputdir = re.sub(r"/*$","",inputdir)  # remove trailing slash
    outputdir = component.outputname
    outputdir = re.sub(r"/*$","",outputdir)  # remove trailing slash
    outputdir = outputdir + "/"              # and then put it back
    latexfiles = glob.glob(inputdir + "/*.html")
    for inputfilename in latexfiles:
        outputfilename = re.sub(".*/([^/]+)", outputdir + r"\1", inputfilename)
        outputfilename = re.sub("html$", "mbx", outputfilename)
        if inputfilename == outputfilename:
            print "big problem, quitting"
        component.iofilepairs.append([inputfilename, outputfilename])
#    print latexfiles
#    print inputdir 
#    print component.iofilepairs

else:
    print "Not proper input.  Does target directory exist?"
    sys.exit()

# print component.iofilepairs

for inputfile, outputfile in component.iofilepairs:

    component.inputstub = inputfile
    component.inputstub = re.sub(".*/","",component.inputstub)
    component.inputstub = re.sub("\..*","",component.inputstub)
    print "file stub is ",component.inputstub

    with open(inputfile) as infile:
        component.onefile = infile.read()

#    print component.onefile[:100]

#    myoperations.setvariables(component.onefile)

#    component.onefile = myoperations.mytransform(component.onefile)
    component.onefile = myoperations.transformMAT101(component.onefile)

    with open(outputfile, 'w') as outfile:
        outfile.write(component.onefile)

#     print component.replaced_macros

sys.exit()

latexfiles = glob.glob(latexfiledir + "/*.tex")
if nonsense == xxx:
        print "found these LaTeX files:",latexfiles
        if len(latexfiles) == 1:
            junk.allworks[work_key]['latexfile'] = latexfiles[0]
        else:
            print "Warning, multiple latex files:",latexfiles
            for file in latexfiles:
                with open(file) as f:
                    filecontents = f.read()
                    if "begin{document}" in filecontents:
                         junk.allworks[work_key]['latexfile'] = file
                         break

