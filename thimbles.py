#game thimbles
import random, time
def thimbles():
    return("Ben walks on a market. He have got 1000$. Ben sees man which shuffles a thimbles. Ben decides to approach for him...")
def thimblerigger_regulations():
    return("Hey, Ben. It's game which called thimbles! I'm shuffle this timbles and you should guess where there is a ball")
def base():
    many = 1000
    if many >= 100:
        print("I'm mix.....")
        time.sleep(3)
        rand = random.randint(1,3)
        print(rand)
        n = int(input("I'm mixing"))
        if n == rand:
            many+=100
            otv = input(f"You win! Do you want continue? Now you have got {many}$! y/n ")
            if otv == "y":
                return game()
            else:
                return "Good buy"
        else:
            many-=100
            otv = input(f"You not win! Do you want continue? Now you have got {many}$! y/n ")
            if otv == "y":
                return base()
            else:
                return "Good buy, Ben!"
    else:
        return "You don't have many"
def the_game():
    print(thimbles())
    print(thimblerigger_regulations())
    return base()


