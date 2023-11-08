def calc_dog_years(human_years):
    if human_years < 0:
        return "Error: Negative number entered."
    elif human_years < 2:
        return human_years * 10.5
    else:
        return 21 + (human_years - 2) * 4

human_years = float(input("Enter the number of human years: "))
dog_years = calc_dog_years(human_years)

print("Dog years" + dog_years)