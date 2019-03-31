# IFTTT python

# Purpose
This repository is meant to be used for the following reasons:

A) Keep a record of modifications made to the original code.

B) Create a new database for modified IFTTT commands providing
a simple template.

C) Maintain a consistent database for my personal use in the event
of a complete system reconstruction.

D) Be available to users that want to explore using IFTTT to 
manage computer systems.

# Function

Each command file is assigned a number. The number is called, translated
into the command file, then processed.

The remStartup script removes command files that can cause loops by using 
the command file name under [FILES]

The runCommand script executes commands by using the command file under
[COMMANDS]

The only user interaction with the script needed is through the files.ini
TO GET a files.ini, rename example_files.ini to the corresponding name.