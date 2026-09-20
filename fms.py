def register_freelancer(name):
    return "Freelancer " + name + " registered"

print(register_freelancer("Aisha"))

#version 1.1
def register_freelancer(name, skill):
    return name + " registered with skill " + skill

print(register_freelancer("Aisha", "Python"))
