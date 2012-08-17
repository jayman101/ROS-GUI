#!/usr/bin/python

import os

"""
This file, as its name suggests, generates a python module which imports
other modules.

The way it works is it scans the local directory for python files, if
it finds one, it imports it, and adds it as an object to an array named "modules".

This file then removes a file set as OUTPUTFILE, and then dumps the generated code in there.


The idea is that this file is executed prior to the application importing OUTPUTFILE. Resulting in the user not needing to manipulate anything but the modules they wish to create.

If there is another way of doing what this program does, it is automatically better than thiss application by default. I'm not even doubting that this program is a very, very, bad idea (but obviously dont know a better solution).

We also depend on write access to OUTPUTFILE and read access to cwd.
"""

"""
TODO:
Pretty sure os.pwd == execution directory when python was executed, not src dir. Will break things.
"""

OUTPUTFILE = "ModuleObjects"

BLACKLIST = ["generateImport", "ModuleFrame", OUTPUTFILE]

imports = []
for file in os.listdir('./'):
    # test what if no ext
    # Getting filename w/o extension for code generation
    fileName, fileExtension = os.path.splitext(file)

    if fileExtension  == ".py" and fileName not in BLACKLIST:
        imports.append(fileName)
        
FileData = [ "#!/usr/bin/python3",
             "# See generateImport.py for a better explanation of this file",
             ""] # Data we're going to write to file

modulesArray = "" # Generated values for modules. 
for line in imports:
    FileData.append("import " + line)

    # There is a more elegant way to do this, I forgot how :(
    modulesArray += line + ', '
if len(FileData) > 0:
    modulesArray = modulesArray[:-2]

FileData.append("")
FileData.append("modules = [%s]" % modulesArray)

FilePath = "./%s.py" % OUTPUTFILE
if os.path.exists("./%s.py"):
    os.remove(FilePath)

File = open(FilePath, 'w')
for line in FileData:
    File.write(line + "\n")

File.flush()
File.close()
