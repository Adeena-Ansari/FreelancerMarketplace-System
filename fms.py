def register_freelancer(name):
    return "Freelancer " + name + " registered"

print(register_freelancer("Aisha"))

#version 1.1
def register_freelancer(name, skill):
    return name + " registered with skill " + skill

print(register_freelancer("Aisha", "Python"))

#version2.0
def register_freelancer(name, skill, experience):
    return name + " registered with " + skill + " and " + str(experience) + " years experience"

print(register_freelancer("Aisha", "Python", 2))
