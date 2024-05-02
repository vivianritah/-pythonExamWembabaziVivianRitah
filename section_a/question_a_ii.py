def convertTemperatures():
    print("converting Temperature")
    print("1. Celsius to Farenheit")
    print("2. Farenheit to Celsius")

    option = int(input("Choose option 1 or 2"))
    if option ==1:
        celsius = float(input("Enter the temperature in celsius"))
        farenheit = (9/5 * celsius) + 32
        print(f"{celsius} degrees celsius is equal to {farenheit} degrees farenheit")
    elif option ==2:
        farenheit = float(input("Enter temperature in farenheit"))
        celsius = 5/9 * (farenheit-32)
        print(f"{farenheit} degrees farenheit is equal to {celsius} degrees celsius")
    else:
        print("Invalid Option")

convertTemperatures()
