import time

'''the coordinate of the wall'''
WALL = 0

'''
boxes are dictionaries that contain:
* x coordinate of lower left corner: x1
* width: w
* velocity: v
* mass: m

main function parameters:
* 2 boxes
* realtime:
    whether the user wants to the simulation to run in real time
* simtime:
    the amount of time to run the simulation for
* interval:
    the time elapsed between updates
'''

def main(box1, box2,realtime=False, sim_time = float('inf'), interval=0.0001):

    '''total time elapsed'''
    t = interval
    collisions = 0
    if realtime:
        print('Collisions: {}'.format(collisions),end = "\r")

    while t < sim_time:

        #start = time.time()

        '''move the boxes to the new position in interval'''
        box1 = move(box1, interval)
        box2 = move(box2, interval)
        t += interval

        '''check and solve for collision between box1 and WALL'''
        if box1['x1'] <= WALL:
            box1 = collision_with_wall(box1)
            collisions += 1
            if realtime:
                print('Collisions: {}'.format(collisions),end = "\r")
                #print('box1: {} \nbox2: {}'.format(box1,box2))
                #print(str(collisions) + "(wall)" ,end = "\r")

        '''check and solve for collision between box2 and WALL'''
        if box2['x1'] <= WALL:
            box2 = collision_with_wall(box2)
            collisions += 1
            if realtime:
                print('Collisions: {}'.format(collisions),end = "\r")
                #print('box1: {} \nbox2: {}'.format(box1,box2))

        '''check and solve for collsion between two boxes'''
        if box1['x1']+box1['w'] >= box2['x1']:
            box1, box2 = collision(box1, box2)
            collisions += 1
            if realtime:
                print('Collisions: {}'.format(collisions),end = "\r")
                #print('box1: {} \nbox2: {}'.format(box1,box2))
                #print(str(collisions) + "(boxs)" ,end = "\r")

        '''check if any further collsions are going to happen'''
        if terminal(box1,box2):
            return box1,box2,collisions


        '''if realtime, stop the simulation for the given interval'''
        #end = time.time()
        if realtime:
            #if interval-(end - start) > 0:
                time.sleep(interval)#-(end - start))

    return box1,box2,collisions

'''updates the position of a box given the velocity'''
def move( box , interval):
    box['x1'] = box['x1'] + box['v'] * interval
    return box

'''perfectly elastic collision with wall'''
def collision_with_wall(box):
    #box['x1'] = WALL
    box['v'] *= -1
    return box

'''perfectly elastic ollisions between blocks'''
def collision(box1, box2):

    m1 = box1['m']
    m2 = box2['m']
    u1 = box1['v']
    u2 = box2['v']

    '''solving equations using momentum and kinetic energy'''
    box1['v']= (m1-m2)/(m1+m2) * u1 + 2*m2/(m1+m2) * u2

    box2['v']= (m2-m1)/(m1+m2) * u2 + 2*m1/(m1+m2) * u1


    return box1,box2

'''check for the terminal state'''
def terminal(box1,box2):

    if box2['v'] >= box1['v'] and box1['v'] >= 0 and box2['v'] > 0:
        return True

    return False



'''if b1 and b2 are powers of 100, the total collisions will be equal to the digits of pi'''
i = float(input('What power of 100? '))
b1 ={'x1':5 , 'w': 1, 'v' : 0 , 'm': 1 }
b2 = {'x1':10 , 'w': 2, 'v' : -2, 'm': 100**i }
o = True if input('Realtime? (y/n) ') == 'y' else False
start = time.time()
res = main(b1,b2,realtime = o,interval = 10**(-i-1) if i > 3 else 0.0001)
end = time.time()
print('BOX1:{} \nBOX2: {} \nCollisions: {} \nRuntime: {}s'.format(res[0],res[1],res[2],end-start))
