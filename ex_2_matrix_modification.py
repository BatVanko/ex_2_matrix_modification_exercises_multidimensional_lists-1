size = int(input())

matrix = []

for _ in range (size):
    matrix.append([int(x) for x in input().split(' ')])

command = input()
while command != 'END':
    commands = command.split(' ')
    com = commands[0]
    row = int(commands[1])
    col = int(commands[2])
    value = int(commands[3])

    if len(commands) == 4  and  0 <= row < len(matrix) and 0<= col < len(matrix):
        if com == 'Add':
            matrix[row][col] += value
        elif com == 'Subtract':
            matrix[row][col] -= value
        else:
            print("Invalid coordinates")

    else:
        print("Invalid coordinates")
    command = input()

for i in range (size):
    print(*matrix[i], sep = ' ')





