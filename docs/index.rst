octocmd: command line for OctoPrint
===================================

octocmd makes it easy to control your `OctoPrint <http://octoprint.org/>`_ server from the command line.  It understands how to process *.scad* files into *.stl* with `OpenSCAD <http://http://www.openscad.org/>`_, and *.stl* files to make *.gcode* files with `Cura <https://github.com/daid/Cura>`_.

============
Installation
============

Installation is easy with pip:

::

    pip install https://github.com/vishnubob/octocmd/archive/master.zip

You can also install octocmd into a virtual environment:

::

    virtualenv octocmd
    . octocmd/bin/activate
    pip install https://github.com/vishnubob/octocmd/archive/master.zip

=============
Configuration
=============

Before you can start using octocmd, you have to configure it first.  It reads a
config file called *.octoprint.conf* from your home directory.  You can either
create it by hand or you can have octocmd do it for you by running the **init**
sub-command:

::

    $ octocmd init
    OctoPrint URL: http://octoprint/
    OctoPrint API Key: MY_API_KEY
    This configuration works, keep it? [Y/n]: y
    Saving config file to '/home/linda/.octocmd.conf'

======
Status
======

You can get a status update from OctoPrint with the **status** sub-command:

::

    $ octocmd status
    state: Printing
        flags: operational=True, paused=False, printing=True, sdReady=True, error=False, ready=True, closedOrError=False
    temperature:
        bed: actual=58.4, target=60.0, offset=0
        tool0: actual=250.2, target=250.0, offset=0
    sd: ready=True

========
Printing
========

You can print files with OctoPrint using the **print** sub-command.

::

    $ octocmd print rabbit.gcode
    [Tue May 20 22:05:51 2014 octocmd] uploading, selecting, printing rabbit.gcode on OctoPrint

If you try to print from a *.scad* file, or a *.stl* file, octocmd will
automatically convert the file to a *.gcode* file before uploading it to the
OctoPrint server:

::

    $ octocmd print rabbit.scad
    [Tue May 20 22:05:34 2014 octocmd] generating '/home/linda/rabbit/rabbit.stl' with OpenSCAD
    [Tue May 20 22:05:46 2014 octocmd] generating '/home/linda/rabbit/rabbit.gcode' with Cura
    [Tue May 20 22:05:51 2014 octocmd] uploading, selecting, printing rabbit.gcode on OctoPrint
