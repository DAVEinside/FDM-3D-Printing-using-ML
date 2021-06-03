import pygad
import numpy

lst = []
def fitness_func(solution, solution_idx):
    a = solution[0]
    b = solution[1]
    c = solution[2]
    d = solution[3]

    output = -3.0500731235557 + (27.305807814185 * a) - (0.02568795511004 * b) + \
             (0.01473071848973 * c) - (0.024766290222257 * d) - (0.21964743016038 * a * b) \
             + (0.075 * a * c) - (0.49107142857143 * a * d) + (0.00027777777777778 * b * c) \
             + (0.0034722222222222 * b * d) - (0.001875 * c * d) - (27.170294216721 * a * a) \
             + (0.00063682469472212 * b * b) - (0.00029314051823067 * c * c) + \
             (0.010446794026458 * d * d)
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

a = solution[0]
b = solution[1]
c = solution[2]
d = solution[3]

output = -3.0500731235557 + (27.305807814185 * a) - (0.02568795511004 * b) + \
             (0.01473071848973 * c) - (0.024766290222257 * d) - (0.21964743016038 * a * b) \
             + (0.075 * a * c) - (0.49107142857143 * a * d) + (0.00027777777777778 * b * c) \
             + (0.0034722222222222 * b * d) - (0.001875 * c * d) - (27.170294216721 * a * a) \
             + (0.00063682469472212 * b * b) - (0.00029314051823067 * c * c) + \
             (0.010446794026458 * d * d)

print(output)

pygad.GA.plot_result(self=ga_instance)