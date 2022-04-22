import emoji

w = input("")

word = w.strip()

if (word == "Hello :)"):
    print("Hello", "\N{slightly smiling face}")
elif (word == "Goodbye :("):
    print("Goodbye", "\N{slightly frowning face}")
elif(word == "Hello :) Goodbye :("):
    print("Hello","\N{slightly smiling face}", "Goodbye","\N{slightly frowning face}")