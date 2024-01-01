# This is a module create to be implemented into another python file. The module can then be called when required.


from random import choice

capital = "Topeka"

bird = "Western Meadowlark"

flower = "Sunflower"

song = "Home on the Range"


def randomfunfact():
    funfacts = ["Kansas is considered flat, but it does have a mountain", "Whichita is the largest city in the state, but many would guess that it is Kansas city.",
                "A considerable portion of Kansas city is actually Missouri", "Most Kansans are annoyed by Wizard of Oz refences from people outside Kansas."]

    index = choice("0123")

    print(funfacts[int(index)])


if __name__ == "__main__":
    randomfunfact()
