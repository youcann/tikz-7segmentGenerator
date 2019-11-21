#!/usr/bin/env python3
import re

def writeSevenSegToFile(name,segments):
	f=open("template.tikz", "r")
	lines=f.read().splitlines(True)
	f.close()
	
	for seg,val in segments.items():
		for i,line in enumerate(lines):
			lines[i]=line.replace('<segment'+seg+'>','\on' if val else '\off')
			
	g=open("out/out_"+name+".tikz",'w')
	g.writelines(lines)
	g.close()

if __name__ == "__main__":
	#write "7"
	writeSevenSegToFile("7",segments={"A":1,"B":1,"C":1,"D":0,"E":0,"F":0,"G":0})
