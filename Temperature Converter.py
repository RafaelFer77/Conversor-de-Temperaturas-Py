def converter(unit1, unit2, temp):
    if unit1.lower() == "c":
        if unit2.lower() == "c":
            result = temp
            return result

        elif unit2.lower() == "f":
            result = (temp * 1.8) + 32
            return result

        elif unit2.lower() == "k":
            result = temp
            return result + 273.15

    if unit1.lower() == "f":
        if unit2.lower() == "f":
            result = temp
            return result

        elif unit2.lower() == "c":
            result = (temp - 32) / 1.8
            return result

        elif unit2.lower() == "k":
            result = (temp - 32) / 1.8 + 273.15
            return result

    if unit1.lower() == "k":
        if unit2.lower() == "k":
            result = temp
            return result

        elif unit2.lower() == "f":
            temp = ((temp - 273.15) * 1.8) + 32
            result = temp
            return result

        elif unit2.lower() == "c":
            temp = temp - 273.15
            result = temp
            return result

while True:

    print("Choose a unit of measurement for your temperature")
    print("C for Celsius")
    print("K for Kelvin")
    print("F for Fahrenheit")
    print("To exit, type 's' ")

    unit1 = input("\nType just one letter here: ")
    if unit1.lower() == "s":
        break
    print("Now choose the temperature unit you want to convert to:")
    print("C for Celsius")
    print("K for Kelvin")
    print("F for Fahrenheit")
    print("To exit, type 's' ")
    
    unit2 = input("\nType just one letter here: ")
    if unit2.lower() == "s":
        break
    print("To exit, type 's' ")
    temp = input("What is the temperature? ")
    if temp.lower() == "s":
        break
    else:
        temp = float(temp)
    
    result = converter(unit1, unit2, temp)
    print(result)
