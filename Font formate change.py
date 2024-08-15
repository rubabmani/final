import pyfiglet
from termcolor import colored

uc = int(input('''
You want to make your text stylish....
1 Yes
2 No / exit:  '''))

if uc == 1:
    text = input("Enter the text you want to format: ")

    # Font selection
    userinput1 = int(input(''' Please select any font style...
        1 slant
        2 banner3-D
        3 bubble
        4 digital
        5 doom
      '''))

    fonts = {
        1: "slant",
        2: "banner3-D",
        3: "bubble",
        4: "digital",
        5: "doom"
    }

    Uchoice_font = fonts.get(userinput1, "slant")

    # Color selection
    userinput2 = int(input(''' Please select any color...
        1 red
        2 green
        3 yellow
        4 blue
        5 magenta
        6 cyan
        7 white
    '''))

    colors = {
        1: "red",
        2: "green",
        3: "yellow",
        4: "blue",
        5: "magenta",
        6: "cyan",
        7: "white"
    }

    Uchoice_color = colors.get(userinput2, "white")
    
    # Font size (scale)
    userinput3 = int(input("Enter the font size (a positive integer): "))
    if userinput3 < 1:
        userinput3 = 1  # Ensuring the font size is at least 1

    # Formatting the text
    formatted_text = pyfiglet.figlet_format(text, font=Uchoice_font)

    # Simulating font size by repeating the text
    scaled_text = "\n".join([formatted_text] * userinput3)

    # Formatting the text
    formatted_text = pyfiglet.figlet_format(text, font=Uchoice_font)
    colored_text = colored(formatted_text, Uchoice_color)

    print(colored_text)

else:
    
    print("Exited without formatting.")
