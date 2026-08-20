# def formatName(s):
#     return " ".join(map(str.capitalize, s.split()))

def formatName(s):
    name_detail = s.split()
    name = ""
    for word in name_detail:
        name += word.capitalize() + " "
    return name.strip()

if __name__ == "__main__":
    s = input()
    print(formatName(s))