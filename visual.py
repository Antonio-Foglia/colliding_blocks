import turtle
import time
import pyautogui as pui

WALL = 0

SHIFT = -300

SCALE = 30

VCONST = (0.36/5+0.735/10)/2


def main2(box1, box2, realspeed = False, simspeed = 1):

    if realspeed:
        box1['v']*=VCONST*simspeed
        box2['v']*=VCONST*simspeed

    curr_wall = WALL*100+SHIFT

    collisions = 0


    wn = turtle.Screen()
    wn.clear()
    wn.bgcolor("black")
    wn.title("Blocks")

    if realspeed:
        

    label = turtle.Turtle()
    label.penup()
    label.hideturtle()
    label.color("white")
    label.goto(200,270)
    label.write("Collisions: {}".format(collisions),
                move=False,
                align="left",
                font=("Deja Vu Sans Mono", 15, "normal"))


    mlabel = turtle.Turtle()
    mlabel.penup()
    mlabel.hideturtle()
    mlabel.color("green")
    mlabel.goto(-200,270)
    mlabel.write("green mass: {} kg \ngreen speed: {} m/s".format(box1['m'],round(box1['v']/(VCONST*simspeed) if realspeed else box1['v'],2)),
                 move=False,
                 align="left",
                 font=("Deja Vu Sans Mono", 15, "normal"))

    mlabel.color("blue")
    mlabel.goto(0,270)
    mlabel.write("blue mass: {} kg \nblue speed: {} m/s".format(box2['m'],round(box2['v']/(VCONST*simspeed) if realspeed else box2['v'],2)),
                 move=False,
                 align="left",
                 font=("Deja Vu Sans Mono", 15, "normal"))


    wall = turtle.Turtle()
    wall.color("white")
    wall.speed(0)
    wall.penup()
    wall.goto(300,0)
    wall.pendown()
    wall.goto(WALL*100+SHIFT, 0 )
    wall.goto(WALL*100+SHIFT, SCALE*10)
    wall.hideturtle()


    alabel = turtle.Turtle()
    alabel.hideturtle()
    alabel.color("white")
    alabel.speed(0)
    i = 0
    while i <= 600/SCALE:
        alabel.penup()
        alabel.goto(WALL*100+SHIFT+i*SCALE, 0)
        alabel.pendown()
        alabel.goto(WALL*100+SHIFT+i*SCALE, -SCALE/2)
        alabel.penup()
        alabel.goto(WALL*100+SHIFT+i*SCALE, -SCALE/2-15)
        alabel.write(i, move=False, align="left", font=("Deja Vu Sans Mono", 10, "normal"))
        i+=1

    b1 = turtle.Turtle()
    b1.shape("square")
    b1.shapesize(stretch_wid=box1['w']/2*SCALE/10, stretch_len=box1['w']/2*SCALE/10, outline=None)
    b1.color("green")
    b1.penup()
    b1.speed(0)
    b1.goto( box1['x1']*SCALE + box1['w']/2*SCALE + SHIFT , box1['w']/2*SCALE )
    b1.dx = box1['v']*SCALE/30


    b2 = turtle.Turtle()
    b2.shape("square")
    b2.shapesize(stretch_wid=box2['w']/2*SCALE/10, stretch_len=box2['w']/2*SCALE/10, outline=None)
    b2.color("blue")
    b2.penup()
    b2.speed(0)
    b2.goto( box2['x1']*SCALE + box2['w']/2*SCALE + SHIFT , box2['w']/2*SCALE )
    b2.dx = box2['v']*SCALE/30

    wn.tracer(0)

    while True:

        wn.update()

        old_coll = collisions
        old_v = (box1['v'], box2['v'])

        b1.setx(b1.xcor() + b1.dx)
        b2.setx(b2.xcor() + b2.dx)

        box1['x1']= b1.xcor()/SCALE - box1['w']/2 - SHIFT/SCALE
        box2['x1']= b2.xcor()/SCALE - box2['w']/2 - SHIFT/SCALE


        if box1['x1'] <= WALL:
            box1 = collision_with_wall(box1)
            b1.dx = box1['v']*SCALE/30
            collisions += 1

        if box2['x1'] <= WALL:
            box2 = collision_with_wall(box2)
            b2.dx = box2['v']*SCALE/30
            collisions += 1


        if box1['x1']+box1['w'] >= box2['x1']:
            box1, box2 = collision(box1, box2)
            b1.dx = box1['v']*SCALE/30
            b2.dx = box2['v']*SCALE/30

            collisions += 1

        if old_coll != collisions:
            label.clear()
            label.write("Collisions: {}".format(collisions),
                        move=False,
                        align="left",
                        font=("Deja Vu Sans Mono", 15, "normal"))

        if old_v != (box1['v'], box2['v']):
            mlabel.clear()
            mlabel.color("green")
            mlabel.goto(-200,270)
            mlabel.write("green mass: {} kg \ngreen speed: {} m/s".format(box1['m'],round(box1['v']/(VCONST*simspeed) if realspeed else box1['v'],2)),
                         move=False,
                         align="left",
                         font=("Deja Vu Sans Mono", 15, "normal"))
            mlabel.color("blue")
            mlabel.goto(0,270)
            mlabel.write("blue mass: {} kg \nblue speed: {} m/s".format(box2['m'],round(box2['v']/(VCONST*simspeed) if realspeed else box2['v'],2)),
                         move=False,
                         align="left",
                         font=("Deja Vu Sans Mono", 15, "normal"))


        if box1['x1']*SCALE+ SHIFT > 350 or ( box2['x1']*SCALE+ SHIFT > 350 and box1['v'] == 0 ):
            break

    wn.mainloop()


    if realspeed:
        box1['v']/= (VCONST*simspeed)
        box2['v']/= (VCONST*simspeed)


    return box1,box2,collisions


