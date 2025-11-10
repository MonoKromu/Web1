import argparse


def format_text_block(frame_width: int, frame_height: int, file_name: str):
    lines = []
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            text = file.read()
            start_index = 1
            for _ in range(frame_height):
                end_index = start_index + frame_width
                if end_index == len(text):
                    lines.append(text[start_index:])
                    break
                line = text[start_index:end_index]
                newline = line.find("\n")
                if newline == -1:
                    start_index = end_index
                else:
                    line = line[0:newline]
                    start_index += newline + 1
                lines.append(line)
    except FileNotFoundError as e:
        return str(e)
    return "\n".join(lines)


def get_args():
    parser = argparse.ArgumentParser()
    parser.description = "Prints formatted text from file"
    parser.add_argument("--frame_width", required=True, type=int)
    parser.add_argument("--frame_height", required=True, type=int)
    parser.add_argument("filename", type=str)
    return parser.parse_args()


args = get_args()
print(format_text_block(args.frame_width, args.frame_height, args.filename))
