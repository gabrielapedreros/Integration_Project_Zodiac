# Gabriela Pedreros
"""
    An integration project on the the different aspects of astrology so that
    the user gains a greater understanding about themselves from this
    pseudoscience.
    """
__author__ = "Gabriela Pedreros"


def random_calculations(num_fav, not_num_fav):
    """
    The function definition will perform various calculations between the
    user's favorite and not favorite number and return the random
    calculations.
    :param num_fav: The user input of their favorite number converted into
    an integer.
    :param not_num_fav: The user input of their least favorite number
    converted into an integer.
    :return: return the various calculations that were performed between the
    two numbers.
    """
    # ** will raise the integer of the user's favorite number to the power of
    # their least favorite number.
    # * will multiply the integer of the user's favorite number and the least
    # favorite number together.
    # use % or the modulus operator to find the remainder of the user's
    # favorite number divided by their least favorite number.
    # The // is used to find the quotient of the two variables.
    # The / numeric operator is used for division, while the + is used for
    # addition.
    print("(a)", num_fav ** not_num_fav)
    print("(b)", num_fav * not_num_fav)
    print("(c)", num_fav % not_num_fav)
    print("(d)", num_fav // not_num_fav)
    print("(e)", num_fav / not_num_fav)
    print("(f)", num_fav + not_num_fav)
    return random_calculations

    # https://www.astrology-zodiac-signs.com/ information on dates and their
    # given zodiac sign.


def user_zodiac_sign(month, day):
    """
    The function definition will use the user's input of their birthday
    information in order to calculate the user's respective zodiac sign.
    The zodiac sign is dependent on a person's birthdate.
    :param month: The user input of their birth month converted into an
    integer.
    :param day: The user input of their birth date converted into an integer.
    :return: return the user's zodiac sign which is based on someone's
    birthdate.
    """
    zodiac_sign = str()
    if month == 1:
        if day < 20:
            zodiac_sign = "Capricorn"
        else:
            zodiac_sign = "Aquarius"
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
    elif month == 4:
        if day < 20:
            zodiac_sign = "Aries"
        else:
            zodiac_sign = "Taurus"
    elif month == 5:
        if day < 21:
            zodiac_sign = "Taurus"
        else:
            zodiac_sign = "Gemini"
    elif month == 6:
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
    """
    Using the user's input of another zodiac sign and the user's birthday
    month, the program will compare the user's zodiac sign with others.
    :param zodiac_sign: A string that is determined by the birth date.
    :param user_month: The user input of their birthdate month converted
    into an integer in order to do calculations.
    :return: returning the comparisons between the zodiac signs and the user's
    birth month.
    """
    # must enter the signs given

    user_choice_to_compare1 = str(input("Let's assume your zodiac sign is "
                                        "not equal to another zodiac sign. "
                                        "Choose a zodiac sign to compare to "
                                        "yours(Aries, Pisces, Taurus,"
                                        "Aquarius): "))
    signs_not_equal = (user_choice_to_compare1 != zodiac_sign)
    print("It is", signs_not_equal, "that these signs are NOT the same.")
    user_choice_to_compare2 = input(
        "Choose another zodiac sign to compare to yours(Virgo, Cancer,"
        " Gemini, Leo): ")
    using_or_with_choices = (user_choice_to_compare2 != zodiac_sign) or (
            user_month == (1, 2, 3, 4, 5, 6))
    print("It is", using_or_with_choices, "that either the",
          user_choice_to_compare2,
          "sign is not the same as yours OR your birth month is within "
          "the first 6 months of the year.")
    compare_user_choices = (
        not (user_choice_to_compare1 == user_choice_to_compare2))
    print("Also, it is", compare_user_choices,
          "that the first zodiac you chose is NOT the same as"
          " the second zodiac you chose.")
    return compare_user_sign


def main():
    """
    This code will start my program with a welcome. The program will ask
    various random and important questions to the user and will provide the
    user with information about zodiac signs.

    """
    print("Welcome to my Integration Project!")

    # user_name is a variable.
    # a variable is a name that refers to a value with a specific location.
    # = assigns the variable.
    # \n prints a string on a new line , in this case,  it is used for the
    # user the input.

    user_name = str(input("What is your name?"))
    print("Hello", user_name + "!",
          "I'm Venus, pleased to meet you. \nI'm going to ask a few random "
          "questions. For the first two questions,"
          " please do not answer with the number zero itself. \nLet's "
          "begin", end="!\n")

    # +  is used as a string operator that concatenates the exclamation
    # mark and the string literal of the variable user_name.
    # fav_number and not_favorite_number are variables that are
    # strings converted into integers.
    # Since the variables fav_num and not_fav_num have been converted to
    # integers, calculations between them are allowed.

    # I use a break with my while statements to show my understanding that it
    # will stop the continuation of a part of the program under certain
    # circumstances although I know all loops should not require a break.
    while True:
        try:
            fav_number = int(input("What is your favorite number? \n"))
            while fav_number <= 0:
                fav_number = int(input("ZeroDivisionError. Please enter"
                                       " a whole number greater than zero: "))
            break
        except ValueError:
            print("ValueError. Please enter a whole number greater than "
                  "zero. ")
    while True:
        try:
            not_favorite_number = int(input("What is your least favorite "
                                            "number? "
                                            "\n"))
            while not_favorite_number == 0:
                not_favorite_number = int(input("ZeroDivisionError. "
                                                "Please enter a whole number"
                                                " greater than zero: "))
            break
        except ValueError:
            print("ValueError. Please enter a whole number greater than "
                  "zero. ")
    #    a = (num_fav ** num_not)
    #    b = (num_fav * num_not)
    #    c = (num_fav % num_not)
    #    d = (num_fav // num_not)
    #    e = (num_fav / num_not)
    #    f = (num_fav + num_not)

    random_calculations(fav_number, not_favorite_number)
    while True:
        try:
            rate_of_avg = int(input("Choose your favorite number out of the "
                                    "six given above. Rate that number on a "
                                    "scale from 1-10: "))
            while rate_of_avg >= 11 or rate_of_avg <= 0:
                rate_of_avg = int(input("Error. Please enter a whole number "
                                        "between 1-10: "))
            break
        except ValueError:
            print("ValueError. Please enter a whole number between 1-10.")

    # MUST BE A LETTER BETWEEN 1-10
    print(user_name * rate_of_avg, "\n")
    print("Thank you for participating in this short interactive section. ")
    print("In order to get to know you better, please answer the following.\n")

    # the string operator * repeats the string (user_name) as many times
    # as the integer (rate_of_avg) value.

    # user info
    # MUST BE BETWEEN 1-12, year any whole number after 1900-2020
    while True:
        try:
            month_dob = int(input("Enter the number month you were born in: "))
            while month_dob >= 13 or month_dob <= 0:
                month_dob = int(input("Error. The number month you were born "
                                      "in must be between 1-12."))
            break
        except ValueError:
            print("ValueError. Month number must be a whole number between "
                  "1-12.")
    while True:
        try:
            day_dob = int(input("Enter the number day you were born on: "))
            while day_dob >= 32 or month_dob <= 0:
                day_dob = int(input("Error. The number day you were born on "
                                    "must be between 1-31."))
            break
        except ValueError:
            print("ValueError. Day number must be a whole number between "
                  "1-31.")
    while True:
        try:
            year_dob = int(input("Enter the year number you were born on: "))
            while year_dob >= 2021 or year_dob <= 1900:
                year_dob = int(input("Error. The year number you were born in "
                                     "must be between 1900-2020."))
            break
        except ValueError:
            print("ValueError. The year number must be a whole number between "
                  "1900-2020.")

    get_zodiac_sign = user_zodiac_sign(month_dob, day_dob)

    # I used sep="/" so that it outputs with a date format

    # The numeric operator - is used to subtract the value of the year
    # the user was born in from 2021.
    print(month_dob, day_dob, year_dob, sep="/")
    age = 2021 - year_dob
    print("According to your birthdate, your zodiac sign is a",
          get_zodiac_sign, "and by the end of 2021 you will be",
          age, "years old!")
    # zodiac info
    air = ['Gemini', 'Libra', 'Aquarius', "air"]
    earth = ["Taurus", "Virgo", "Capricorn", "earth"]
    fire = ["Leo", "Sagittarius", "Aries", "fire"]
    water = ["Cancer", "Scorpio", "Pisces", "water"]
    # https://www.astrology-zodiac-signs.com/ information on elements.
    while True:
        user_element_guess = input(
            "Even if you do not know much about zodiac signs, enter what "
            "element(water, fire, air, and earth) you "
            "think your sign is associated with: ")
        if user_element_guess in air and get_zodiac_sign in air:
            print("Correct! Your zodiac sign" + ",", get_zodiac_sign + ","
                  " is an air sign.")
            break
        if user_element_guess in earth and get_zodiac_sign in earth:
            print("Correct! Your zodiac sign" + ",", get_zodiac_sign + ","
                  " is an earth sign.")
            break
        if user_element_guess in fire and get_zodiac_sign in fire:
            print("Correct! Your zodiac sign" + ",", get_zodiac_sign + ","
                  " is a fire sign.")
            break
        if user_element_guess in water and get_zodiac_sign in water:
            print("Correct! Your zodiac sign" + ",", get_zodiac_sign + ","
                  " is a water sign.")
            break

    compare_user_sign(get_zodiac_sign, month_dob)

    for count in range(5, 0, -1):
        print(count)
    print("All done! I hope you were able to learn more about horoscopes "
          ":)")
    print("Exiting")


if __name__ == "__main__":
    main()
