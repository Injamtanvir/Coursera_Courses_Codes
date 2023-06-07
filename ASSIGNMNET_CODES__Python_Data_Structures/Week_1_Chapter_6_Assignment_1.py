#InjamTanvir
'''
Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below.
Convert the extracted value to a floating point number and print it out.
text = "X-DSPAM-Confidence:    0.8475   " getout 0.8475 from there
'''


text = "X-DSPAM-Confidence:    0.8475   "

colon_position = text.find(":")
After_colon_Position = text[colon_position+1:]
length_strip = After_colon_Position.strip()   #Remove all tghe spaces before and after
print(length_strip)  #There's a Bug the answer will come as a string
#print(type(length_strip))    #If you wish remove the # and check


#ANOTHER WAY

text = "X-DSPAM-Confidence:    0.8475   "

colon_position = text.find(":")
After_colon_Position = text[colon_position+1:]
print(float(After_colon_Position))   #For this no need to remove spaces cause float function automatically find the floating values and shows them without spaces.