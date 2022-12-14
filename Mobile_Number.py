import re


def checkNumber(test_string):

    patterns = {"[0-9]{10}",
                "[0-9]{3}[-][0-9]{3}[-][0-9]{4}",
                "[(][0-9]{3}[)][0-9]{3}[-][0-9]{4}",
                "[(][0-9]{3}[)][-][0-9]{3}[-][0-9]{4}",
                "[0-9]{3}[.][0-9]{3}[.][0-9]{4}",
                "[0-9]{3}[' '][0-9]{3}[' '][0-9]{4}",
                "([+][0-9])[0-9]{10}",
                "([+][0-9])[' '][0-9]{3}[.][0-9]{3}[.][0-9]{4}",
                "[+][0-9]{3}[-][0-9]{3}[-][0-9]{4}",
                "[0-9][-][0-9]{3}[-][0-9]{3}[-][0-9]{4}"
                }

    for pattern in patterns:
        if re.match(pattern, test_string):
            return "A Valid Number."
    return "Invalid Number."


if __name__ == "__main__":
    print(checkNumber("212.456.7890"))
