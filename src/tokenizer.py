import re


def load_file(filename: str) -> str:
    with open(filename, "r") as f:
        x = f.readlines()

    return x


def _whitespace_filter(data):
    filtered = []
    for i in range(len(data)):
        datas = re.sub(' +', ' ', data[i]).replace("\n", "")

        if datas != '':
            filtered.append("".join(datas))

    return filtered


def tokenize(data):
    print("".join(_whitespace_filter(data)))
    