"""
function_library.py
Bat City Collective — Personal Developer Toolkit
Student Name: Lucia Santillan Arriaga
UTSA ID: vep381
Section: 901/902 Programming 1
Date: 02/24/2026

Reusable helper functions for Lab 2.2:
- flip_coin() → returns 'HEADS' or 'TAILS'
- roll_d20() → returns integer 1–20
- check_percentage(chance) → returns True/False based on percentage chance
"""

import random


def flip_coin():
    """
    Simulate a coin flip.
    Returns 'HEADS' or 'TAILS'.
    """
    return 'HEADS' if random.randint(0, 1) == 1 else 'TAILS'


def roll_d20():
    """
    Simulate a 20-sided die roll.
    Returns an integer from 1 to 20.
    """
    return random.randint(1, 20)


def check_percentage(chance):
    """
    Returns True if a random number 1–100 is <= chance.
    Used for hazard probability checks.
    """
    return random.randint(1, 100) <= chance
