#!/usr/bin/env python
from ants import *

# define a class with a do_turn method
# the Ants.run method will parse and update bot input
# it will also run the do_turn method for us

FILEPATH1 = "4new_loc.txt"
def my_log(FILEPATH1, content):
    f = open(FILEPATH1, "a")
    f.write(content)
    f.close()
FILEPATH2 = "4direction_log.txt"
def mi_log(FILEPATH2, content):
  m = open(FILEPATH2, "a")
	m.write(content)
	m.close()
FILEPATH3 = "4antloc_log.txt"
def ant_log(FILEPATH3, content):
	a = open(FILEPATH3, "a")
	a.write(content)
	a.close()
FILEPATH4 = "4unseenloc_log.txt"
def unseen_log(FILEPATH4, content):
	b = open(FILEPATH4, "a")
	b.write(content)
	b.close()
FILEPATH5 = "4unseendist_log.txt"
def unseendist_log(FILEPATH5, content):
	b = open(FILEPATH5, "a")
	b.write(content)
	b.close()
FILEPATH6 = "4dist_log.txt"
def dist_log(FILEPATH6, content):
	b = open(FILEPATH6, "a")
	b.write(content)
	b.close()


class MyBot:
    def __init__(self):
        # define class level variables, will be remembered between turns
        pass
    
    # do_setup is run once at the start of the game
    # after the bot has received the game settings
    # the ants class is created and setup by the Ants.run method
    def do_setup(self, ants):
        self.hills = []

        # initialize data structures after learning the game settings
        pass

        self.unseen = []
        for row in range(ants.rows):
            for col in range(ants.cols):
                self.unseen.append((row, col))
    
    def do_turn(self, ants):
        # track all moves, prevent collisions
        orders = {}
        def do_move_direction(loc, direction):
            new_loc = ants.destination(loc, direction)
            if (ants.unoccupied(new_loc) and new_loc not in orders):
                ants.issue_order((loc, direction))
                orders[new_loc] = loc
                return True
            else:
                return False
        targets = {}

        def do_move_aster(loc, dest):
            new_loc = ants.aster(loc, dest)
            try:
                d = (new_loc[0][0] - ant_loc[0], new_loc[0][1] - ant_loc[1])
                if d == (-1, 0):
                    direction = 'n'
                elif d == (0, 1):
                    direction = 'e'
                elif d == (1, 0):
                    direction = 's'
                elif d == (0, -1):
                    direction = 'w'
                else:
                    direction ='e'    
                
                if do_move_direction(loc, direction):
                	targets[dest] = loc
                        return True
                else:
            	    return False
            except:
                 my_log(FILEPATH1, "%s\n\n\n\n\n" % str(new_loc))
                 do_move_location(loc, dest)
            
            """new_loc = ants.destination(loc, direction)
            if (ants.unoccupied(new_loc) and new_loc not in orders):
                ants.issue_order((loc, direction))
                orders[new_loc] = loc
                targets[dest] = loc
                return True
            else:
                return False"""

        def do_move_location(loc, dest):
            directions = ants.direction(loc, dest)
            for direction in directions:
                if do_move_direction(loc, direction):
                    targets[dest] = loc
                    return True
            return False

        # prevent stepping on own hill
        for hill_loc in ants.my_hills():
            orders[hill_loc] = None


        # find close food
        ant_dist = []
        for food_loc in ants.food():
            for ant_loc in ants.my_ants():
                dist = ants.distance(ant_loc, food_loc)
                ant_dist.append((dist, ant_loc, food_loc))
        ant_dist.sort()
        for dist, ant_loc, food_loc in ant_dist:
            if food_loc not in targets and ant_loc not in targets.values():
                #do_move_location(ant_loc, food_loc)
                do_move_aster(ant_loc, food_loc)
                """new_loc = ants.aster(ant_loc, food_loc)
                ant_log(FILEPATH3, "%s\n\n\n\n" % str(ant_loc))
                my_log(FILEPATH1, "%s\n\n\n\n\n" % str(new_loc))
                d = (new_loc[0][0] - ant_loc[0], new_loc[0][1] - ant_loc[1])
                if d == (-1, 0):
                    direction = 'n'
                elif d == (0, 1):
                    direction = 'e'
                elif d == (1, 0):
                    direction = 's'
                elif d == (0, -1):
                    direction = 'w'
                mi_log(FILEPATH2, "%s\n\n\n\n" % str(direction))
                if (ants.unoccupied(new_loc[0]) and new_loc[0] not in orders):
                    ants.issue_order((ant_loc, direction))
                    orders[new_loc[0]] = ant_loc
                    targets[food_loc] = ant_loc
                    return True
                else:
                    return False"""


        
        # attack hills
        for hill_loc, hill_owner in ants.enemy_hills():
            if hill_loc not in self.hills:
                self.hills.append(hill_loc)
        ant_dist = []
        for hill_loc in self.hills:
            for ant_loc in ants.my_ants():
                if ant_loc not in orders.values():
                    dist = ants.distance(ant_loc, hill_loc)
                    ant_dist.append((dist, ant_loc, hill_loc))
        ant_dist.sort()
        for dist, ant_loc, hill_loc in ant_dist:
            #do_move_location(ant_loc, hill_loc)
            do_move_aster(ant_loc, hill_loc)
            """ants.aster(ant_loc, hill_loc)
            new_loc = ants.aster(ant_loc, food_loc)
            d = (new_loc[0][0] - ant_loc[0], new_loc[0][1] - ant_loc[1])
            if d == (-1, 0):
                direction = 'n'
            elif d == (0, 1):
                direction = 'e'
            elif d == (1, 0):
                direction = 's'
            elif d == (0, -1):
                direction = 'w'

            if (ants.unoccupied(new_loc[0]) and new_loc[0] not in orders):
                ants.issue_order((loc, direction))
                orders[new_loc[0]] = loc
                targets[hill_loc] = ant_loc
                return True
            else:
                return False"""

        # explore unseen areas
        for loc in self.unseen[:]:
            if ants.visible(loc):
                self.unseen.remove(loc)
        for ant_loc in ants.my_ants():
            if ant_loc not in orders.values():
                unseen_dist = []
                for unseen_loc in self.unseen:
                    dist = ants.distance(ant_loc, unseen_loc)
                    unseen_dist.append((dist, unseen_loc))
                unseen_dist.sort()
                #u = unseen_dist[0][1]
                for unseen_loc in unseen_dist:
                    unseen_log(FILEPATH4, "%s\n\n" % str(unseen_loc))
                    unseendist_log(FILEPATH5, "%s\n\n" % str(unseen_dist))

                    
                    if do_move_aster(ant_loc, unseen_loc):
                       #do_move_location(ant_loc, unseen_loc):

                        break

        # unblock own hill
        for hill_loc in ants.my_hills():
            if hill_loc in ants.my_ants() and hill_loc not in orders.values():
                for direction in ('s','e','w','n'):
                    if do_move_direction(hill_loc, direction):
                        break
        

         


            
if __name__ == '__main__':
    # psyco will speed up python a little, but is not needed
    
    try:
        import psyco
        psyco.full()
    except ImportError:
        pass
    
    try:
        # if run is passed a class with a do_turn method, it will do the work
        # this is not needed, in which case you will need to write your own
        # parsing function and your own game state class
        print "hello"
        Ants.run(MyBot())
        
    except KeyboardInterrupt:
        print('ctrl-c, leaving ...')
