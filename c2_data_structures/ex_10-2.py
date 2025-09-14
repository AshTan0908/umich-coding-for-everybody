# Write a program to read through the mbox-short.txt and figure out the
# distribution by hour of the day for each of the messages. You can pull the hour
# out from the 'From ' line by finding the time and then splitting the string a
# second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted
# by hour as shown below.

# Desired Output:
# 04 3
# 06 1
# 07 1
# 09 2
# 10 3
# 11 6
# 14 1
# 15 2
# 16 4
# 17 2
# 18 1
# 19 1

# Opening the file
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
counts = dict()
hours_list = list()

# Searching for the time, taking just hour and creating the list
for line in handle:
    if not line.startswith("From ") :
        continue
    a = line.split()
    time = a[5]
    hour = time[:2]
    hours_list.append(hour)

# Creating histogram
for hr in hours_list:
    counts[hr] = counts.get(hr, 0) + 1

# Finding the top ten most frequent timings(hours)
lst = list()
for k, v in counts.items():
    newtup = (k, v)
    lst.append(newtup)

lst = sorted(lst)

# Printing it out
for k, v in lst[:12] :
    print(k, v)
