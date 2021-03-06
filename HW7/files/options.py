#From Class Discussion 8/26/2014
from __future__ import division
import sys,re,random,math
import numpy as np
sys.dont_write_bytecode = True

class Options:
  #Globals
  debug = False
  seed = 1
  era_lives = 3
  a12_test = 0.6
  
  #MaxWalkSat options
  mws_prob = 0.75
  mws_maxTries = 500
  mws_maxChanges = 500
  mws_threshold = .001
  mws_slices = 10
  
  #Simulated Annealing options
  sa_kmax = 500
  sa_cooling = .6
  
  #Genetic Algorithm options
  ga_gen_list = [10]
  ga_pop_size = 50
  ga_crossover = .6
  
  #Differential Evolution options
  de_max     = 100   # number of repeats 
  de_np      = 100   # number of candidates
  de_f       = 0.2  # extrapolate amount
  de_cf      = 0.3   # prob of cross-over 
  de_epsilon = 0.01
  
  #Particle Swarm Optimization options
  pso_phi1 = 2.8
  pso_phi2 = 1.3
  pso_n = 30
  pso_w = 1
  pso_epsilon = 0.000001
  #pso_repeats = 1000
  pso_repeats = 1000
  
  def printGlobals(self):
    print "Seed:", self.seed, "Lives: ", self.era_lives
    print "A12test:", self.a12_test
    