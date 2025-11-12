import random
from game_data import data
one = random.choice(data)
name_one = one ["name"]
description_one = one["description"]
country_one = one["country"]
follower_one = one["follower"]
print(f"{name_one}, is a {description_one},from {country_one}")

two = random.choice(data)
name_two = two ["name"]
description_two = two["description"]
country_two = two["country"]
follower_two = two["follower"]
print(f"{name_two}, is a {description_two},from {country_two}")



