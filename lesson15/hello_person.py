# Using modules and command line arguments


def hello(name, lang):  # Derfin function 'hello' with two arguments to be passed
    greetings = {  # Creates a dictionary with 3No. key/value pairs
        "English": "Hello",
        "Spanish": "Hola",
        "German": "Hallo"
    }

    msg = f"{greetings[lang]} {name}!"
    print(msg)


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(
        description="Provides a personal greeting."
    )

    parser.add_argument(
        "-n", "--name", metavar="name",
        required=True, help="The name of the person to greet."
    )

    parser.add_argument(
        "-l", "--lang", metavar="language", required=True, choices=["English", "Spanish", "German"],
        help="The language of the greeting."
    )

    args = parser.parse_args()

    hello(args.name, args.lang)
