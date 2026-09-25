text = ""
listTexts = []
while True:
    try:
        line = input()
        if line == "": break
        for word in line.split():
            c = word[len(word) - 1]
            if c == "." or c == "?" or c == "!":
                text += word[0:len(word) - 1]
                listTexts.append(text)
                text = ""
            else:
                text += word + " "
    except EOFError:
        break

for i in range(len(listTexts)):
    print(listTexts[i].capitalize())
