#N1
print('\t\t\tExercise 1\n')
strings = list()
dct = {}

for n in range(int(input('Enter quantity of strings: '))):
  string = input(f'N{n+1} string: ')
  strings.append(string)
  if string not in dct:  dct[string] = 1
  else: dct[string] += 1

print('\nQuantity of different strings is', len(dct), '\nThe numbers of occurrences of each string: ', '; '.join([str(dct[string]) for string in dct]))






#N2
def bigger_Is_greater(s):
    x, y = len(s) - 1, len(s) - 1
    while s[x] <= s[x-1] and x > 0:   
        x -= 1
    if x <= 0:   return print('No answer!')
    while s[x-1] >= s[y]:
        y -= 1
    s[y], s[x-1] = s[x-1], s[y]
    s[x:] = reversed(s[x:])
    return print('The smallest lexicographically higher string: ', ''.join(s))

print('\n\n\t\t\tExercise 2\n')
for n in range(int(input('Enter quantity of strings: '))):
    string = list(input(f'\nN{n+1} string: '))
    bigger_Is_greater(string)






#N3
def bomber_man(n, grid):
    n = int(input('Firstly enter seconds of explosion after planting bombs: '))
    if n > 3: n = 3
    row = int(input('Secondly enter quantity of rows: '))
    column = int(input('Then enter quantity of columns: '))
    print(f'\nNow fill grid({row}x{column}):')
    grid = [ list(input()) for _ in range(row) ]
    planted = [column * [0] for _ in range(row)]
    for i in range(row):
        for j in range(column):
            if grid[i][j] == 'O' or grid[i][j] == 'o': planted[i][j] = 2
    sec = 1
    while n > sec:
        sec += 1
        if sec % 2 == 1:
            bomb = [column * [False] for _ in range(row)]
            for i in range(row):
                for j in range(column):  
                    planted[i][j] -= 1       
                    if planted[i][j] == 0:   
                        bomb[i][j] = True
                        if i > 0: bomb[i-1][j] = True
                        if i < row-1: bomb[i+1][j] = True
                        if j > 0: bomb[i][j-1] = True
                        if j < column-1: bomb[i][j+1] = True
            for i in range(row):
                for j in range(column):
                    if bomb[i][j]: planted[i][j] = 0
        else:
            for i in range(row):
                for j in range(column):
                    if planted[i][j] < 0: planted[i][j] = 3
                    else: planted[i][j] -= 1
    for i in range(row):
        for j in range(column):
            if planted[i][j] != 0: grid[i][j] = 'O'
            else: grid[i][j] = '.'
    print(f'\n\nThe grid after {n} seconds:')
    print('\n'.join(map(lambda g: ''.join(g), grid)))

print('\n\n\t\t\tExercise 3\n')
t, g = 0, []
bomber_man(t, g)