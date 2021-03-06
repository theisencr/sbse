#From Class Discussion 8/26/2014
from __future__ import division
import sys,re,random,math
import numpy as np
sys.dont_write_bytecode = True

kmax = 5000
cooling = .6

#Structure from SA Lecture
def say(x): 
  sys.stdout.write(str(x)); sys.stdout.flush()
        
rand = random.random

class Kursawe:
  smin = -5
  smax = 5
  XVar = [random.uniform(smin, smax) for i in range (0, 3)]
  XVarMax = XVar
  eMax = 0
  eMin = 0
  a = 0.8
  b = 3
  
  def Energy(self):
    X = self.XVar
    f1 = np.sum([-10*math.exp(-0.2*(np.sqrt(X[i]**2+X[i]**2))) for i in range (0, 3-1)])
    f2 = np.sum([math.fabs(X[i])**self.a + 5*np.sin(X[i])**self.b for i in range (0, 3)])
    return (math.fabs(f1-f2) - self.eMin) / (self.eMax - self.eMin)
    
  def RawEnergy(self):
    X = self.XVar
    f1 = np.sum([-10*math.exp(-0.2*(np.sqrt(X[i]**2+X[i]**2))) for i in range (0, 3-1)])
    f2 = np.sum([math.fabs(X[i])**self.a + 5*np.sin(X[i])**self.b for i in range (0, 3)])
    return math.fabs(f1-f2)

  def Neighbor(self):
    self.XVar[random.randint(0, 2)] = random.uniform(self.smin, self.smax)
    
  def Chaos(self):
    self.XVar[0] = random.uniform(self.smin, self.smax)
    self.XVar[1] = random.uniform(self.smin, self.smax)
    self.XVar[2] = random.uniform(self.smin, self.smax)
    
  def Baseline(self, numRuns):
    self.Chaos()
    self.eMax = self.eMin = self.RawEnergy()
    runs = 1
    while runs < numRuns:   
      self.Neighbor()
      eNew = self.RawEnergy()
      if eNew > self.eMax: #find largest difference               
        self.eMax = eNew
        self.XVarMax = self.XVar
        #print self.XVarMax, eNew
      if eNew < self.eMin: #find smallest difference  
        self.eMin = eNew
        #print 'Min: ', self.XVar, eNew
      runs += 1
    print 'Baseline: ', self.eMin, ', ', self.eMax
    
  def __init__(self):
    print 'Initializing Kursawe...'
    self.Baseline(10000)
    self.XVar = self.XVarMax
    print 'Initialized.'
  
#Structure from SA Lecture
def main():
  sa = Kursawe()
  XVarBest = sa.XVar
  eBest = e = 1
  print 'start energy: ', eBest           
  k = 1
  say(int(math.fabs(eBest-1)*100))
  say(' ')
  while k < kmax:   
    sa.Neighbor()
    eNew = sa.Energy()
    if eNew < eBest:               
      eBest = eNew
      XVarBest = list(sa.XVar)
      say('!')
	  
    if eNew < e:                 
      e = eNew     
      say('+')       
    #Probability Check from SA Lecture
    elif math.exp(-1*(eNew-e)/(k/kmax**cooling)) < random.uniform(0,1):
    #P function should be between 0 and 1
    #more random hops early, then decreasing as time goes on
      sa.Chaos()
      say('?')        
    say('.')
    k = k + 1
    if k % 50 == 0 and k != kmax:
      print ''
      say(int(math.fabs(eBest-1)*100))
      say(' ')

  print '\nFound best - e: ', eBest
  print 'Variables: ', XVarBest[0], ', ', XVarBest[1], ', ', XVarBest[2]
  
main()
