def to_celsius(farenheit):
    celsius = (farenheit - 32) * 5/9
    return celsius

def to_farenheit(celsius):
    farenheit = celsius * 9/5 + 32
    return farenheit

# the main function is used to test the other functions


if __name__ == "__main__":
    for temp in range(0, 212, 40):
        print(temp, "Farenheit =", round(to_celsius(temp), 2), "Celsius")

    for temp in range(0, 101, 20):
        print(temp, "Celsius =", round(to_farenheit(temp), 2),
              "Farenheit")

                     