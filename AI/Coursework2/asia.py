import sys,math,time
from pgmpy.models import BayesianModel
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination
from GibbsSamplingWithEvidence import GibbsSampling
from prettytable import PrettyTable
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
print("\n\n\n\n\nAsia Bayesian Network\n------------------------\n")

######################
### CREATE MODEL
######################
asiaNetwork = BayesianModel([('asia','tub'),
                             ('tub','either'),
                             ('smoke','lung'),
                             ('lung','either'),
                             ('either','xray'),
                             ('either','dysp'),
                             ('smoke','bron'),
                             ('bron','dysp'),])

# non dependant variables first
cpdAsia = TabularCPD(variable='asia', variable_card=2,values=[[0.99], [0.01]])
cpdSmoking = TabularCPD(variable='smoke', variable_card=2,values=[[0.5], [0.5]])

# dependant on only one thing
cpdTub = TabularCPD(variable='tub', variable_card=2,values=[[0.99, 0.95], [0.01, 0.05]],evidence=['asia'], evidence_card=[2])
cpdLung = TabularCPD(variable='lung', variable_card=2,values=[[0.99, 0.9],[0.01, 0.1]],evidence=['smoke'], evidence_card=[2])
cpdBron = TabularCPD(variable='bron', variable_card=2,values=[ [0.7, 0.4],[0.3, 0.6]],evidence=['smoke'], evidence_card=[2])

cpdEither = TabularCPD(variable='either', variable_card=2,
                        values=[[0.999, 0.001, 0.001, 0.001],
                                [0.001, 0.999, 0.999, 0.999]],
                        evidence=['tub', 'lung'],
                        evidence_card=[2, 2])

cpdDysp = TabularCPD(variable='dysp', variable_card=2,
                        values=[[0.9, 0.2, 0.3, 0.1],
                                [0.1, 0.8, 0.7, 0.9]],
                        evidence=['bron', 'either'],
                        evidence_card=[2, 2])

cpdXRay = TabularCPD(variable='xray', variable_card=2,values=[[0.95, 0.02],[0.05, 0.98]],evidence=['either'], evidence_card=[2])

# add the cpds to the network
asiaNetwork.add_cpds(cpdAsia,cpdSmoking,cpdTub,cpdLung,cpdBron,cpdEither,cpdDysp,cpdXRay)
# check network is valid
asiaNetwork.check_model()


######################
### GET ARGUMENTS
######################

# arguments
params = {}
possibleArgs = ["--evidence","--query","--exact","--gibbs","-N","--ent"]
arguments = sys.argv

# create a dictionary of all our arguments based off the command line input
for currentArg in possibleArgs:
    if(currentArg in arguments):
        thisArgsValues = []
        i = arguments.index(currentArg)+1
        while(i < len(arguments) and arguments[i][0] != "-"):
            thisArgsValues.append(arguments[i])
            i += 1
        params[currentArg] = thisArgsValues

#print(params)

### Finding evidence from args
evidence = {}
if("--evidence" in params):
    for item in params["--evidence"]:
        evidence[item.split("=")[0]] = int(item.split("=")[1])

######################
### INFERENCE
######################

# calculate exact posterior probabilites
exactInference = VariableElimination(asiaNetwork)
approxInference = GibbsSampling(asiaNetwork)

if("--query" in params):
    print("\nExact Inference")
    for query in params["--query"]:
        q = exactInference.query(variables=[query], evidence=evidence)
        print(q[query])

if("--gibbs" in params):
    print("\nApprox Inference")
    if("-N" in params):
        samples = approxInference.sample(size=int(params["-N"][0]),evidence=evidence)
    else:
        # use defalut value of 500
        samples = approxInference.sample(size=500,evidence=evidence)

    for query in params["--query"]:
        p1 = sum(samples[query])/len(samples[query])
        p0 = 1 - p1
        results = PrettyTable([str(query),str("phi(") + str(query) + str(")")])
        results.add_row([str(query) + "_0",str(round(p0,4))])
        results.add_row([str(query) + "_1",str(round(p1,4))])
        print(results)

if("--ent" in params):
    print("\nCross Entropy")
    if("--query" in params):
        crossEntropy = 0

        # only doing this once speeds things up
        samples = approxInference.sample(size=int(params["-N"][0]),evidence=evidence)
        for query in params["--query"]:
            exactQueryValues = exactInference.query(variables=[query], evidence=evidence)[query].values
            approxQueryValues = sum(samples[query])/len(samples[query])
            # this is doing the formula at the bottom of the second page
            crossEntropy -= (1-approxQueryValues)*math.log(exactQueryValues[0]) + (approxQueryValues)*math.log(exactQueryValues[1])

        print("\nThe cross entropy is : ",crossEntropy)
    else:
        print("\nCannot perform cross entropy with no --query params\n")
        sys.exit()
