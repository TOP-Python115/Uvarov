dict = {
  "name" : "Иван e1",
  "имя" : "Иван r1",
  "surname" : "Жуков e2",
  "фамилия" : "Жуков r2",
  "age" : "26 e3",
  "возраст" : "26 r3"
}

word = input()

for k, v in dict.items():
    if word in v:
      print(k)
      # break
      
# Иван
# name
# имя

# Жуков
# surname
# фамилия

# 26
# age
# возраст

# e1
# name

# r2
# фамилия

# r1
# имя