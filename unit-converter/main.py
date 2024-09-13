def convert_length(value, from_unit, to_unit):
    # Define conversion factors to meters
    units_to_meters = {
        'meters': 1,
        'kilometers': 1000,
        'centimeters': 0.01,
        'millimeters': 0.001,
        'inches': 0.0254,
        'feet': 0.3048,
        'yards': 0.9144,
        'miles': 1609.34
    }

    # Convert value to meters
    meters = value * units_to_meters[from_unit]
    # Convert meters to target unit
    return f"{meters / units_to_meters[to_unit]:.2f}"


def convert_weight(value, from_unit, to_unit):
    # Define conversion factors to kilograms
    units_to_kilograms = {
        'kilograms': 1,
        'grams': 0.001,
        'pounds': 0.453592,
        'ounces': 0.0283495
    }

    # Convert value to kilograms
    kilograms = value * units_to_kilograms[from_unit]
    # Convert kilograms to target unit
    return f"{kilograms / units_to_kilograms[to_unit]:.2f}"


def convert_temperature(value, from_unit, to_unit):
    if from_unit == 'Celsius' and to_unit == 'Fahrenheit':
        return (value * 9 / 5) + 32
    elif from_unit == 'Fahrenheit' and to_unit == 'Celsius':
        return (value - 32) * 5 / 9
    elif from_unit == 'Celsius' and to_unit == 'Kelvin':
        return value + 273.15
    elif from_unit == 'Kelvin' and to_unit == 'Celsius':
        return value - 273.15
    elif from_unit == 'Fahrenheit' and to_unit == 'Kelvin':
        return (value - 32) * 5 / 9 + 273.15
    elif from_unit == 'Kelvin' and to_unit == 'Fahrenheit':
        return (value - 273.15) * 9 / 5 + 32
    else:
        return value  # No conversion needed if units are the same


def main():
    print("WELCOME TO DEVSTORIES PLAYGROUND")
    print("-------------------------")
    while True:
        try:
            print("Unit Converter")
            print("1. Length")
            print("2. Weight")
            print("3. Temperature")
            print("4. Exit")

            choice = input("Choose conversion type (1/2/3/4): ")

            if choice == '1':
                try:
                    print("Choose from length units: [meters, kilometers, centimeters, "
                          "millimeters, inches, feet, yards, miles]")
                    from_unit = input("From unit: ")
                    to_unit = input("To unit: ")
                    value = float(input("Value to convert: "))
                    result = convert_length(value, from_unit, to_unit)
                    print(f"{value} {from_unit} is {result} {to_unit}")
                except Exception as ex:
                    print("Invalid input. Please try again!!!")
                    continue

            elif choice == '2':
                try:
                    print("Choose from weight units: [kilograms, grams, pounds, ounces]")
                    from_unit = input("From unit: ")
                    to_unit = input("To unit: ")
                    value = float(input("Value to convert: "))
                    result = convert_weight(value, from_unit, to_unit)
                    print(f"{value} {from_unit} is {result} {to_unit}")
                except Exception as ex:
                    print("Invalid input. Please try again!!!")
                    continue

            elif choice == '3':
                print("Choose from temperature units: [celsius, fahrenheit,kelvin]")
                from_unit = input("From unit: ")
                to_unit = input("To unit: ")
                value = float(input("Value to convert: "))
                result = convert_temperature(value, from_unit, to_unit)
                print(f"{value} {from_unit} is {result} {to_unit}")

            elif choice == '4':
                print("Thank you!!!")
                break

        except Exception as ex:
            print("Invalid input. Please try again!!!")
            continue


if __name__ == "__main__":
    main()