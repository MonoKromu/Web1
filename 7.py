import argparse

parser = argparse.ArgumentParser()
parser.add_argument("args", nargs="*")
args = parser.parse_args().args
if not args:
    print("no args")
else:
    print("\n".join(args))
