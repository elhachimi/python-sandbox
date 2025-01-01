import random

# Sample data
names = [
    "Alice",
    "Bob",
    "Charlie",
    "David",
    "Eve",
    "Frank",
    "Grace",
    "Hannah",
    "Ivy",
    "Jack",
    "Karen",
    "Leo",
    "Mona",
    "Nina",
    "Oscar",
    "Paul",
    "Quincy",
    "Rachel",
    "Steve",
    "Tina",
    "Uma",
    "Victor",
    "Wendy",
    "Xander",
    "Yara",
    "Zane",
    "Aaron",
    "Bella",
    "Cody",
    "Diana",
]
heights = [random.randint(150, 200) for _ in range(30)]  # Heights in cm
weights = [random.randint(50, 100) for _ in range(30)]  # Weights in kg
surf_levels = [random.randint(1, 10)
               for _ in range(30)]  # Surf levels from 1 to 10

# Generate the text file
with open("users_compaire.txt", "w") as file:
    file.write("Name,Height(cm),Weight(kg),Surf Level\n")
    for i in range(30):
        file.write(f"{names[i]},{heights[i]},{weights[i]},{surf_levels[i]}\n")

print("users_compaire.txt file has been generated.")
