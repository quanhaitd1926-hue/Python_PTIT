def formatBirth(s):
    date = s.split("/")
    return date[0].zfill(2) + "/" + date[1].zfill(2) + "/" + date[2]

if __name__ == "__main__":
    s = input()
    print(formatBirth(s))