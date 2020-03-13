'''
Simple script for running the Covid-19 agent-based model
'''

import sciris as sc

print('Importing...')
sc.tic()
import covid_seattle as covid # Or: import covid_abm as covid
sc.toc()

do_plot = 1
do_save = 0
verbose = 1

print('Making sim...')
sc.tic()
sim = covid.Sim()
sim.set_seed(1)

print('Running...')
sim.run(verbose=verbose)
if do_plot:
    sim.plot(do_save=do_save)