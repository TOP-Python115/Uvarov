text = input().split()
dict = {}

for i in text:
  if i in dict:
    print(f'{i}_{dict[i]}', end=' ')
  else:
    print(i, end=' ')
  dict[i] = dict.get(i, 0) + 1

# 1.py 1.py aux.h main.cpp functions.h main.cpp 2.py main.cpp
# 1.py 1.py_1 aux.h main.cpp functions.h main.cpp_1 2.py main.cpp_2