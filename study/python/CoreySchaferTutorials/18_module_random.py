#!/usr/bin/env python3

"""
    Random Module
        - Generate pseudo-random numbers
        - Use Secrets module for security purposes or cryptography
"""
import random


# Random method: Return a random value(0 <= r < 1)
value = random.random()
print(value)

# Randint method: Return a random integer(a <= r <= b)
value = random.randint(1, 6)
print(value)

# Uniform method: Return a random floating point value(a <= r <= b)
value = random.uniform(1, 2)
print(value)

# Choice method
greetings = ['Hello', 'Hi', 'Hey', 'Howdy', 'Hola']
value = random.choice(greetings)
print(value + ', Young!')

# Choices method - Simulate a Roulette
colors = ['Red', 'Black', 'Green']
results = random.choices(colors, weights=[18, 18, 2], k=10)
print(results)

# Shuffle a Deck of Cards and select 5 cards from the Deck
deck = list(range(1, 53))
random.shuffle(deck)
hand = random.sample(deck, k=5)
print(hand)
