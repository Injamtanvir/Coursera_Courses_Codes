#InjamTanvir
'''
Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages.
The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.
The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file.
After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
'''


name = input("Please Enter file name:")

try:
    handle = open(name)
except:
    print("Sorry!!\nPlease re-enter the file name.")
    quit()

count = 0
hold_name = list()

for line in handle:
    if not line.startswith("From:"):
        continue
    line = line.split()   #If line startswith From:
    hold_name.append(line[1])  #append line[1] word in hold_name to store the word

counts = dict()      #Create a empty Dictionaries
for word in hold_name:
    counts[word] = counts.get(word, 0) + 1   # Idiom: retrieve / create / update
                                             # If the word already in dict() then add +1, If not in dict() by default it took 0.

bigcount = None
bigword = None   #By Default
for word, count in sorted(counts.items()):      #Key, value pair takes by .items() function  #Sorted function sort the key value pair
    if bigcount is None or count > bigcount:
        bigcount = count
        bigword = word

print(bigword, bigcount)
