#!/usr/env/python3
import sys
from Card import Card
from Vector import cross
import math

# class to handle Serpent datacard
class MCNPDataCard(Card):
    def __init__(self, card_string):
        Card.__init__(self, card_string)


# class to handle Serpent Transforms
# Class to handle MCNP Transform Cards
class MCNPTransformCard(MCNPDataCard):
    id = 0 # transform card number
    angle_form = 0 # 0 is radians, 1 is degrees
    # spatial shift
    shift = [0.,0.,0.]
    # default basis vector
    v1 = [1.,0.,0.]
    v2 = [0.,1.,0.]
    v3 = [0.,0.,1.]

    def __init__(self, card_string):
        MCNPDataCard.__init__(self, card_string)
        self.__process_string()

    def __process_string(self):
        tokens = self.text_string.split()
        print(self.text_string)
