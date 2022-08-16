# 141
dict1 = {
    0: "",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
}

dict2 = {
    0: "",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
}

dict3 = {
    0: "",
    1: "one hundred",
    2: "two hundred",
    3: "three hundred",
    4: "four hundred",
    5: "five hundred",
    6: "six hundred",
    7: "seven hundred",
    8: "eight hundred",
    9: "nine hundred"
}

num = int(input("Введите число от 0 до 999: "))

def word():
    c = num // 100
    b = num % 100
    a = num % 10
    
    if b in range(11, 20):
        a = 0
    else:
        b = b // 10 * 10
    
    # print(c, b, a)
    print(dict3[c], dict2[b], dict1[a])


word()

# Введите число от 0 до 999: 12
 # twelve
 
# Введите число от 0 до 999: 7
 # seven
  
# Введите число от 0 до 999: 919
# nine hundred nineteen

# Введите число от 0 до 999: 919
# nine hundred nineteen

# Введите число от 0 до 999: 54
 # fifty four
 
# Введите число от 0 до 999: 16
 # sixteen
 
# Введите число от 0 до 999: 3
 # three