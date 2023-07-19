print (" ‼ FACTORIAL OR NON FACTORIAL NUMBERS ‼ ")

number = int (input (" Please enter your number : "))
factorial_factor = 2

while True :
    baqi_mande = number % factorial_factor

    if baqi_mande != 0 :
        print (" ❌ NO ❌ ")
        break

    else :
        number = number / factorial_factor
        factorial_factor += 1

    if number == 1 :
        print (" ✔ YES ✔ ")
        break
