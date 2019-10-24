Doxygen filter for Google Protocol Buffers .proto files
=======================================================

How to enable this filter in Doxygen:
  1. Generate Doxygen configuration file with command 'doxygen -g <filename>':
       e.g.  doxygen -g doxyfile
  2. In the Doxygen configuration file, find FILE_PATTERNS and add *.proto:
       FILE_PATTERNS          = *.proto
  3. In the Doxygen configuration file, find EXTENSION_MAPPING and add proto=C++:
       EXTENSION_MAPPING      = proto=C++
  4. In the Doxygen configuration file, find INPUT_FILTER and add this script:
       INPUT_FILTER           = "python proto2cpp.py"
  5. Run Doxygen with the modified configuration:
       doxygen doxyfile
   
Following change is recommended by Timo Marjoniemi but must not be used:
  In the Doxygen configuration file, find JAVADOC_AUTOBRIEF and set it enabled:
    JAVADOC_AUTOBRIEF      = YES
   
Version history
===============

0.8-beta (2018-12-09) OSI
-------------------------
  - Bugfix regarding long comments, remove typo
  - Bugfix and extensions have been made by Open Simulation Interface (OSI) Carsten Kuebler https://github.com/OpenSimulationInterface

0.7-beta (2018-04-19) OSI
-------------------------
  - Include changes from University of California.
  - Support for all OSI *.proto files.
  - Separate statement and comments to treat both parts differently (remove bugs 
    regarding string modifications).
  - Remove "option" statements.
  - Add support for "extend" statements.
  - Change "repeat" from Template to standard member. --> Better collaboration 
    diagrams.
  - Fix problems with references of nested messages (replace "." with "::").
  - Change mapping from C to C++.
  - Bugfix and extensions have been made by Open Simulation Interface (OSI) Carsten Kuebler https://github.com/OpenSimulationInterface
  
0.6-beta (2015-07-27)
--------------------
  - made output to be more compact by removing extra empty lines and
    not moving member comments before the member but keeping it after
    the member instead
     * these changes lead into need of enabling JAVADOC_AUTOBRIEF
  - added steps for enabling the filter in Doxygen in this file

0.5-beta (2014-11-16)
--------------------
  - fixed enum ending to have semicolon to have proper enum syntax
    in struct (thanks to m47iast for pointing this out)

0.4-beta (2013-08-29)
--------------------
  - 'classified' proto2cpp and updated documentation to make the
     script itself Doxygen compatible
  - changed all print statements to print() functions
     * 64-bit Python v3.3.1 running on 64-bit Windows 7 Home Premium
       did not automatically convert print statements to print()
       functions but instead raised a syntax error
  - made a change so that .proto files are converted before printing
    and other files are printed to stdout as is
     * this allows using the filter with multiple file types
     
0.3-alpha (2013-01-29)
--------------------
  - moved .proto file parsing logic to another function
  - added comments to the file
  
0.2-pre-alpha (2012-06-15)
--------------------
  - added support for enums

0.1-pre-alpha (2012-06-13)
--------------------
  - initial version


Copyright
=========

Version 0.7-beta -
------------------
Extensions for Open Simulation Interface - License MIT

Version 0.7-beta
----------------
Copyright (C) 2016 Regents of the University of California https://github.com/vgteam/vg

Version 0.1-beta  - 0.6-beta 
----------------------------
Copyright (C) 2012-2015 Timo Marjoniemi https://sourceforge.net/p/proto2cpp/wiki/Home/
