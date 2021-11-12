import random
from game import constants
from game.action import Action
from game.point import Point

class RandomizeActions(Action):

    def execute(self, cast):
        if random.randint(0, 50) != 50:
            return
        
        for artifact in cast["artifact"]:
            x = random.randint(0, constants.MAX_X - 1)
            y = random.randint(1, constants.MAX_Y - 1)
            position = Point(x, y)
            artifact.set_position(position)


        
            
            # artifacts = cast["artifact"]
            # for artifact in artifacts:
            #     artifact.set_postion(position)


    