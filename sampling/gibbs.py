"""
https://www.jonki.net/entry/2019/05/05/142536
just rewrote this
"""

import random

# the conditional probability of going shopping
probs = {
    'mother|daughter':  5/6,
    'father|daughter':  1/6,

    'mother|son':       5/8,
    'father|son':       3/8,

    'daughter|mother':  2/3,
    'son|mother':       1/3,

    'daughter|father':  2/5,
    'son|father':       3/5
}

def sample_one(probs):
    z = sum(probs.values())
    remaining = random.uniform(0, z)
    for k, v in probs.items():
        remaining -= v
        if remaining <= 0:
            return k

# let's figure out the joint probability through the conditional probability
# sampling
def gibbs():
    samples = {
        'mother,daughter': 0,
        'mother,son': 0,
        'father,daughter': 0,
        'father,son': 0
    }

    A = 'mother'
    B = 'daughter'

    N = 10000

    for _ in range(N):
        # get one sample from a probability distribution conditioned on mother
        _A = sample_one(
               {k:v for k, v in probs.items() if k.endswith(B)}).split('|')[0]
        # get one sample from a probability distribution conditioned on daughter
        _B = sample_one(
               {k:v for k, v in probs.items() if k.endswith(A)}).split('|')[0]
        samples["{},{}".format(_A, _B)] += 1

    print("Result:")

    for k, v in samples.items():
        print("P({}) = {:.3f} ({}/{})".format(k, v/N, v, N))


if __name__ == "__main__":
    gibbs()
