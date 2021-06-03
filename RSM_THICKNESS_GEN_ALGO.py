import pygad
import numpy

lst = []
def fitness_func(solution, solution_idx):
    A = solution[0]
    B = solution[1]
    C = solution[2]
    D = solution[3]

    output = 7.56366 + (-21.7779 * A) + (-0.0921383 * B) + (-0.0314286 * C) + (-0.116071 * D) + (0.323602 * A*B) + \
             (0.0785714 * A*C) + (0.446429 * A*D) + (0.000133333 * B*C) + (-0.000555556 * B*D) + (0.0015 * C*D)


    if output > 0 and output < 0.03560803481675263 :
        lst.append(solution)
    if output < 0:
        fitness = -100000
    else:
        fitness = 1.0 / (numpy.abs(output - 0) + 0.000001)
    return fitness


fitness_function = fitness_func

num_generations = 500
num_parents_mating = 4

sol_per_pop = 10
num_genes = 4

parent_selection_type = "sus"
keep_parents = 1

crossover_type = "single_point"
#gene_space=[{'low': 0.12, 'high': 0.4}, {'low': 0, 'high': 90}, {'low': 0, 'high': 100},{'low': 2, 'high': 10}]

#gene_space = [[0.12, 0.19, 0.26, 0.33],[0,22.5,45,67.5,90],[25,50,75,100],[2,4,6,8,10]]

mutation_type = "random"
mutation_percent_genes = 10

ga_instance = pygad.GA(num_generations=num_generations,
                       num_parents_mating=num_parents_mating,
                       fitness_func=fitness_function,
                       sol_per_pop=sol_per_pop,
                       init_range_low=0,
                       init_range_high=100,
                       num_genes=num_genes,
                       parent_selection_type=parent_selection_type,
                       keep_parents=keep_parents,
                       gene_space = [[0.12, 0.19, 0.26, 0.33],[22.5,45,67.5,90],[25,50,75,100],[2,4,6,8,10]],
                       crossover_type=crossover_type,
                       mutation_type=mutation_type,
                       mutation_num_genes=4,
                       mutation_percent_genes=mutation_percent_genes,
                       allow_duplicate_genes=False)

ga_instance.run()

solution, solution_fitness, solution_idx = ga_instance.best_solution()
print("Parameters of the best solution : "+ str(solution))
print("Fitness value of the best solution = {solution_fitness}".format(solution_fitness=solution_fitness))

#print(len(lst))
#print(lst)

A = solution[0]
B = solution[1]
C = solution[2]
D = solution[3]

output = 7.56366 + (-21.7779 * A) + (-0.0921383 * B) + (-0.0314286 * C) + (-0.116071 * D) + (0.323602 * A*B) + \
             (0.0785714 * A*C) + (0.446429 * A*D) + (0.000133333 * B*C) + (-0.000555556 * B*D) + (0.0015 * C*D)

print(output)

pygad.GA.plot_result(self=ga_instance)