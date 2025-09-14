sum = 0
count = 0
for thing in [100000, 9, 85, 89, 60, 24, 62, 276]:
    count = count + 1
    sum = sum + thing
    print(count,')', thing,'-', sum, 'Average =', sum/count)
print('Done')
