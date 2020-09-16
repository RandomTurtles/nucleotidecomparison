
def print_mat(mat):
    for x in range(len(mat)):
        for y in range(len(mat[x])):
            print('{:6.2f}'.format(mat[x][y]), end = ' ')
        print()


if __name__ == '__main__':
    animal=[]
    with open("data") as f:
        for line in f:
            animal.append(line)

    animal_count = len(animal)
    base_length = len(animal[0])-1
    matrix = [[0] * animal_count for i in range(animal_count)]
    for i in range(0, animal_count):
        for j in range(i+1, animal_count):
            sum = 0
            for k in range(0, base_length):
                if animal[i][k] == animal[j][k]:
                    sum += 1
            matrix[i][j] = sum/base_length

    print_mat(matrix)
