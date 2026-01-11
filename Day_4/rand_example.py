import random

america_st = ["tx", "nv", "co", "ca", "in", "ny", "nj"]

# option 1
print(random.choice(america_st))

# option 2

random_index = random.randint(0, 6)
print(america_st[random_index])
