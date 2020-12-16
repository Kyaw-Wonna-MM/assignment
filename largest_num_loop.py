largest = 0
smallest = None
print('Before: ',largest)
print('Before: ',smallest)


for i in [23,234234,12,6656,234234,745678994,144]:
    if smallest == None:
        smallest = i
    elif i < smallest:
        smallest = i
        print(f'Now i is {i} and smallest is {smallest}')
    if i > largest:
        largest = i
        print(f'Now i is {i} and Largest is {largest}')

print('---------------end loop--------------------------')
   
        
print(f'After Loop largest is {largest}')
print(f'After Loop smallest is {smallest}')


