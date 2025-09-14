# Write code using find() and string slicing (see section 6.10) to extract the
# number at the end of the line below. Convert the extracted value to a floating
# point number and print it out.

#Desired Output: 0.8475

text = "X-DSPAM-Confidence:    0.8475"

index_0 = text.find('0')

find_num = text[index_0:]
x = float(find_num)
print(x)
