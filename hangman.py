from appJar import gui
import random

app = gui("oof hangman")
app.setSticky("news")
app.setExpand("both")
app.setFont(20)

words = ["hanging", "human", "pneumonoultramicroscopicsilicovolcanoconiosis", "supercalifragilisticexpialidocious, "]


def start(btn):
    stuff = random.choice(words)
    print(stuff)

def press(btn):
    app.playSound("roblox-death-sound-effect.wav")

if __name__ == "__main__":
    app.addButton("start", start)
    app.addButton("A", press, 1, 0)
    app.addButton("B", press, 1, 2)
    app.addButton("C", press, 1, 4)
    app.addButton("D", press, 2, 0)
    app.addButton("E", press, 2, 2)
    app.addButton("F", press, 2, 4)
    app.addButton("G", press, 3, 0)
    app.addButton("H", press, 3, 2)
    app.addButton("I", press, 3, 4)
    app.addButton("J", press, 4, 0)
    app.addButton("K", press, 4, 2)
    app.addButton("L", press, 4, 4)
    app.addButton("M", press, 5, 0)
    app.addButton("N", press, 5, 2)
    app.addButton("O", press, 5, 4)
    app.addButton("P", press, 6, 0)
    app.addButton("Q", press, 6, 2)
    app.addButton("R", press, 6, 4)
    app.addButton("S", press, 7, 0)
    app.addButton("T", press, 7, 2)
    app.addButton("U", press, 7, 4)
    app.addButton("V", press, 8, 0)
    app.addButton("W", press, 8, 2)
    app.addButton("X", press, 8, 4)
    app.addButton("Y", press, 9, 0)
    app.addButton("Z", press, 9, 2)




    app.go()

