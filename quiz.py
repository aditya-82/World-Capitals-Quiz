import random

def main():
    data = {'Afghanistan' : 'Kabul',
        'Albania' : 'Tirana',
        'Algeria' : 'Algiers',
        'Andorra' : 'Andorra La Vella',
        'Angola' : 'Luanda',
        'Antigua and Barbuda' : "Saint John's",
        'Argentina' : 'Buenos Aires',
        'Armenia' : 'Yerevan',
        'Australia' : 'Canberra',
        'Austria' : 'Vienna',
        'Azerbaijan' : 'Baku',
        'Bahamas' : 'Nassau',
        'Bahrain' : 'Manama',
        'Bangladesh' : 'Dhaka',
        'Barbados' : 'Bridgetown',
        'Belarus' : 'Minsk',
        'Belgium' : 'Brussels',
        'Belize' : 'Belmopan',
        'Benin' : 'Porto-Novo',
        'Bhutan' : 'Thimphu',
        'Bolivia' : 'Sucre',
        'Bosnia & Herzegovina' : 'Sarajevo',
        'Botswana' : 'Gaborone',
        'Brazil' : 'Brasilia',
        'Brunei' : 'Bandar Seri Begawan',
        'Bulgaria' : 'Sofia',
        'Burkina Faso' : 'Ouagadougou',
        'Burundi' : 'Bujumbura',
        
    }

    print("Welcome to the Atlas Quiz!")
    # Quiz should have a list of all the capitals of the world and randomly ask capitals of countries

    playing = input("Would you like to start a new game? ")
    if playing.lower() != "yes":
        quit()

    else:
        points= 0
        quiz(points, data)
        
def quiz(a, b):

    if len(b) != 0:
        question = random.choice(list(b))
        answer = input(question + ": ")
        if answer == b[question]:
            a += 1
            del b[question]
            print(f'Correct! You now have {a} points!')
            quiz(a, b)
        else:
            print("Wrong answer! Better Luck next time!")
            quit()
    else:
        print("You seem to know all the capitals! Please wait till a new country is created and try again!")
        quit()


main()