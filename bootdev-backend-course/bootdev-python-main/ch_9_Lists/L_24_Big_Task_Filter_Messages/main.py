# code before changes:

# def filter_messages(messages):
#     pass

# assignment:

# (link for a lesson because a lot of essential stuff is laying there 
#  https://www.boot.dev/lessons/1d9bbaf7-f597-497d-aebd-4662097ef2f7)

# We need to filter the profanity out of our game's live chat feature! 

# Complete the filter_messages function. It takes a list of chat messages as input and returns 2 new lists:

# A list of the same messages but with all instances of the word dang removed.
# A list containing the number of dang words that were removed from the message at that particular index.

# Here are some examples:

# messages = ["dang it bobby!", "look at it go"]
# filter_messages(messages) 
# # returns ["it bobby!", "look at it go"], [1, 0]

# messages2 = ["That's the bloody dang Reaper of Mars...", "Pax au Telemanus!", "I was never taught how to use a dang razor!"]
# filter_messages(messages2) 
# # returns ["That's the bloody Reaper of Mars...", "Pax au Telemanus!", "I was never taught how to use a razor!"], [1, 0, 1]

# actual code:

def filter_messages(messages):
    filtered_messages = []
    counted_words = []

    splitted_messages = []

    for message in messages:
        message = message.split()
        splitted_messages.append(message)

        non_bad_words = []
        counter = 0

        for word in message:
            if word == "dang":
                counter += 1
            else:
                non_bad_words.append(word)
                message = " ".join(non_bad_words)
                
        filtered_messages.append(message) # ВОООООТ ЗДЕСЬ мы разделяем сообщения, тем что вкидываем сообщение из текущего цикла в список с отфильтрованными!!!! ЭВРИКА
        counted_words.append(counter)

    return filtered_messages, counted_words


# мои инпуты для теста:

# messages = ["dang it bobby!", 
#             "look at it go", 
#             "That's the bloody dang Reaper of Mars...", 
#             "Pax au Telemanus!", 
#             "I was never taught how to use a dang razor!"
#             ]

# print(filter_messages(messages))

# если честно это было пиздец как трудно нахуй
# и я до сих пор не вполне понимаю как оно получилось
# смог нормально сделать только когда прямо пошёл по гайду, но это почти магия ебаная, у меня в голове оно не укладывается
# типо по сути своей реально помогло то, что делаешь по маленьким шажкам и маленькие шажки же и дебажишь сразу, пробуешь