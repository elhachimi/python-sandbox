def extract_name(line: str) -> str:
    return line.split(",")[0]


with open("users.txt", "r") as file:
    lines = file.readlines()

with open("users_compaire.txt", "r") as file:
    lines_compaire = file.readlines()

names = list(map(extract_name, lines[1:]))
names_compaire = list(map(extract_name, lines_compaire[1:]))


print(names_compaire)

with open("users_intersection.txt", "w") as file:
    file.write("Name,Height(cm),Weight(kg),Surf Level\n")
    i = 0
    for name in names:
        if name in names_compaire:
            if i < len(lines):
                file.write(lines[i + 1])
        i += 1
