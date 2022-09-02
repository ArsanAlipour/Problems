import random


N_QUEENS = 4
POPULATION_SIZE = 200
MUTATION_RATE = 0.8
EPOCH = 200



def initial_population(population_size:int, n:int) -> list:
    population_list = []
    for i in range(population_size):
        new_member = []
        for j in range(n):
            new_member.append(random.randint(1,n))
        new_member.append(0)
        population_list.append(new_member)
    return population_list



def cross_ower(population_list:list) -> list:
    for i in range(0,len(population_list), 2):
        child1 = population_list[i][:len(population_list[i])//2] + population_list[i+1][len(population_list[i])//2 : len(population_list[i])-1] + [0]
        child2 = population_list[i+1][:len(population_list[i])//2] + population_list[i][len(population_list[i])//2 : len(population_list[i])-1] + [0]
        population_list.append(child1)
        population_list.append(child2)
    return population_list



def mutate(population_list:list, mutation_rate:float, n:int) -> list:
    choosen_ones = [i for i in range(len(population_list)//2,len(population_list))]
    for i in range(len(population_list)//2):
        new_random = random.randint(0,(len(population_list)//2)-1)
        choosen_ones[new_random], choosen_ones[i] = choosen_ones[i], choosen_ones[new_random]
    choosen_ones = choosen_ones[:int(len(choosen_ones)*mutation_rate)]
    for i in choosen_ones:
        selected_ch = random.randint(0,n-1)
        new_value = random.randint(1,n)
        population_list[i][selected_ch] = new_value
    
    return population_list




def fitness(population_list:list, n:int) -> list:
    conflict = 0
    lenght = len(population_list)
    for i in range(lenght):
        j = 0
        conflict = 0
        while j < n:
            l = j+1
            while l < n:
                if population_list[i][j] == population_list[i][l]:
                    conflict += 1
                if abs(j-l) == abs(population_list[i][j] - population_list[i][l]):
                    conflict += 1
                l+=1
            j+=1
        population_list[i][n] = conflict
    for i in range(lenght):
        _min = i
        for j in range(i, lenght):
            if population_list[j][n] < population_list[_min][n]:
                _min = j
        population_list[i], population_list[_min] = population_list[_min], population_list[i]
    return population_list


def main():
    population = initial_population(POPULATION_SIZE, N_QUEENS)
    population = fitness(population, N_QUEENS)
    if population[0][N_QUEENS] == 0:
        print(f"solution found: {population[0][:N_QUEENS]}")
    else:
        for i in range(EPOCH):
            print("------------------------------------------------------------")
            print(f"Epoch {i+1}")
            population = cross_ower(population)
            population = mutate(population, MUTATION_RATE, N_QUEENS)
            population = fitness(population, N_QUEENS)
            population = population[:len(population)//2]
            if population[0][N_QUEENS] == 0:
                print(f"solution found: {population[0][:N_QUEENS]}")
                break
            else:
                print(f"best solution so far: {population[0][:N_QUEENS]} ---> {population[0][N_QUEENS]}")


if __name__ == "__main__":
    main()
