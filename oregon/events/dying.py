from oregon.utilities.user_prompts import ask_yes_no


def dying():
    print("")
    print("DO TO YOUR UNFORTUNATE SITUATION, THERE ARE A FEW")
    print("FORMALITIES WE MUST GO THROUGH")
    print("")
    # Responses to the first two questions are ignored intentionally
    ask_yes_no("WOULD YOU LIKE A MINISTER?")
    ask_yes_no("WOULD YOU LIKE A FANCY FUNERAL?")
    response = ask_yes_no("WOULD YOU LIKE US TO INFORM YOUR NEXT OF KIN?")
    if not response:
        print("YOUR AUNT NELLIE IN ST. LOUIS IS ANXIOUS TO HEAR")
    print("")
    print("WE THANK YOU FOR THIS INFORMATION AND WE ARE SORRY YOU")
    print("DIDN'T MAKE IT TO THE GREAT TERRITORY OF OREGON")
    print("BETTER LUCK NEXT TIME")
    print("")
    print("")
    print("                              SINCERELY")
    print("                 THE OREGON CITY CHAMBER OF COMMERCE")
    exit(0)
