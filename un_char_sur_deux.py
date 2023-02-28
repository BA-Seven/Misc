"""Besoin de faire du phishing avec une xss ? URLencode c'est bien mais le lien deviens vite long. URLencode un char sur 2 et ton url sera leggit pour l'average user."""



string = "Ceci est une chaîne à encoder"

encoded = ""

for i,char in enumerate(string):
    if i % 2 == 0:
        if char == " ":
            encoded += "%20"
        else:
            encoded += char
    else:
        encoded += "%{0:0>2}".format(format(ord(char), "x"))

print(encoded)
