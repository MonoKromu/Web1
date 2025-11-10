import sys

def get_args_dict(args):
    args_dict = {}
    sort = False
    for arg in args:
        if arg == "--sort":
            sort = True
            continue
        kv = arg.split("=")
        if len(kv) == 2:
            key, value = kv[0], kv[1]
            args_dict[key] = value
    if sort:
        args_dict = dict(sorted(args_dict.items()))
    return args_dict

for k, v in get_args_dict(sys.argv).items():
    print(f"Key: {k} Value: {v}")
