def convertor(message):
    words = message.split(" ")
    emojis = {
        ":)": "☺",
        ":(": "🐱"
    }
    output = ""
    for word in words:
        output +=emojis.get(word,word) + " "
    return output


message = input("> ")
print(convertor(message))
