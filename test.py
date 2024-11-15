def calc_person_age(age):
    
    if age > 18 :
        is_adult = True
    else:
        is_adult = False
    return is_adult

age_input = int(input("Enther your age : "))
is_of_age = calc_person_age(age_input)

if is_of_age:
    print ("You are adult.")
else:
    print("You are under than 18.")