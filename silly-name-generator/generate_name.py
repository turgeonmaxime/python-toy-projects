"""Generate funny names by randomly combining names from 2 separate tuples."""
import random

BCOLOURS = {
    'HEADER': '\033[95m',
    'OKBLUE': '\033[94m',
    'OKCYAN': '\033[96m',
    'OKGREEN': '\033[92m',
    'WARNING': '\033[93m',
    'FAIL': '\033[91m',
    'ENDC': '\033[0m',
    'BOLD': '\033[1m',
    'UNDERLINE': '\033[4m'
    }

FIRST_NAMES = ('Baby Oil', 'Bad News', 'Big Burps', "Bill 'Beenie-Weenie'",
               "Bob 'Stinkbug'", 'Bowel Noises', 'Boxelder', "Bud 'Lite'",
               'Butterbean', 'Buttermilk', 'Buttocks', 'Chad', 'Chesterfield',
               'Chewy', 'Chigger', 'Cinnabuns', 'Cleet', 'Cornbread', 'Crab Meat',
               'Crapps', 'Dark Skies', 'Dennis Clawhammer', 'Dicman', 'Elphonso',
               'Fancypants', 'Figgs', 'Foncy', 'Gootsy', 'Greasy Jim', 'Huckleberry',
               'Huggy', 'Ignatious', 'Jimbo', "Joe 'Pottin Soil'", 'Johnny',
               'Lemongrass', 'Lil Debil', 'Longbranch', '"Lunch Money"', 'Mergatroid',
               '"Mr Peabody"', 'Oil-Can', 'Oinks', 'Old Scratch', 'Ovaltine',
               'Pennywhistle', 'Pitchfork Ben', 'Potato Bug', 'Pushmeet',
               'Rock Candy', 'Schlomo', 'Scratchensniff', 'Scut',
               "Sid 'The Squirts'", 'Skidmark', 'Slaps', 'Snakes', 'Snoobs',
               'Snorki', 'Soupcan Sam', 'Spitzitout', 'Squids', 'Stinky',
               'Storyboard', 'Sweet Tea', 'TeeTee', 'Wheezy Joe',
               "Winston 'Jazz Hands'", 'Worms')

LAST_NAMES = ('Appleyard', 'Bigmeat', 'Bloominshine', 'Boogerbottom',
              'Breedslovetrout', 'Butterbaugh', 'Clovenhoof', 'Clutterbuck',
              'Cocktoasten', 'Endicott', 'Fewhairs', 'Gooberdapple', 'Goodensmith',
              'Goodpasture', 'Guster', 'Henderson', 'Hooperbag', 'Hoosenater',
              'Hootkins', 'Jefferson', 'Jenkins', 'Jingley-Schmidt', 'Johnson',
              'Kingfish', 'Listenbee', "M'Bembo", 'McFadden', 'Moonshine', 'Nettles',
              'Noseworthy', 'Olivetti', 'Outerbridge', 'Overpeck', 'Overturf',
              'Oxhandler', 'Pealike', 'Pennywhistle', 'Peterson', 'Pieplow',
              'Pinkerton', 'Porkins', 'Putney', 'Quakenbush', 'Rainwater',
              'Rosenthal', 'Rubbins', 'Sackrider', 'Snuggleshine', 'Splern',
              'Stevens', 'Stroganoff', 'Sugar-Gold', 'Swackhamer', 'Tippins',
              'Turnipseed', 'Vinaigrette', 'Walkingstick', 'Wallbanger', 'Weewax',
              'Weiners', 'Whipkey', 'Wigglesworth', 'Wimplesnatch', 'Winterkorn',
              'Woolysocks')

def main():
    """Choose names at random from 2 tuples and print to screen."""
    print("Welcome to the Psych 'Sidekick Name Picker.'\n")
    print("A name just like Sean would pick for Gus:\n\n")


    while True:
        sample_first = random.choice(FIRST_NAMES)
        sample_last = random.choice(LAST_NAMES)
        pseudo_name = sample_first + ' ' + sample_last

        print(f"{BCOLOURS['OKGREEN']}{BCOLOURS['BOLD']}{pseudo_name}{BCOLOURS['ENDC']}")

        try_again = input("\n\nTry again? (Press Enter else X to quit)\n")
        if try_again.lower() == "x":
            break

if __name__ == "__main__":
    main()
