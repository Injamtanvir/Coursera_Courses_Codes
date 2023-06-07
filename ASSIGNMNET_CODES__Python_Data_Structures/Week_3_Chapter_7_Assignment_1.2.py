#InjamTanvir
'''
Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
X-DSPAM-Confidence:    0.8475
Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below.
Do not use the sum() function or a variable named sum in your solution.
You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.
'''


count = 0
total = 0

fname = input("Please Enter file name: ")
try:
    fhandle = open(fname)

except:
    print("Sorry!!\nPlease re-enter the file name.")
    quit()

for line in fhandle:
    if line.startswith("X-DSPAM-Confidence:"):    #Find which line startswith "X-DSPAM-Confidence:"
        f = line.find(":")                        #Then find the :
        float_number = float(line[f+1:])          #Then get float value which is after :
        count = count + 1                         #Then count every similar line
        total = total + float_number              #Then add floating values in total

avrg = total / count
print(f"Average spam confidence: {avrg}")
