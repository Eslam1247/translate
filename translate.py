def translate(str):
    translation = ""
    for letter in str:
        if letter in "AEUIOaeuio":
            translation = translation + "z"
        else:
            translation = translation + letter
    return translation           

print(translate(input(" enter your phrease ")))    