# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 08:36:04 2016

@author: adam
"""

import random
global niches

#hierarchical dictionary flow
T = {
    "mine" : {"enrichment", "reactor:hwr"},
    "enrichment" : {"fuel_fab:uo2", "fuel_fab:triso", "reactor:hwr"},
    "fuel_fab" : {"reactor:lwr", "reactor:htgr", "reactor:rbmk", "reactor:pb"},
    "fuel_fab:uo2" : {"reactor:lwr", "reactor:htgr", "reactor:rbmk"},
    "fuel_fab:triso" : {"reactor:pb"},
    "fuel_fab:mox" : {"reactor:fr", "reactor:lwr", "reactor:htgr", "reactor:rbmk"},
    "reactor" : {"storage", "separations", "repository"},
    "reactor:fr" : {"storage", "separations", "repository"},
    "reactor:lwr" : {"storage", "separations", "repository"},
    "reactor:hwr" : {"storage",  "repository"},
    "reactor:htgr" : {"storage", "separations", "repository"},         
    "reactor:rbmk" : {"storage", "separations", "repository"},         
    "reactor:pb" : {"storage", "repository"},         
    "storage" : {"separations", "repository"},
    "storage:wet" : {"separations", "repository"},  
    "storage:dry" : {"separations", "repository"}, 
    "storage:interim" : {"separations", "repository"},        
    "separations" : {"enrichment", "reactor:hwr", "fuel_fab:mox"},
    "repository" : {None},          
    }

#randomniche generates a set of possible nodes along a path of niches
#to change start point add new string in argument

def random_niches(max_niches, choice="mine", niches=None):
    """Generates a randomized list of niches of the nuclear fuel cycle.
    
    Parameters
    ----------
        max_niches : int
            The maximum number of niches desired by the user, the total number
            of generated niches does not have to reach this number.
        choice : str
            If desired the starting point of the list of niches can be set. 
            Preset to the natural starting point of "mine"
        niches : None
            This will be set to be a list at the beginning of the function and
            will contain the chosen niches.
            
    Returns
    -------
        niches : list
            List of connected niches that model the steps of the full nuclear
            fuel cycle.
    """
    if niches is None:
        niches = []
    niches.append(choice)
    if max_niches == 1:
        return niches
    else:
        choice = random.sample(T[choice], 1)[0]
        if choice is None:
            return niches
        return random_niches(max_niches-1, choice, niches)
