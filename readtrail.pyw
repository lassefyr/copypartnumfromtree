import tkinter as tk
import os, glob
import re

def sortBy(f):
	s=re.findall("(\\w+)$",f)
	return (int(s[0]) if s else -1,f)
    
def copyToClip():
	myInt = 0
	filename = "trail.txt"
	folder = "c:/PTC/work/"
	latestFile = glob.glob(folder+filename+".*")
	useThis = max(latestFile, key=sortBy)		
	#print(useThis)
	
	try:
		myFile = open(useThis, "r")
		fileOpened = True
	except IOError:
		fileOpened = False
		print("File "+useThis+" Not found!")
	
	for line in reversed(list(myFile)):
		mystring = line.rstrip()
		suffix1 = ".PRT"
		suffix2 = ".ASM"
	
		latestFile = glob.glob(folder+filename+".*")
		#print(latestFile)
		
		if mystring.endswith(suffix1):
			#print(line[1:], end = '')
			putToClip(line[1:])
			break
			
		if mystring.endswith(suffix2):
			#print(line[1:], end = '')
			putToClip(line[1:])
			break
			
		if myInt > 20:
			break
		myInt+=1
	
	if( fileOpened ):
		myFile.close()
		fileOpened = False
		

def putToClip( mystring ):
#	r = Tk()
#	r.withdraw()
	frame.clipboard_clear()
	frame.clipboard_append(mystring)
#	this.update() # now it stays on the clipboard after the window is closed


root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button(frame, 
                   text="QUIT", 
                   fg="red",
                   command=quit)
button.pack(side=tk.LEFT)
slogan = tk.Button(frame,
                   text="CopyToClipboard",
                   command=copyToClip)
slogan.pack(side=tk.LEFT)



root.attributes("-topmost", True)
#root.withdraw()
root.mainloop()





