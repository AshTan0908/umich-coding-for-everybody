# Write a program to read through the mbox-short.txt and figure out who has sent
# the greatest number of mail messages. The program looks for 'From ' lines and
# takes the second word of those lines as the person who sent the mail. The
# program creates a Python dictionary that maps the sender's mail address to a
# count of the number of times they appear in the file. After the dictionary is
# produced, the program reads through the dictionary using a maximum loop to find
# the most prolific committer.

#Desired Output = cwen@iupui.edu 5

# Opening the file
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
counts = dict()
email_list = list()

# Searching for the email addresses and creating the list
for line in handle:
    if not line.startswith("From "):
        continue
    a=line.split()
    emails=a[1]
    email_list.append(emails)
#print(email_list)

# Creating histogram
for email in email_list:
    counts[email] = counts.get(email,0) + 1

# Finding the most repeated email address
top_email = None
top_email_count = None

for key, value in counts.items():
    if top_email is None or value > top_email_count:
        top_email = key
        top_email_count = value

# Printing it out
print(top_email, top_email_count)
