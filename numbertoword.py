from collections import *
from Tkinter import *
from tkColorChooser import *
import json
import random
#from webcolors import *
#import colordata
# -*- coding: utf-8 -*- 


def displayColors():
	MAX_ROWS = 36
	FONT_SIZE = 10 # (pixels)

	COLORS = ['snow', 'ghost white', 'white smoke', 'gainsboro', 'floral white', 'old lace',
	    'linen', 'antique white', 'papaya whip', 'blanched almond', 'bisque', 'peach puff',
	    'navajo white', 'lemon chiffon', 'mint cream', 'azure', 'alice blue', 'lavender',
	    'lavender blush', 'misty rose', 'dark slate gray', 'dim gray', 'slate gray',
	    'light slate gray', 'gray', 'light grey', 'midnight blue', 'navy', 'cornflower blue', 'dark slate blue',
	    'slate blue', 'medium slate blue', 'light slate blue', 'medium blue', 'royal blue',  'blue',
	    'dodger blue', 'deep sky blue', 'sky blue', 'light sky blue', 'steel blue', 'light steel blue',
	    'light blue', 'powder blue', 'pale turquoise', 'dark turquoise', 'medium turquoise', 'turquoise',
	    'cyan', 'light cyan', 'cadet blue', 'medium aquamarine', 'aquamarine', 'dark green', 'dark olive green',
	    'dark sea green', 'sea green', 'medium sea green', 'light sea green', 'pale green', 'spring green',
	    'lawn green', 'medium spring green', 'green yellow', 'lime green', 'yellow green',
	    'forest green', 'olive drab', 'dark khaki', 'khaki', 'pale goldenrod', 'light goldenrod yellow',
	    'light yellow', 'yellow', 'gold', 'light goldenrod', 'goldenrod', 'dark goldenrod', 'rosy brown',
	    'indian red', 'saddle brown', 'sandy brown',
	    'dark salmon', 'salmon', 'light salmon', 'orange', 'dark orange',
	    'coral', 'light coral', 'tomato', 'orange red', 'red', 'hot pink', 'deep pink', 'pink', 'light pink',
	    'pale violet red', 'maroon', 'medium violet red', 'violet red',
	    'medium orchid', 'dark orchid', 'dark violet', 'blue violet', 'purple', 'medium purple',
	    'thistle', 'snow2', 'snow3',
	    'snow4', 'seashell2', 'seashell3', 'seashell4', 'AntiqueWhite1', 'AntiqueWhite2',
	    'AntiqueWhite3', 'AntiqueWhite4', 'bisque2', 'bisque3', 'bisque4', 'PeachPuff2',
	    'PeachPuff3', 'PeachPuff4', 'NavajoWhite2', 'NavajoWhite3', 'NavajoWhite4',
	    'LemonChiffon2', 'LemonChiffon3', 'LemonChiffon4', 'cornsilk2', 'cornsilk3',
	    'cornsilk4', 'ivory2', 'ivory3', 'ivory4', 'honeydew2', 'honeydew3', 'honeydew4',
	    'LavenderBlush2', 'LavenderBlush3', 'LavenderBlush4', 'MistyRose2', 'MistyRose3',
	    'MistyRose4', 'azure2', 'azure3', 'azure4', 'SlateBlue1', 'SlateBlue2', 'SlateBlue3',
	    'SlateBlue4', 'RoyalBlue1', 'RoyalBlue2', 'RoyalBlue3', 'RoyalBlue4', 'blue2', 'blue4',
	    'DodgerBlue2', 'DodgerBlue3', 'DodgerBlue4', 'SteelBlue1', 'SteelBlue2',
	    'SteelBlue3', 'SteelBlue4', 'DeepSkyBlue2', 'DeepSkyBlue3', 'DeepSkyBlue4',
	    'SkyBlue1', 'SkyBlue2', 'SkyBlue3', 'SkyBlue4', 'LightSkyBlue1', 'LightSkyBlue2',
	    'LightSkyBlue3', 'LightSkyBlue4', 'SlateGray1', 'SlateGray2', 'SlateGray3',
	    'SlateGray4', 'LightSteelBlue1', 'LightSteelBlue2', 'LightSteelBlue3',
	    'LightSteelBlue4', 'LightBlue1', 'LightBlue2', 'LightBlue3', 'LightBlue4',
	    'LightCyan2', 'LightCyan3', 'LightCyan4', 'PaleTurquoise1', 'PaleTurquoise2',
	    'PaleTurquoise3', 'PaleTurquoise4', 'CadetBlue1', 'CadetBlue2', 'CadetBlue3',
	    'CadetBlue4', 'turquoise1', 'turquoise2', 'turquoise3', 'turquoise4', 'cyan2', 'cyan3',
	    'cyan4', 'DarkSlateGray1', 'DarkSlateGray2', 'DarkSlateGray3', 'DarkSlateGray4',
	    'aquamarine2', 'aquamarine4', 'DarkSeaGreen1', 'DarkSeaGreen2', 'DarkSeaGreen3',
	    'DarkSeaGreen4', 'SeaGreen1', 'SeaGreen2', 'SeaGreen3', 'PaleGreen1', 'PaleGreen2',
	    'PaleGreen3', 'PaleGreen4', 'SpringGreen2', 'SpringGreen3', 'SpringGreen4',
	    'green2', 'green3', 'green4', 'chartreuse2', 'chartreuse3', 'chartreuse4',
	    'OliveDrab1', 'OliveDrab2', 'OliveDrab4', 'DarkOliveGreen1', 'DarkOliveGreen2',
	    'DarkOliveGreen3', 'DarkOliveGreen4', 'khaki1', 'khaki2', 'khaki3', 'khaki4',
	    'LightGoldenrod1', 'LightGoldenrod2', 'LightGoldenrod3', 'LightGoldenrod4',
	    'LightYellow2', 'LightYellow3', 'LightYellow4', 'yellow2', 'yellow3', 'yellow4',
	    'gold2', 'gold3', 'gold4', 'goldenrod1', 'goldenrod2', 'goldenrod3', 'goldenrod4',
	    'DarkGoldenrod1', 'DarkGoldenrod2', 'DarkGoldenrod3', 'DarkGoldenrod4',
	    'RosyBrown1', 'RosyBrown2', 'RosyBrown3', 'RosyBrown4', 'IndianRed1', 'IndianRed2',
	    'IndianRed3', 'IndianRed4', 'sienna1', 'sienna2', 'sienna3', 'sienna4', 'burlywood1',
	    'burlywood2', 'burlywood3', 'burlywood4', 'wheat1', 'wheat2', 'wheat3', 'wheat4', 'tan1',
	    'tan2', 'tan4', 'chocolate1', 'chocolate2', 'chocolate3', 'firebrick1', 'firebrick2',
	    'firebrick3', 'firebrick4', 'brown1', 'brown2', 'brown3', 'brown4', 'salmon1', 'salmon2',
	    'salmon3', 'salmon4', 'LightSalmon2', 'LightSalmon3', 'LightSalmon4', 'orange2',
	    'orange3', 'orange4', 'DarkOrange1', 'DarkOrange2', 'DarkOrange3', 'DarkOrange4',
	    'coral1', 'coral2', 'coral3', 'coral4', 'tomato2', 'tomato3', 'tomato4', 'OrangeRed2',
	    'OrangeRed3', 'OrangeRed4', 'red2', 'red3', 'red4', 'DeepPink2', 'DeepPink3', 'DeepPink4',
	    'HotPink1', 'HotPink2', 'HotPink3', 'HotPink4', 'pink1', 'pink2', 'pink3', 'pink4',
	    'LightPink1', 'LightPink2', 'LightPink3', 'LightPink4', 'PaleVioletRed1',
	    'PaleVioletRed2', 'PaleVioletRed3', 'PaleVioletRed4', 'maroon1', 'maroon2',
	    'maroon3', 'maroon4', 'VioletRed1', 'VioletRed2', 'VioletRed3', 'VioletRed4',
	    'magenta2', 'magenta3', 'magenta4', 'orchid1', 'orchid2', 'orchid3', 'orchid4', 'plum1',
	    'plum2', 'plum3', 'plum4', 'MediumOrchid1', 'MediumOrchid2', 'MediumOrchid3',
	    'MediumOrchid4', 'DarkOrchid1', 'DarkOrchid2', 'DarkOrchid3', 'DarkOrchid4',
	    'purple1', 'purple2', 'purple3', 'purple4', 'MediumPurple1', 'MediumPurple2',
	    'MediumPurple3', 'MediumPurple4', 'thistle1', 'thistle2', 'thistle3', 'thistle4',
	    'gray1', 'gray2', 'gray3', 'gray4', 'gray5', 'gray6', 'gray7', 'gray8', 'gray9', 'gray10',
	    'gray11', 'gray12', 'gray13', 'gray14', 'gray15', 'gray16', 'gray17', 'gray18', 'gray19',
	    'gray20', 'gray21', 'gray22', 'gray23', 'gray24', 'gray25', 'gray26', 'gray27', 'gray28',
	    'gray29', 'gray30', 'gray31', 'gray32', 'gray33', 'gray34', 'gray35', 'gray36', 'gray37',
	    'gray38', 'gray39', 'gray40', 'gray42', 'gray43', 'gray44', 'gray45', 'gray46', 'gray47',
	    'gray48', 'gray49', 'gray50', 'gray51', 'gray52', 'gray53', 'gray54', 'gray55', 'gray56',
	    'gray57', 'gray58', 'gray59', 'gray60', 'gray61', 'gray62', 'gray63', 'gray64', 'gray65',
	    'gray66', 'gray67', 'gray68', 'gray69', 'gray70', 'gray71', 'gray72', 'gray73', 'gray74',
	    'gray75', 'gray76', 'gray77', 'gray78', 'gray79', 'gray80', 'gray81', 'gray82', 'gray83',
	    'gray84', 'gray85', 'gray86', 'gray87', 'gray88', 'gray89', 'gray90', 'gray91', 'gray92',
	    'gray93', 'gray94', 'gray95', 'gray97', 'gray98', 'gray99']

	row = 0
	col = 0
	for color in COLORS:
		print color
		e = Label(root, text=color, background=color, 
		    font=(None, -FONT_SIZE))
		e.grid(row=row, column=col, sticky=E+W)
		row += 1
		if (row > 36):
			row = 0
			col += 1

