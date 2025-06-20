import random
from PIL import Image # type: ignore
from agent import Agent

class Eugenics:
    """
    Artificially selecting the fittest members of each generation for reproduction and purging the outliers
    """

    def __init__(self,ipath='images/square.png',population=20,actionNum=20):
        self.kids=[]

        for i in range(population):
            acts=[]
            for i in range(actionNum):acts.append(random.randint(1,4))
            self.kids.append(Agent(ipath,actions=acts,pos=(400,400)))

    #sort agents by success eval
    #TODO: should probably test this
    def sort(agents:list[Agent]):
        agents.sort(key=lambda agent: agent.pro, reverse=True)

    #mixes attributes of best agents to create new agent
    def procreate(agents): 
        kid=[]
        coinflip=0
        numParents=len(agents)

        for i in range(numParents):
            coinflip=random(0,numParents)
            kid.append(agents[coinflip].actions[i])

        return kid

    def evolve(self,agents,ipath,numParents,addNum,addRate):
        children=[]
        parents=[]
        size=len(agents)

        self.sort(agents)

        #prevent overflow in procreate
        if numParents>=size:parents=agents
        #take specified number of parents from agents
        #TODO: test this
        else: parents=agents[:numParents]

        #make new generation
        for child in children:
            acts=self.procreate(parents)
            if addRate: 
                for i in range(addNum): acts.append(random.randint(1,4))
            children.append(Agent(ipath=ipath,actions=acts,pos=(400,400)))

