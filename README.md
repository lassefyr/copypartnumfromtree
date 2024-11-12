# readtrail.pyw
Python script that copies the selected partnumber from modeltree to clipboard. 

Start by doubleclicking the readtrail.pyw (assumes that you have python 3x)

This script reads the latest 20 lines from your trail file (you must set the path to your own trail file location)
filename = "trail.txt"
folder = "c:/PTC/mytrailfileLocation/" <- change this.

Select .prt or .asm from the modeltree and press "CopyToClipboard". Number should be copied to clipboard.

# find_harness_parts.py
This is a user specific script to find harness parts in Creo. The script will scan each .prt file and see whether it is a harness template. All harness parts and their description (user parameter) will be printed on the console in csv-format.

Usage:
* Save your design to a backup directory (save backup in Creo).
* Run the script in that directory.

