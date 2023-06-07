#InjamTanvir
'''
Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method.
The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list.
When the program completes, sort and print the resulting words in python sort() order as shown in the desired output.
You can download the sample data at http://www.py4e.com/code3/romeo.txt
'''


fname = input("Enter the file name: ")
try:
    fh = open(fname)
except:
    print("Sorry!!\nPlease re-enter the file name.")
    quit()

lst = list()

for line in fh:
    word= line.rstrip().split()
    for elem in word:
        if elem in lst:     #For each word on each line check to see if the word is already in the list and if not append it to the list.
            continue
        else :
            lst.append(elem)
lst.sort()
print(lst)
