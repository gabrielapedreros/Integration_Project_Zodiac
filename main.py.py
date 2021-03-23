# Gabriela Pedreros
# An integration project on the different aspects of astrology so that the user gains a greater understanding about themselves from this and other psuedosciences.  
def favorite_and_not_favorite_power_sum(num_fav, num_not):
    # ** will raise the intger of the user's favorite number to the power of their least favorite number
    print("(a)", num_fav ** num_not)
          
def favorite_and_not_favorite_sum(num_fav, num_not):
    # * will multiply the integer of the user's favorite number and the least favorite number together
    print("(b)", num_fav * num_not)

def random_calculations(num_power, num_sum):
    # use % or the modulus operator to find the remainder of the favorite number divided by the least favorite number
    # The // is used to find the quoitent of the two variables
    # The / numeric operator is used for divison , while the + is used for addition
    print("(c)", num_power % num_sum)
    print("(d)", num_power // num_sum)
    print("(e)", num_power / num_sum)
    print("(f)", num_power + num_sum)
#https://www.astrology-zodiac-signs.com/ information on dates
def zodiac_sign(month, day):    
    if month == 1:
        if day < 20:
            zodiac_sign = "Capricorn"
        else:
            zodaic_sign = "Aquarius"
    elif month == 2:
        if day < 19:
            zodiac_sign = "Aquarius"
        else:
            zodiac_sign = "Pisces"
    elif month == 3:
        if day < 21:
            zodiac_sign = "Pisces"
        else:
            zodiac_sign = "Aries"
    elif month == 4 :
        if day < 20:
            zodiac_sign = "Aries"
        else:
            zodiac_sign = "Taurus"
    elif month == 5 :
        if day < 21:
            zodiac_sign = "Taurus"
        else:
            zodiac_sign = "Gemini"
    elif month == 6 :
        if day < 21:
            zodiac_sign = "Gemini"
        else:
            zodiac_sign = "Cancer"
    elif month == 7:
        if day < 23:
            zodiac_sign = "Cancer"
        else:
            zodiac_sign = "Leo"
    elif month == 8:
        if day < 23:
            zodiac_sign = "Leo"
        else:
            zodiac_sign = "Virgo"
    elif month == 9:
        if day < 23:
            zodiac_sign = "Virgo"
        else:
            zodiac_sign = "Libra"
    elif month == 10:
        if day < 23:
            zodiac_sign = "Libra"
        else:
            zodiac_sign = "Scorpio"
    elif month == 11:
        if day <= 21:
            zodiac_sign = "Scorpio"
        else:
            zodiac_sign = "Sagittarius"
    elif month == 12:
        if day <= 21:
            zodiac_sign = "Sagittarius"
        else:
            zodiac_sign = "Capricorn"
    return zodiac_sign

def compare_user_sign(zodiac_sign, user_month):
    user_choice_to_compare1 = input("Let's assume your zodiac sign is not equal to another. Choose a zodiac sign to compare(Aries, Pisces, Taurus, Aquarius): ")
    signs_not_equal = (user_choice_to_compare1 != zodiac_sign)
    print("It is",signs_not_equal, "that these signs are NOT the same.")
    
    user_choice_to_compare2 = input("Choose another zodiac sign to compare to yours(Virgo, Cancer, Gemini, Leo): ")
    using_or_with_choices = (user_choice_to_compare2 != zodiac_sign) or (user_month == (1,2,3,4,5,6))
    print("It is", using_or_with_choices, "that either the", user_choice_to_compare2, "sign is not the same as yours OR your birth month is within the first 6 months of the year.")
    compare_user_choices =(not(user_choice_to_compare1 == user_choice_to_compare2))
    print("Also, it is", compare_user_choices,"that the first zodiac you chose is NOT the same as the second zodiac you chose.")
    

    

def main():
    print("Welcome to my Integration Project!")
    
    # user_name is a variable
    # a variable is a name that refers to a value with a specific location
    # = assigns the variable
    # \n prints string in a new line , in this case , the input
    
    user_name = input("What is your name? \n")
    print("Hello" , user_name + "!" , "I'm Venus, pleased to meet you. \nI'm going to ask a few random questions. For the first two questions, please do not answer with the number zero itself. \nLet's begin!")
    
    # +  is used as a string operator that concatenates the exclamation mark and the string literal of the varible user_name
    # fav_num and not_fav_num are variables , the int converts the string into an integer
    # Since the variables fav_num and not_fav_num have been converted to integers , calculations are allowed between them
    
    fav_number = int(input("What is your favorite number? \n"))
    not_favorite_number = (int(input("What is your least favorite number? \n")))
    
    get_power_sum = favorite_and_not_favorite_power_sum(fav_number, not_favorite_number)
    get_sum = favorite_and_not_favorite_sum(fav_number, not_favorite_number)
    
    # to randomize more numbers , I created two new variables that are integers for the following few calculations
    fav_num1 = fav_number
    not_fav1 = not_favorite_number
    
    fav_num1 **= not_fav1
    not_fav1 *= fav_num1
    
    get_random_calculations = random_calculations(fav_num1, not_fav1)
        
    a = int(fav_number ** not_favorite_number)
    b = int(fav_number ** not_favorite_number)
    c = int(fav_num1 % not_fav1)
    d = int(fav_num1 // not_fav1)
    e = int(fav_num1 / not_fav1)
    f = int(fav_num1 + not_fav1)

    avg_of_fav_not_fav = str(input("Which value from above do you prefer out of the six? Please type the letter. \n"))
    rate_of_avg = int(input("Rate that value on a scale from 1 to 10. \n"))
    
    # the string operator * repeats the string (user_name) as many times as the integer (rate_of_avg) value
    
    print(user_name * rate_of_avg , "\n")
    print("Thank you for participating in this short interactive section. \nIn order to get to know you better, please answer the following. \n")

        
#user info
    month_dob = int(input("Enter the number month you were born in: "))
    day_dob = int(input("Enter the number day you were born on: "))
    year_dob = int(input("Enter the year number you were born on: "))
    
    # I used sep="/" so that it outputs with a date format
    
    get_zodiac_sign = zodiac_sign(month_dob, day_dob)
    user_birthdate = print(month_dob, day_dob, year_dob, sep = "/")
    
    # The numeric operator - is used to subtract the value of the year the user was born in from 2021
    
    age = 2021 - year_dob
    print("According to your birthdate, your zodiac sign is a", get_zodiac_sign,"and by the end of 2021 you will be" , age , "years old!")
#zodiac info            
    air = ['Gemini','Libra','Aquarius',"air"]
    earth = ["Taurus","Virgo","Capricorn","earth"]
    fire = ["Leo","Sagittarius","Aries","fire"]
    water = ["Cancer","Scorpio","Pisces","water"]
#https://www.astrology-zodiac-signs.com/ information on elements
    while True:
        user_element_guess = input("Even if you do not know much about zodiac signs, enter what element(water, fire, air, and earth) you think your sign is associated with: ")
        if user_element_guess in air and get_zodiac_sign in air:
            print("Correct! Your zodiac sign,",get_zodiac_sign,", is an air sign.")
            break
        if user_element_guess in earth and get_zodiac_sign in earth:
            print("Correct! Your zodiac sign,",get_zodiac_sign,", is an earth sign.")
            break
        if user_element_guess in fire and get_zodiac_sign in fire :
            print("Correct! Your zodiac sign,",get_zodiac_sign,", is a fire sign.")
            break
        if user_element_guess in water and get_zodiac_sign in water:
            print("Correct! Your zodiac sign,",get_zodiac_sign,", is a water sign.")
            break
        
    compare_user_sign_with_other_signs = compare_user_sign(get_zodiac_sign, month_dob)

    for count in range(5, 0,-1):
        print(count)
    print("All done! I hope you were able to learn more about horoscopes :)")


main()
print("Exiting")
