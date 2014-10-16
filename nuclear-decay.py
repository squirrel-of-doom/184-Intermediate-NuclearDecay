###
# Challenge #184 [Intermediate] Radioactive decay
# from r/dailyprogrammer
# http://www.reddit.com/r/dailyprogrammer/comments/2jcgej/10152014_challenge_184_intermediate_radioactive/
# 
# Author: squirrel-of-doom
# Date:   2014-10-16
###

print ""
print "Challenge #184 [Intermediate] Radioactive decay"
print "-----------------------------------------------"

# Read input file
with open('nuclear.in') as infile:
    inlines = infile.read().splitlines()
    
try:
    T_MAX = int(inlines[0])
    decay_chain = inlines[1].split('->')
    lambdas = {}
    for lambda_line in inlines[2:]:
        entry = lambda_line.split(': ')
        lambdas[entry[0]] = float(entry[1])
    # Do we have lambdas for all the nuclei?
    for nucleus in decay_chain:
        if not nucleus in lambdas:
            raise StandardError
except:
    print "Bad input!"
    exit(1)

# Output values read
print "Read T_MAX: %d" % T_MAX
print "Read decay chain: %s" % decay_chain
print "Read lambdas: %s" % lambdas
print

# Initialize population vector
N_initial = 1000000
N_vector = {nucleus: 0 for nucleus in decay_chain}
N_vector[decay_chain[0]] = N_initial
print "Initial population: %s" % N_vector

# Main loop
decay_chain.reverse()
stable_nucleus = decay_chain[0]
timestep = 0
while timestep < T_MAX:
    # Go up the decay chain and propagate the products down
    for nucleus in decay_chain:
        if nucleus != stable_nucleus:
            delta = int(N_vector[nucleus] * lambdas[nucleus])
            N_vector[daughter] += delta
            N_vector[nucleus]  -= delta
        daughter = nucleus
    timestep += 1

# Output
print "Population at t = %d:" % T_MAX
decay_chain.reverse()
N_total = 0
for nucleus in decay_chain:
    print "%s: %d (%2.3f%%)" % (nucleus, N_vector[nucleus], 100.0 * N_vector[nucleus] / N_initial)
    N_total += N_vector[nucleus]
# Sanity check
if N_total != N_initial:
    print "Whoops, you seem to have lost some atoms!"
else:
    print "Done!"
    