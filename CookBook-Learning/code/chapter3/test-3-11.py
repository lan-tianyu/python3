import random

values = [1, 2, 3, 4, 5, 6]
print(random.choice(values), random.choice(values), random.choice(values),
      random.choice(values), random.choice(values))

print(random.sample(values, 2), random.sample(values, 2),
      random.sample(values, 3), random.sample(values, 3))

print(random.shuffle(values), values)
print(random.shuffle(values), values)

print(random.randint(0, 10), random.randint(0, 10), random.randint(0, 10),
      random.randint(0, 10), random.randint(0, 10), random.randint(0, 10),
      random.randint(0, 10), random.randint(0, 10), random.randint(0, 10),
      random.randint(0, 10), random.randint(0, 10), random.randint(0, 10),
      random.randint(0, 10), random.randint(0, 10), random.randint(0, 10))

print(random.random(), random.random(), random.random(),
      random.random(), random.random(), random.random())
      
print(random.getrandbits(200))

print(random.seed(), random.seed(1234), random.seed(b'bytedata'))