def numberToThreeTuple(number):
	'''
	Takes a 10-20 digit integer as input and parses it to either permutations of three digits or random
	one, two, and three digit triples, according to its divisibility by three. 
	Decision: if it is not divisible by three, 
	Working example: 1234567891
	'''
	string = str(number)
	length = len(string)
	excess = string[-(length%3)] #excess means the string is not divisible by three
	colorTriple = []
	triple = ''
	if excess:
		for i in range(2): #calculates what to divide the original thing, completely arbitrary
			digit = string[length//(i+3)] #3 is arbitrary just to make it interesting i guess...
			triple += digit
		colorTriple.append(int(triple))
	i = 0
	j = i+2 #splice it by threes
	while j <= length-1:
		strcandidate =  string[i:(j+1)] #takes three digits of each number
		candidate = int(strcandidate)
		while candidate > 255: #if the number is above the range, arbitrarily divide by three and take its floor
			candidate = candidate//3
		colorTriple.append(int(candidate))
		j += 1
		i += 1
	while not len(colorTriple) % 3 == 0: #this loop makes the length of colorTriple always a factor of three, so that we can compute complete three-tuples without numbers left over 
		colorTriple.append(colorTriple[len(colorTriple)//5])
	return colorTriple

#print numberToThreeTuple(12345678912344678)

def numberToColor(num):
	'''
	Input: nothing really, the input is dictated by the tkinter module, so this input is a dummy
	Output: a list of three-tuples representing rgb traits respectively
	'''
	master_input = entry.get()
	print master_input
	triples = numberToThreeTuple(master_input)
	#triples = numberToThreeTuple(num)
	#convert it to rgb values, especially if more than 9!
	#convert list into three-tuples
	three_tuples = []
	i = 0
	lst = []
	for i in range(len(triples)):
		if (i+1) % 3 == 0:
			lst.append(triples[i])
			three_tuples.append(tuple(lst))
			del lst[:]
		else:
			lst.append(triples[i])
	results.insert(END, 'the corresponding colors are:')
	results.insert(END, three_tuples)
	#now match the three-tuples to their names in colors!
	with open('colordata.json', 'r') as f:
		colors_list = json.load(f) #saves json file as a listb for python access
	# print colors_list[2]['rgb']['b']
	# print len(colors_list)
	print three_tuples
	color_results = []
	for i in range(len(three_tuples)):
		for j in range(len(colors_list)):
			# print 'tuples', three_tuples[i][0]
			# print 'color', colors_list[j]
			if three_tuples[i][0] == colors_list[j]['rgb']['r']:
				#only one condition is met
				if len(color_results) <= len(three_tuples):
					color_results.append(colors_list[j]['name'])
				if three_tuples[i][1] == colors_list[j]['rgb']['g']:
					#Two conditions are met
					if len(color_results) <= len(three_tuples):
						color_results.append(colors_list[j]['name'])
					if three_tuples[i][2] == colors_list[j]['rgb']['b']:
						#all three conditions are met!
						print colors_list[j]['name']
						if len(color_results) <= len(three_tuples):
							color_results.append(colors_list[j]['name'])
	results.insert(END, color_results)
	if len(color_results) < len(three_tuples):
		results.insert(END, 'The colors generated are not named!! Use the color picker to visualize the colors!')
				#else:
					#print colors_list[j]['name']
	return color_results

	#if all three numbers dont match because not all numbers are named, return at least one number that matches!

# print numberToColor(6786806875447)

#GUI stuff

root = Tk()
root.title("Number to Color!")

explanation = Text(root, height=1,width=30,bg='peach puff')
explanation.pack()
explanation.insert(CURRENT, "Welcome to Number to Color!")
logo = PhotoImage(file="guiimage.ppm")
entry = Entry(root) #create input 
photo = Label(root,image=logo).pack(side=TOP)
#entry.grid(row = 0, column = 1)
color = entry.bind('<Return>', numberToColor) #runs program when user presses enter!
entry.pack()
results = Text(root, height=10, width=35, bg='peach puff')
results.pack()

#text.insert(END, '\n{}\n'.format(color))

numbertocolor = Button(root, text='Submit', command=numberToColor)
numbertocolor.pack(side=RIGHT)
#buttons in GUI
allcolors = Button(root, text='View ALL colors', command=displayColors)
allcolors.pack(side=LEFT)

root.mainloop()



