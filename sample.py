# https://esa.github.io/pygmo2/tutorials/moo_moead.html

from pygmo import *
udp = dtlz(prob_id = 1)
pop = population(prob = udp, size = 105)
algo = algorithm(moead(gen = 100))
for i in range(10):
    pop = algo.evolve(pop)
    print(udp.p_distance(pop))