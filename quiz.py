import pgzrun

TITLE = "Quiz_Master"

WIDTH  = 685
HEIGHT = 500

markquee_box =Rect(0,0,850,50)
quebox=Rect(10,70,500,100)
timerbox=Rect(550,70,120,100)
skipbox=Rect(550,190,120,700)
answerbox1=Rect(10,180,120,120)
answerbox2=Rect(10,320,120,120)
answerbox3=Rect(330,180,120,120)
answerbox4=Rect(330,320,120,120)


def draw():
    screen.clear()
    screen.draw.filled_rect(markquee_box,"red")
    screen.draw.filled_rect(quebox,"aqua")
    screen.draw.filled_rect(timerbox,"green")
    screen.draw.filled_rect(skipbox,"yellow")
    screen.draw.filled_rect(answerbox1,"orange")
    screen.draw.filled_rect(answerbox2,"orange")
    screen.draw.filled_rect(answerbox3,"orange")
    screen.draw.filled_rect(answerbox4,"orange")











































































pgzrun.go()