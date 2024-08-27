
def get_bmi_computation(weight, height):
    height = height / 100
    result = weight / (height * height)
    return result


def get_bmi_interpretation(result):
    if result < 18.5:
        return 'Underweight'
    elif 18.5 <= result < 24.9:
        return 'Normal weight'
    elif 25 <= result < 29.9:
        return 'Overweight'
    else:
        return 'Obesity'


def main():
    while True:
        print("----------------WELCOME TO DEVSTORIES PLAYGROUND--------------------------")
        print("BODY MASS INDEX CALCULATOR")
        print("BMI Categories:")
        print("Underweight = <18.5")
        print("Normal weight = 18.5–24.9")
        print("Overweight = 25–29.9")
        print("Obesity = BMI of 30 or greater")
        try:
            user_weight = float(input("WEIGHT(KG): "))
            user_height = float(input("HEIGHT(CM): "))
            calculation = get_bmi_computation(user_weight, user_height)
            bmi_result = get_bmi_interpretation(calculation)
            print(f"BMI: {bmi_result}")
            return False
        except Exception as ex:
            print(f"Error encountered: {ex}")


if __name__ == "__main__":
    main()

