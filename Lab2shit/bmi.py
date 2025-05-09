def calculate_bmi(height, weight):
    bmi = weight / height ** 2
    return bmi

def classify_bmi(bmi):
    if(bmi < 18.5):
        return -1
    elif(bmi >=18.5 and bmi <=25):
        return 0
    else:
        return 1
    return


def main():
    height = float(input("Enter your height (in m): "))
    weight = float(input("Enter your weight (in kg): "))

    print(f"Your BMI is {calculate_bmi(height, weight)}")
    bmi = calculate_bmi(height, weight)
    ahh = classify_bmi(bmi)
    print(ahh)

if __name__ == "__main__":
    main()