def collision_with_wall(box):
    box['v'] *= -1
    return box



def collision(box1, box2):

    m1 = box1['m']
    m2 = box2['m']
    u1 = box1['v']
    u2 = box2['v']

    box1['v']= (m1-m2)/(m1+m2) * u1 + 2*m2/(m1+m2) * u2

    box2['v']= (m2-m1)/(m1+m2) * u2 + 2*m1/(m1+m2) * u1

    return box1,box2


def bxs(error = True):

    box1 = None
    box2 = None

    proceed = True

    while error:

        error = False

        try:
            l1 = pui.prompt(text='Enter the following for box 1 separated by a space: \nx-coordinate (m) \nwidth (m) \nvelocity (m/s) \nmass (kg)', title='BOX1' , default='5 1 0 1').split()
            l2 = pui.prompt(text='Enter the following for box 2 separated by a space: \nx-coordinate (m) \nwidth (m) \nvelocity (m/s) \nmass (kg)', title='BOX2' , default='10 4 -2 100').split()

            box1 = {'x1': int(l1[0]) , 'w': int(l1[1]), 'v' : int(l1[2]) , 'm': int(l1[3]) }
            box2 = {'x1': int(l2[0]) , 'w': int(l2[1]), 'v' : int(l2[2]) , 'm': int(l2[3]) }
        except:
            if pui.confirm('You made a mistake, try filling in the details again or press cancel to exit')  == 'Cancel':
                error = False
                proceed = False
            else:
                error = True

    return box1,box2,proceed




def main():

    box1, box2, proceed = bxs()
    if not proceed:
        return 'Finito'

    a = pui.prompt(text='Enter simulation speed (e.g. 0.5 for half the speed)', title='Simualtion speed' , default='1')

    try:
        main2(box1,box2, realspeed=True, simspeed = float(a.replace(" ","")) if a is not None else 1  )
        return  'Finito'
    except:
        return 'Finito'

    '''
    while True:
        box1, box2, proceed = bxs()

        if not proceed:
            return 'Done'

        try:
          main2(box1,box2,realspeed=True)
        except:
            None

        print(box1,box2)

        if pui.confirm('Press OK if you want to go again, otherwise press Cancel') == 'Cancel':
            return 'Done'
    '''


if __name__ == "__main__":
    print(main())
