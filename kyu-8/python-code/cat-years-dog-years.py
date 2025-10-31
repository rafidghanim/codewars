def human_years_cat_years_dog_years(human_years):
    catYears = 0
    dogYears = 0

    if human_years == 1:
        catYears = 15
        dogYears = 15

    elif human_years == 2:
        catYears = 24
        dogYears = 24

    elif human_years >= 3:
        catYears = 4*(human_years-2) + 24 
        dogYears= 5*(human_years-2) + 24


    return [human_years, catYears, dogYears]
