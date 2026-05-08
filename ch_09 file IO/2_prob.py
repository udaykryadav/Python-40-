import random
def game():
    print("you are playing the game..")
    score = random.randint(1,62)
    # fetch high score
    with open("2highScore.txt") as f:
        highscore=f.read()
        if(highscore != ""):
            highscore = int(highscore)
        else:
            highscore = 0 
    print(f"your score: {score}")
    print(f'your current high scrre {highscore}')
        
    if(score>highscore):
        #write new highscroe in file 
        with open("2highScore.txt",'w') as f:
            f.write(str(score))    
    return score

game()