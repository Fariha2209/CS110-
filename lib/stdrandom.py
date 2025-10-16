"""
The stdrandom library defines functions related to pseudo-random numbers.
"""

import random


def seed(i=None):
    """
    Seed the random number generator as hash(i), where i is an int. If i is None, then seed using
    the current time or, quoting the help page for random.seed(), "an operating system specific
    randomness source if available."
    """
    random.seed(i)


def uniformInt(lo, hi):
    """
    Return an integer chosen uniformly from the range [lo, hi).
    """
    return random.randrange(lo, hi)


def uniformFloat(lo, hi):
    """
    Return a number chosen uniformly from the range [lo, hi).
    """
    return random.uniform(lo, hi)


def bernoulli(p=0.5):
    """
    Return True with probability p and False with probability 1 - p.
    """
    return random.random() < p


def binomial(n, p=0.5):
    """
    Return the number of heads in n coin flips, each of which is heads with probability p.
    """
    heads = 0
    for i in range(n):
        if bernoulli(p):
            heads += 1
    return heads


def gaussian(mu=0.0, sigma=1.0):
    """
    Return a float according to a standard Gaussian distribution with the given mean (mu) and
    standard deviation (sigma).
    """
    return random.gauss(mu, sigma)


def discrete(a):
    """
    Return an integer from a discrete distribution a (ie, return i with probability a[i]).
    """
    r = uniformFloat(0.0, sum(a))
    subtotal = 0.0
    for i in range(len(a)):
        subtotal += a[i]
        if subtotal > r:
            return i


def exp(lambd):
    """
    Return a float from an exponential distribution with rate lambd.
    """
    return random.expovariate(lambd)


def choice(a):
    """
    Returns a random element from the array a.
    """
    return random.choice(a)


def sample(a, k):
    """
    Returns a list of k unique random elements from the array a.
    """
    return random.sample(a, k)


def shuffle(a):
    """
    Shuffle array a.
    """
    random.shuffle(a)


# Unit tests the library.
def _main():
    import sys
    import stdio
    seed(1)
    n = int(sys.argv[1])
    a = [1, 2, 3, 4, 5]
    for i in range(n):
        stdio.writef(" %2d ", uniformInt(10, 100))
        stdio.writef("%8.5f ", uniformFloat(10.0, 99.0))
        stdio.writef("%5s ", bernoulli())
        stdio.writef("%5s ", binomial(100, .5))
        stdio.writef("%8.5f ", gaussian(9.0, .2))
        stdio.writef("%2d ", discrete([.5, .3, .1, .1]))
        stdio.writef("%8.5f ", exp(3.0))
        stdio.writef(" %2d ", choice(a))
        stdio.writef("%s ", sample(a, 3))
        shuffle(a)
        stdio.writef("%s ", a)
        stdio.writeln()


if __name__ == "__main__":
    _main()
