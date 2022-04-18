def emoji_converter(message):
    words = message.split(' ')
    emojis = {
        ":)": "🙂",
        ":(": "🙁"
    }
    output_val = ""
    for word in words:
        output_val += emojis.get(word, word) + " "
    return output_val


message = input(">")
output = emoji_converter(message)
print(output)
