"""
prices = [10, 20, 30]

total = 0
for price in prices:
    total += price
    print(f"Total: {total}")
"""

"""
for x in range (4):
    for y in range(3):
        print(f'({x}, {y})')
"""

"""
numbers = [5, 2, 5, 2, 2]
for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)
"""
"""
names = ['John', 'Bob', 'Mosh', 'Sarah', 'MoMo']
print(names[2:4])
print(names)
"""

"""
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for row in matrix:
    for item in row:
        print(item)
    """


numbers = [2, 2, 4, 6, 3, 4, 6, 1]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
        print(uniques)

