def load_file(filename: str) -> str:
    with open(filename, "r") as f:
        x = f.readlines()

    return x

def tokenize(data):
    print(data)


print(load_file("question_1.xams"))
