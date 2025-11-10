from argparse import ArgumentParser

parser = ArgumentParser(exit_on_error=False)
parser.add_argument("numbers", nargs="*", type=int)

try:
    numbers = parser.parse_args().numbers
    count = len(numbers)
    if count == 0:
        print("NO PARAMS")
    elif count == 1:
        print("TOO FEW PARAMS")
    elif count > 2:
        print("TOO MANY PARAMS")
    else:
        print(numbers[0] + numbers[1])
except Exception as e:
    print(type(e))
