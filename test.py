import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    match = re.search(r"^([0-9]+)\.([0-9]+)\.([0-9]+)\.([0-9]+)$",ip)
    if not match:
        return False

    for num in match.groups():
        if int(num) > 255 or int(num) < 0:
            return False
    return True


...


if __name__ == "__main__":
    main()