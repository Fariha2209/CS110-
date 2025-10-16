# Simulates a coin flip by writing "Heads" or "Tails" as standard output.

import stdio
import stdrandom

result = "Heads" if stdrandom.bernoulli() else "Tails"
stdio.writeln(result)
