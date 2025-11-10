import argparse
from argparse import ArgumentParser


def key_value_type(arg):
    kv = arg.split("=")
    if len(kv) != 2:
        raise argparse.ArgumentTypeError("Wrong argument type")
    elif kv[0] == "" or kv[1] == "":
        raise  argparse.ArgumentTypeError("Empty key or value")
    else:
        key, value = kv[0], kv[1]
        return key, value

parser = ArgumentParser()
parser.add_argument("kvs", nargs="*", type=key_value_type)
parser.add_argument("-s", "--sort", action="store_true")
kvs = parser.parse_args().kvs
if parser.parse_args().sort:
    kvs = sorted(kvs)
for k, v in kvs:
    print(f"Key: {k} Value: {v}")
