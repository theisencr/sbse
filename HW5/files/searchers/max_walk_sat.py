#Structure from SA Lecture
import sys,re,random,math
sys.dont_write_bytecode = True
  
from options import *
from utils import *
from analyzer import *

myOpt = Options()

class MWS:
  debug = False
  
  def say(self, x): 
    if self.debug:
      sys.stdout.write(str(x)); sys.stdout.flush()

  def specificRun(self, probability, klass):
    fon = klass
    XVarBest = fon.XVar
    eBest = e = 1
    eNew = 1  
    k = 1
    temp = []
    self.say(int(math.fabs(eBest-1)*100))
    self.say(' ')
    
    analyze = Analyzer()
    stop = False
    
    for i in xrange(myOpt.mws_maxTries):
      fon.Chaos()
      for j in xrange(myOpt.mws_maxChanges):
        eNew = fon.Energy()
        if(eNew < myOpt.mws_threshold or stop == True):
          #% means found a solution and quit
          self.say('%')
          eBest = eNew
          XVarBest = list(fon.XVar)
          temp.append(eNew)
          #print xtile(temp,lo=0, hi=1, width=25,show=" %1.5f")
          return eBest, XVarBest
        else:
          #modify random part of solution
          if probability < random.uniform(0,1):
            fon.Neighbor()
            self.say('+')
          #maximize for some random
          else:
            fon.BestNeighbor()
          self.say('.')
          temp.append(eNew)
          if (i+1)*(j+1) % 40 == 0 and len(temp) != 0:
            #print ''
            self.say(int(math.fabs(eNew-1)*100))
            self.say(' ')
            #print xtile(temp,lo=0, hi=1, width=25,show=" %1.5f")
            #stop = analyze.EraStop(temp)
            temp = []
      return -1, XVarBest
      
  def run(self, klass):
    theBest = -1
    valid = False
    eBest, XVarBest = self.specificRun(myOpt.mws_prob, klass)
    if eBest == -1:
      print 'No Best Found for prob = ', myOpt.mws_prob
      self.say('')
    else:
      theBest = eBest
      valid = True
    return theBest, valid
  
  def printOptions(self):
    print "MaxWalkSat Options:"
    print "Prob:", myOpt.mws_prob
    print "MaxTries:", myOpt.mws_maxTries, "MaxChanges", myOpt.mws_maxChanges
    print "Threshold:", myOpt.mws_threshold, "Slices:", myOpt.mws_slices 