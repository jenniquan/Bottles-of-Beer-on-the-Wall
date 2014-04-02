number = int (raw_input ("How many bottles? "))
drink = raw_input ("What kind of drink? ")

while number > 0:
    print number, " bottles of ", drink, " on the wall, ", number, " bottles of ", drink, "!"
    number = number - 1
    print "So take one down, pass it around, ", number, "more bottles of ", drink, " on the wall!"
