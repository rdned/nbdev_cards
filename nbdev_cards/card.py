"""A simple API for creating and using playing cards"""

# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/00_card.ipynb.

# %% auto 0
__all__ = ['spades', 'hearts', 'diamonds', 'clubs', 'suits', 'ranks', 'Card']

# %% ../nbs/00_card.ipynb 2
from fastcore.utils import *

# %% ../nbs/00_card.ipynb 4
spades = "\u2660"
hearts = "\u2665"
diamonds = "\u2666"
clubs = "\u2663"

# %% ../nbs/00_card.ipynb 7
suits = [clubs, diamonds, hearts, spades]
ranks = [None, "A"] + [str(x) for x in range(2,11)] + ['J', 'Q', 'K']

# %% ../nbs/00_card.ipynb 16
class Card:
    "A playing card"
    def __init__(self, 
                 suit: int, # An index into suits
                 rank: int  # An index into ranks
                 ):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{ranks[self.rank]}, {suits[self.suit]}"
    
    __repr__ = __str__


# %% ../nbs/00_card.ipynb 19
@patch
def __eq__(self: Card, a: Card):
    return (self.suit, self.rank)==(a.suit, a.rank)

# %% ../nbs/00_card.ipynb 23
@patch
def __lt__(self: Card, a: Card):
    return (self.suit, self.rank)<(a.suit, a.rank)

# %% ../nbs/00_card.ipynb 26
@patch
def __gt__(self: Card, a: Card):
    return (self.suit, self.rank)>(a.suit, a.rank)
