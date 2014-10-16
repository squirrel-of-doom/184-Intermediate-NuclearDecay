###
# Challenge #184 [Intermediate] Radioactive decay
# from r/dailyprogrammer
# http://www.reddit.com/r/dailyprogrammer/comments/2jcgej/10152014_challenge_184_intermediate_radioactive/
# 
# Author: squirrel-of-doom
# Date:   2014-10-16
# File:   nuclear-decay-random.py
###

import random

print ""
print "Challenge #184 [Intermediate] Radioactive decay"
print "-----------------------------------------------"

# This version differs from nuclear-decay.py: 
# There, the decay was just applied to the system as a bulk
# Here, we will modify the sample individually based on probabilities

# Read input file
with open('nuclear.in') as infile:
    inlines = infile.read().splitlines()
    
try:
    T_MAX = int(inlines[0])
    decay_chain = inlines[1].split('->')
    lambdas = {lambda_line.split(': ')[0]: float(lambda_line.split(': ')[1]) for lambda_line in inlines[2:]}
except:
    print "Bad input!"
    exit(1)

# Output values read
print "Read T_MAX: %d" % T_MAX
print "Read decay chain: %s" % decay_chain
print "Read lambdas: %s" % lambdas
print

# Initialize successor lookup and helper vars
mother_nucleus = decay_chain[0]
daughter_nucleus = dict(zip(decay_chain[:-1], decay_chain[1:]))

# Initialize population
N_population = 10000
all_nuclei = [mother_nucleus] * N_population
nucleus_count = dict(zip(decay_chain, [0] * len(decay_chain)))
nucleus_count[mother_nucleus] = N_population

# Run simulation
timestep = 0
while timestep < T_MAX:
    all_nuclei = [daughter_nucleus[nucleus] if random.random() < lambdas[nucleus] else nucleus for nucleus in all_nuclei]
    timestep += 1

# Output
print "Population at t = %d:" % T_MAX
N_total = 0
for nucleus in decay_chain:
    nucleus_count = all_nuclei.count(nucleus)
    print "%s: %d (%2.3f%%)" % (nucleus, nucleus_count, 100.0 * nucleus_count / N_population)
    N_total += nucleus_count
# Sanity check
if N_total != N_population:
    print "Whoops, you seem to have lost some atoms!"
else:
    print "Done!"
    