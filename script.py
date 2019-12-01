import fontforge
import glob
import os

fonts = ['simsun.ttc']
#names = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

folder_name = "Kanji_images\\"
for font in fonts:
	fontname = font.split('.')[0]
	os.mkdir(folder_name)
	F = fontforge.open(font)
	#for name in F:
	for i in range(13312, 19894):
		#first_letter_equivalent_int = ord(name[0])
		#if first_letter_equivalent_int >47 and first_letter_equivalent_int < 58 :
		#if name in names :
		F[i].export(folder_name+str(i)+".bmp", 63)

