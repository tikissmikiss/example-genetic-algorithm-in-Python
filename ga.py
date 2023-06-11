# -*- coding: utf-8 -*-
# Path: ga.py


from algorithms.genetics import GeneticAlgorithmV3, GeneticAlgorithmV1, GeneticAlgorithmV2, GeneticAlgorithmV4, \
    GeneticAlgorithmV5, GeneticAlgorithmV6
from utils import args, separator_line

args = args()

if int(args['version']) == 1:
    ga = GeneticAlgorithmV1(vars=args)
elif int(args['version']) == 2:
    ga = GeneticAlgorithmV2(vars=args)
elif int(args['version']) == 3:
    ga = GeneticAlgorithmV3(vars=args)
elif int(args['version']) == 4:
    ga = GeneticAlgorithmV4(vars=args)
elif int(args['version']) == 5:
    ga = GeneticAlgorithmV5(vars=args)
elif int(args['version']) == 6:
    ga = GeneticAlgorithmV6(vars=args)
else:
    raise Exception("Error: Invalid version")

ga.run()

print(f"{separator_line()}\nEnd of version {ga.version}\n")
ga.print_stats()
print(f"{separator_line()}\n")
