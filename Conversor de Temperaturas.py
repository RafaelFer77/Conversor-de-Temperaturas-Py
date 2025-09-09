def converter(unidade1, unidade2, temp):
    if unidade1.lower() == "c":
        if unidade2.lower() == "c":
            resultado = temp
            return resultado

        elif unidade2.lower() == "f":
            resultado = (temp * 1.8) + 32
            return resultado

        elif unidade2.lower() == "k":
            resultado = temp
            return resultado + 273.15

            
              

    if unidade1.lower() == "f":
        if unidade2.lower() == "f":
            resultado = temp
            return resultado

        elif unidade2.lower() == "c":
            resultado = (temp - 32) / 1.8
            return resultado
            

        elif unidade2.lower() == "k":
            resultado = (temp - 32) / 1.8 + 273.15
            return resultado



    if unidade1.lower() == "k":
        if unidade2.lower() == "k":
            resultado = temp
            return resultado

        elif unidade2.lower() == "f":
            temp = ((temp - 273.15) * 1.8) + 32
            resultado = temp
            return resultado

        elif unidade2.lower() == "c":
            temp = temp - 273.15
            resultado = temp
            return resultado

while True:

    print("Escolha uma unidade de medida que vc tenha a temperatura")
    print("C para Celcius")
    print("K para Kelvin")
    print("F para Fahrenheit")
    print("Caso queira sair digite 's' ")

    unidade1 = input("\nDigite apenas uma letra aqui: ")
    if unidade1.lower() == "s":
        break
    print("Agora escolha a temperatura que vc deseja converter:")
    print("C para Celcius")
    print("K para Kelvin")
    print("F para Fahrenheit")
    print("Caso queira sair digite 's' ")
    
    unidade2 = input("\nDigite apenas uma letra aqui: ")
    if unidade2.lower() == "s":
        break
    print("Caso queira sair digite 's' ")
    temp = input("Qual a temperatura? ")
    if temp.lower() == "s":
        break
    else:
        temp = float(temp)
    
    resultado = converter(unidade1, unidade2, temp)
    print(resultado)
    
