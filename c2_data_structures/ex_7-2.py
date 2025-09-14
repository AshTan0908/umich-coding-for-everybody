# Write a program that prompts for a file name, then opens that file and reads
# through the file, looking for lines of the form: X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from each of the lines
# and compute the average of those values and produce an output as shown below.
# Do not use the sum() function or a variable named sum in your solution.
# You can download the sample data at http://www.py4e.com/code3/mbox-short.txt
# when you are testing below enter mbox-short.txt as the file name.

# Desired Output = Average spam confidence: 0.7507185185185187

# Use the file name mbox-short.txt as the file name

# Opening the file
fname = input("Enter file name: ")
fh = open(fname)
count = 0
total = 0

# Searching for "stuff" in the file (count value unneccesary)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    count = count + 1
    # print(line.rstrip())
    # Taking out just the numbers and leaving out X-DSPAM-Confidence:
    num = line.find('0')
    num = float(line[num:])
    total = num + total
    # Adding them all (sum is 20.2694)

# Done
print('Average spam confidence:',total/count)
