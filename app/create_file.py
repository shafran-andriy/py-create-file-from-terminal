import time
import argparse
import os


named_tuple = time.localtime()  # get struct_time
time_string = time.strftime("%m-%d-%Y, %H:%M:%S", named_tuple)
parser = argparse.ArgumentParser()
parser.add_argument("-d", nargs="+", required=False)
parser.add_argument("-f", nargs="+", required=False)
args = parser.parse_args()
dirs = args.d
file_name = args.f


def create_file() -> None:
    with open("file.txt", "w") as file:
        pass
    with open("file.txt", "a+") as file:
        file.write(f"{time_string}\n")
    line = ""
    count = 1
    while line != "stop":
        line = input(f"Enter content line: Line{count} content")
        if line == "stop":
            break
        with open("file.txt", "a+") as file:
            file.write(f"{count} Line{count} content\n")
        count += 1


def create_dirs() -> None:
    os.makedirs(os.path.join(*dirs), exist_ok=True)


if args.f is None:
    create_dirs()
else:
    if args.d is None:
        create_file()
    else:
        create_dirs()
        os.chdir(os.path.join(*dirs))
        create_file()
