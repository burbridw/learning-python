members = []

with open("family.csv") as file:
    for line in file:
        name, role, age = line.rstrip().split(",")
        member = {"name": name, "role": role, "age": age}
        members.append(member)

print(members)