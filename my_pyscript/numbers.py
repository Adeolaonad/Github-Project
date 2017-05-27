num_word_dict = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9,
                 "ten": 10,
                 "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15, "sixteen": 16,
                 "seventeen": 17,
                 "eighteen": 18, "nineteen": 19, "twenty": 20, "thirty": 30, "forty": 40, "fifty": 50, "sixty": 60,
                 "seventy": 70,
                 "eighty": 80, "ninety": 90, "hundred": 100, "thousand": 1000, "million": 1000000,
                 "billion": 1000000000, "and": "+", ",": "+"}

number = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
          "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen",
          "eighteen", "nineteen", "twenty", "thirty", "forty", "fifty", "sixty", "seventy",
          "eighty", "ninety", "hundred"]

textinput = raw_input("Enter Number in Words in small letters: ")

numwordlist = textinput.replace('-', ' ').split()
print numwordlist
numberstack = []
if (len(numwordlist) == 1) and (numwordlist[0] in number):
    print num_word_dict[numwordlist[0]]
elif (len(numwordlist) == 2):
    for j in numwordlist:
        numberstack.append(num_word_dict[j])
    print numberstack

    for k in range(len(numberstack) - 1):
        if numberstack[k] < numberstack[k + 1]:
            print numberstack[k] * numberstack[k + 1]
        elif numberstack[k] > numberstack[k + 1]:
            print numberstack[k] + numberstack[k + 1]


elif (len(numwordlist) == 3):
    for m in numwordlist:
        numberstack.append(num_word_dict[m])
    print numberstack

    for n in range(len(numberstack) - 1):
        if numberstack[n - 1] > numberstack[n] and numberstack[n] > numberstack[n + 1]:
            print (numberstack[n] + numberstack[n + 1]) * numberstack[n - 1]


elif (len(numwordlist) == 4 and "and" in numwordlist):
    for j in numwordlist:
        numberstack.append(num_word_dict[j])
    print numberstack

    numstring = " "

    for l in range(len(numberstack) - 1):
        if numberstack[l] < numberstack[l + 1]:
            numstring = numstring + str(numberstack[l])
            numstring = numstring + " * " + str(numberstack[l + 1])
            numstring = eval(numstring)
            numstring = numstring + numberstack[l + 3]
            print numstring

"""elif (len(numwordlist) == 4):
    for p in numwordlist:
               numberstack.append(num_word_dict[p])
           print numberstack

           for q in range(len(numberstack) - 1):
               if numberstack[q] < numberstack[q + 1] and numberstack[q + 2] > numberstack[q - 1]:
                   z = (numberstack[q] * numberstack[q + 1]) + (numberstack[q + 2] * numberstack[q - 1])
                   print z

                   # numstring = numstring + str(numberstack[l+1])
           # print numstring
            #numstring = eval(numstring + str(numberstack[l+3]))
            #print numstring

 else:numberstack[l] > numberstack[l + 1]:
            numstring = numstring + (str(numberstack[l]))
            numstring = numstring + "+"
            numstring = numstring + (str(numberstack[l + 1]))
            print numstring

        else:
            pass

"""
