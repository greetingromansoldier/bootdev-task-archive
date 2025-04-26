string = "my!! dear friend#2 2"
new_string = []
for character in string:
    character *= 2
    new_string.append(character)

sentence = "".join(new_string)
print(string)
print(new_string)
print(sentence)
