file = open("chat_history.txt", "w",encoding="utf-8")

while True:
    user = input("You: ").lower()
    file.write("You: " + user + "\n")

    if user == "hello":
        reply = "Hi! How can I help you?"
    
    elif user == "how are you":
        reply = "I am fine "

    elif user == "bye":
        reply = "Goodbye!"
        print("Bot:", reply)
        file.write("Bot: " + reply + "\n")
        break

    else:
        reply = "Sorry, I don't understand"

    print("Bot:", reply)
    file.write("Bot: " + reply + "\n")

file.close()