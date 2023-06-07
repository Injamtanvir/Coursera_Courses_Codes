#InjamTanvir
'''
Write a program that prompts for a file name, then opens that file and reads through the file, and print the contents of the file in upper case.
Use the file words.txt to produce the output below.
You can download the sample data at http://www.py4e.com/code3/words.txt
'''


fname = input("Please enter the file name: ")
try:
    handle = open(fname)
except:
    print("Sorry!!\nPlease re-enter the file name.")
    quit()


for line in handle:     #Catches every line.
    new_line = line.rstrip().upper()  #If we didn't use rstrip() it will catches \n from the files-lines and add extra spaces on the output.
    print(new_line)                   #upper() function uses to write the letter in upper format.
