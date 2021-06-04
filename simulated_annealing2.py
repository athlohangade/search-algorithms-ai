import random
def SimulatedAnnealing(matrix, start, M, N) :

    current_state = start
    best_so_far = current_state
    probability_list = [0.25, 0.75]
    probability = 0.5
    step = 100000           # Number of times the loop should run 
    i = 0                   # No. of operations applied to the current_state
    transition_of_current_state = []

    while i != 8 and step > 0:

        pos = (current_state[0] - 1, current_state[1])
        if (pos[0] >= 0) :
            if matrix[pos[0]][pos[1]] > matrix[current_state[0]][current_state[1]] :
                current_state = pos
                transition_of_current_state.append(current_state)
                i = 0
                step -= 1
                if matrix[pos[0]][pos[1]] > matrix[best_so_far[0]][best_so_far[1]] :
                    best_so_far = pos
                continue
            else :
                x = random.choice(probability_list)
                if (x < probability) :
                    current_state = pos
                    transition_of_current_state.append(current_state)
                    i = 0
                    step -= 1
                    continue
        i += 1


        pos = (current_state[0] - 1, current_state[1] - 1)
        if (pos[0] >= 0 and pos[1] >= 0) :
            if matrix[pos[0]][pos[1]] > matrix[current_state[0]][current_state[1]] :
                current_state = pos
                transition_of_current_state.append(current_state)
                i = 0
                step -= 1
                if matrix[pos[0]][pos[1]] > matrix[best_so_far[0]][best_so_far[1]] :
                    best_so_far = pos
                continue
            else :
                x = random.choice(probability_list)
                if (x < probability) :
                    current_state = pos
                    transition_of_current_state.append(current_state)
                    i = 0
                    step -= 1
                    continue
        i += 1

        pos = (current_state[0], current_state[1] - 1)
        if (pos[1] >= 0) :
            if matrix[pos[0]][pos[1]] > matrix[current_state[0]][current_state[1]] :
                current_state = pos
                transition_of_current_state.append(current_state)
                i = 0
                step -= 1
                if matrix[pos[0]][pos[1]] > matrix[best_so_far[0]][best_so_far[1]] :
                    best_so_far = pos
                continue
            else :
                x = random.choice(probability_list)
                if (x < probability) :
                    current_state = pos
                    transition_of_current_state.append(current_state)
                    i = 0
                    step -= 1
                    continue
        i += 1


        pos = (current_state[0] + 1, current_state[1] - 1)
        if (pos[0] < M and pos[1] >= 0) :
            if matrix[pos[0]][pos[1]] > matrix[current_state[0]][current_state[1]] :
                current_state = pos
                transition_of_current_state.append(current_state)
                i = 0
                step -= 1
                if matrix[pos[0]][pos[1]] > matrix[best_so_far[0]][best_so_far[1]] :
                    best_so_far = pos
                continue
            else :
                x = random.choice(probability_list)
                if (x < probability) :
                    current_state = pos
                    transition_of_current_state.append(current_state) 
                    i = 0 
                    step -= 1
                    continue 
        i += 1


        pos = (current_state[0] + 1, current_state[1])
        if (pos[0] < M) :
            if matrix[pos[0]][pos[1]] > matrix[current_state[0]][current_state[1]] :
                current_state = pos
                transition_of_current_state.append(current_state) 
                i = 0 
                step -= 1
                if matrix[pos[0]][pos[1]] > matrix[best_so_far[0]][best_so_far[1]] :
                    best_so_far = pos
                continue
            else :
                x = random.choice(probability_list)
                if (x < probability) :
                    current_state = pos
                    transition_of_current_state.append(current_state) 
                    i = 0
                    step -= 1
                    continue
        i += 1

        pos = (current_state[0] + 1, current_state[1] + 1)
        if (pos[0] < M and pos[1] < N) :
            if matrix[pos[0]][pos[1]] > matrix[current_state[0]][current_state[1]] :
                current_state = pos
                transition_of_current_state.append(current_state) 
                i = 0
                step -= 1
                if matrix[pos[0]][pos[1]] > matrix[best_so_far[0]][best_so_far[1]] :
                    best_so_far = pos
                continue
            else :
                x = random.choice(probability_list)
                if (x < probability) :
                    current_state = pos
                    transition_of_current_state.append(current_state) 
                    i = 0
                    step -= 1
                    continue
        i += 1


        pos = (current_state[0], current_state[1] + 1)
        if (pos[1] < N) :
            if matrix[pos[0]][pos[1]] > matrix[current_state[0]][current_state[1]] :
                current_state = pos
                transition_of_current_state.append(current_state) 
                i = 0
                step -= 1
                if matrix[pos[0]][pos[1]] > matrix[best_so_far[0]][best_so_far[1]] :
                    best_so_far = pos
                continue
            else :
                x = random.choice(probability_list)
                if (x < probability) :
                    current_state = pos
                    transition_of_current_state.append(current_state) 
                    i = 0
                    step -= 1
                    continue
        i += 1


        pos = (current_state[0] - 1, current_state[1] + 1)
        if (pos[0] >= 0 and pos[1] < N) :
            if matrix[pos[0]][pos[1]] > matrix[current_state[0]][current_state[1]] :
                current_state = pos
                transition_of_current_state.append(current_state) 
                i = 0
                step -= 1
                if matrix[pos[0]][pos[1]] > matrix[best_so_far[0]][best_so_far[1]] :
                    best_so_far = pos
                continue
            else :
                x = random.choice(probability_list)
                if (x < probability) :
                    current_state = pos
                    transition_of_current_state.append(current_state) 
                    i = 0
                    step -= 1
                    continue
        i += 1

    '''
    print("Transition of CURRENT STATE :")
    for i in transition_of_current_state :
        print(i, end = " ")
    print("")
    '''

    print("Path :")
    for i in transition_of_current_state :
        print(i, end = " ")
        if i == best_so_far :
            break

    print("")
    print("Final Position :")
    print(best_so_far)
    return


M = 5       #No of rows
N = 8       #No of columns
'''
elevation_matrix = []
for i in range(0, M) :
    elevation_matrix.append([random.randint(1,9) for x in range(0,N)])# for j in range(0,5)] 
for i in range(0, M) :
    print(elevation_matrix[i])
print("Enter the position in the range (%d, %d):" %(M-1, N-1))
position = tuple(map(int, input().split()))
if position[0] >= M or position[1] >= N :
    exit("Enter a valid position!!!")
'''

elevation_matrix = []
elevation_matrix.append([1,6,3,3,4,7,5,5])
elevation_matrix.append([4,5,1,6,7,6,2,9])
elevation_matrix.append([7,3,1,2,1,8,1,9])
elevation_matrix.append([1,4,5,1,8,5,1,4])
elevation_matrix.append([2,5,4,4,7,8,2,8])
for i in range(0, M) :
    print(elevation_matrix[i])
print("Enter the position in the range (%d, %d):" %(M-1, N-1))
position = tuple(map(int, input().split()))
if position[0] >= M or position[1] >= N :
    exit("Enter a valid position!!!")

SimulatedAnnealing(elevation_matrix, position, M, N)
