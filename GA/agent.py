from PIL import Image # type: ignore

class Agent:
    """
    Agents for the Genetic Algorithm
    Contains a success evaluation and a list of actions
    """
    def __init__(self,ipath="/images/square.png",actions=[],pos=(0,0)):
        #image to display
        self.img=Image.open(ipath)

        #success evaluation
        self.pro=0
        
        #list of actions
        self.actions=actions

        self.pos=pos

    def move_left(self):
        (x,y)=self.pos
        self.pos=(x-5,y)
    def move_right(self):
        (x,y)=self.pos
        self.pos=(x+5,y)
    def move_up(self):
        (x,y)=self.pos
        self.pos=(x,y+5)
    def move_down(self):
        (x,y)=self.pos
        self.pos=(x,y-5)
