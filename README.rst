octocmd
=======

octocmd makes it easy to control your `OctoPrint <http://octoprint.org/>`_ server from the command line.  It understands how to process .scad files into .stl with `OpenSCAD <http://http://www.openscad.org/>`_, and .stl files to make .gcode files with `Cura <https://github.com/daid/Cura>`_.  Check out the `documentation http://octocmd.readthedocs.org/`_.

::

  $ octocmd print rabbit.scad
  [Tue May 20 22:05:34 2014 octocmd] generating '/home/linda/rabbit/rabbit.stl' with OpenSCAD
  [Tue May 20 22:05:46 2014 octocmd] generating '/home/linda/rabbit/rabbit.gcode' with Cura
  [Tue May 20 22:05:51 2014 octocmd] uploading, selecting, printing rabbit.gcode on OctoPrint
