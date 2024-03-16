import os

# Create directory
os.mkdir("/home/cicles/AO/Tasca11/Prova")
os.chdir("/home/cicles/AO/Tasca11/Prova")

# Create file and write a message
with open("Ex12.txt", "w") as f:
    print("Fitxer creat correctament!")

# List of professors
professors = ["David", "Pep", "Fela", "Lluis", "Joan"]

# Append professors to the file
with open("Ex12.txt", "a+") as f:
    for e in professors:
        f.write(e + "\n")

# Read the file and print its contents
a = []
with open("Ex12.txt", "r") as f:
    for e in f:
        c = e.split("\n")
        a.append(c[0])
print(a)
