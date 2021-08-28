import sys

#python3 game.py sample_paths.txt sample_items.txt sample_chasers.txt sample_exits.txt

from creature import Creature
from item import Item
from location import Location
from preprocessing import process_locations, process_exits,\
                          process_items, process_creatures,\
                          process_directions,\
                          draw_map, move #two new functions to draw map and move

# ===============================================
# CHECK CONFIGURATION FILES
if len(sys.argv) < 5:
    print('Usage: python3 game.py <PATHS> <ITEMS> <CHASERS> <EXITS>')
    quit()
    
#get something be returned as variables
locations_list = process_locations(sys.argv[1])
items_list = process_items(sys.argv[2],locations_list)
chasers_list = process_creatures(sys.argv[3],locations_list)
exits_list = process_exits(sys.argv[4],locations_list)
process_directions(sys.argv[1], locations_list)

#Draw a initial map
draw_map(locations_list[0],locations_list,items_list,exits_list)

# CREAT PLAYER WITHIN Creature Class and initialize the current location
current_location = locations_list[0] 
player = Creature('goose', None, 5, current_location, None)

# ASK FOR COMMANDs
while True:
#Make command case-insensitive
    print()
    command = input('>> ').upper()

    #command - quit
    if command == 'QUIT':
        print('Game terminated.')
        quit()
        
    #command - help
    elif command == 'HELP':
        print('HELP            - Shows some available commands.')
        print('INV             - Lists all the items in your inventory.')
        print('TAKE <ITEM>     - Takes an item from your current location.')
        print('DROP <ITEM>     - Drops an item at your current location.')
        print('')
        print('LOOK or L       - Lets you see the map/location again.')
        print('LOOK <ITEM>     - Lets you see an item in more detail.')
        print('LOOK ME         - Sometimes, you just have to admire the feathers.')
        print('LOOK <CREATURE> - Sizes up a nearby creature.')
        print('LOOK HERE       - Shows a list of all items in the room.')
        print('')
        print('NORTHWEST or NW - Moves you to the northwest.')
        print('NORTH or N      - Moves you to the north.')
        print('NORTHEAST or NE - Moves you to the northeast.')
        print('EAST or E       - Moves you to the east.')
        print('')
        print('SOUTHEAST or SE - Moves you to the southeast.')
        print('SOUTH or S      - Moves you to the south.')
        print('SOUTHWEST or SW - Moves you to the southwest.')
        print('WEST or W       - Moves you to the west.')
        print('')
        print('FLEE            - Attempt to flee from your current location.')
        print('HONK or Y       - Attempt to scare off all creatures in the same location.')
        print('WAIT            - Do nothing. All other creatures will move around you.')
        print('QUIT            - Ends the game. No questions asked.')
        
    #command - look me
    elif command == 'LOOK ME':
        print('You are a goose. You are probably quite terrifying.')
        print(f'In fact, you have a terror rating of: {player.terror_rating}')
        
    #command - inv (three different conditions)
    elif command == 'INV':
        if len(player.creature_items_list) == 0:
            print('You are carrying nothing.')
        if len(player.creature_items_list) == 1:
            print('You, a goose, are carrying the following item:')
            print(f' - {player.creature_items_list[0].item_name}')
        if len(player.creature_items_list) > 1:
            print('You, a goose, are carrying the following items:')
            i = 0
            while i < len(player.creature_items_list):
                print(f' - {player.creature_items_list[i].item_name}')
                i += 1
                
    #command - look current location
    elif command == 'LOOK' or command == 'L':
        draw_map(current_location,locations_list,items_list,exits_list)
        
    #command - move northwest
    elif command == 'NW' or command == 'NORTHWEST':
        for chaser in chasers_list:
            chaser.caught_times = 1
        if current_location.destinations_list[0] == None:
            print('You can\'t go that way.')
        else:
            print(f'You move northwest, to {current_location.destinations_list[0].name}.')
            #detect for all creatures exsit and make it move
            for location in locations_list:
                if current_location.destinations_list[0].name == location.name:
                    current_location = location
                    #costly actions make chaser move
                    for chaser in chasers_list:
                        move(chaser,player,current_location,locations_list)
                    break
            draw_map(current_location,locations_list,items_list,exits_list)
        
    #command - move north
    elif command == 'N' or command == 'NORTH':
        for chaser in chasers_list:
            chaser.caught_times = 1
        if current_location.destinations_list[1] == None:
            print('You can\'t go that way.')
        else:
            print(f'You move north, to {current_location.destinations_list[1].name}.')
            #detect for all creatures exsit and make it move
            for location in locations_list:
                if current_location.destinations_list[1].name == location.name:
                    current_location = location
                    #costly actions make chaser move
                    for chaser in chasers_list:
                        move(chaser,player,current_location,locations_list)
                    break
            draw_map(current_location,locations_list,items_list,exits_list)
            
    #command - move northeast
    elif command == 'NE' or command == 'NORTHEAST':
        for chaser in chasers_list:
            chaser.caught_times = 1
        if current_location.destinations_list[2] == None:
            print('You can\'t go that way.')
        else:
            print(f'You move northeast, to {current_location.destinations_list[2].name}.')
            #detect for all creatures exsit and make it move
            for location in locations_list:
                if current_location.destinations_list[2].name == location.name:
                    current_location = location
                    #costly actions make chaser move
                    for chaser in chasers_list:
                        move(chaser,player,current_location,locations_list)
                    break
            draw_map(current_location,locations_list,items_list,exits_list)
            
    #command - move east
    elif command == 'E' or command == 'EAST':
        for chaser in chasers_list:
            chaser.caught_times = 1
        if current_location.destinations_list[3] == None:
            print('You can\'t go that way.')
        else:
            print(f'You move east, to {current_location.destinations_list[3].name}.')
            #detect for all creatures exsit and make it move
            for location in locations_list:
                if current_location.destinations_list[3].name == location.name:
                    current_location = location
                    #costly actions make chaser move
                    for chaser in chasers_list:
                        move(chaser,player,current_location,locations_list)
                    break
            draw_map(current_location,locations_list,items_list,exits_list)
            
    #command - move southeast
    elif command == 'SE' or command == 'SOUTHEAST':
        for chaser in chasers_list:
            chaser.caught_times = 1
        if current_location.destinations_list[4] == None:
            print('You can\'t go that way.')
        else:
            print(f'You move southeast, to {current_location.destinations_list[4].name}.')
            #detect for all creatures exsit and make it move
            for location in locations_list:
                if current_location.destinations_list[4].name == location.name:
                    current_location = location
                    #costly actions make chaser move
                    for chaser in chasers_list:
                        move(chaser,player,current_location,locations_list)
                    break
            draw_map(current_location,locations_list,items_list,exits_list)
            
    #command - move south
    elif command == 'S' or command == 'SOUTH':
        for chaser in chasers_list:
            chaser.caught_times = 1
        if current_location.destinations_list[5] == None:
            print('You can\'t go that way.')
        else:
            print(f'You move south, to {current_location.destinations_list[5].name}.')
            #detect for all creatures exsit and make it move
            i = 0
            for location in locations_list:
                if current_location.destinations_list[5].name == location.name:
                    current_location = location
                    #costly actions make chaser move
                    for chaser in chasers_list:
                        move(chaser,player,current_location,locations_list)
                    break
            draw_map(current_location,locations_list,items_list,exits_list)
            
    #command - move southwest
    elif command == 'SW' or command == 'SOUTHWEST':
        for chaser in chasers_list:
            chaser.caught_times = 1
        if current_location.destinations_list[6] == None:
            print('You can\'t go that way.')
        else:
            print(f'You move southwest, to {current_location.destinations_list[6].name}.')
            #detect for all creatures exsit and make it move
            for location in locations_list:
                if current_location.destinations_list[6].name == location.name:
                    current_location = location
                    #costly actions make chaser move
                    for chaser in chasers_list:
                        move(chaser,player,current_location,locations_list)
                    break
            draw_map(current_location,locations_list,items_list,exits_list)
            
    #command - move west
    elif command == 'W' or command == 'WEST':
        for chaser in chasers_list:
            chaser.caught_times = 1
        if current_location.destinations_list[7] == None:
            print('You can\'t go that way.')
        else:
            print(f'You move west, to {current_location.destinations_list[7].name}.')
            #detect for all creatures exsit and make it move
            for location in locations_list:
                if current_location.destinations_list[7].name == location.name:
                    current_location = location
                    #costly actions make chaser move
                    for chaser in chasers_list:
                        move(chaser,player,current_location,locations_list)
                    break
            draw_map(current_location,locations_list,items_list,exits_list)
            
    #command - look here
    elif command == 'LOOK HERE':
        space = ' '
        items = current_location.location_items_list
        #detect items for current location
        if len(items) == 0:
            print('There is nothing here.')
        else:
            i = 0
            j = 0
            while i < len(current_location.location_items_list):
                while j < len(items_list):
                    if current_location.location_items_list[i] == items_list[j].short_name:
                        current_location.location_items_list[i] = items_list[j]
                    j += 1
                    print(f'{current_location.location_items_list[i].short_name.upper()}{space*(16-len(current_location.location_items_list[i].short_name))}| {current_location.location_items_list[i].item_name}')
                    break
                i += 1
                
    #command - take something
    elif command.upper().split()[0] =='TAKE':
        com = command.lower().split()
        found = False 
        for item in current_location.location_items_list:
            item_name = item.short_name 
            if com[1] == item_name:
                print(f'You pick up the {item.item_name}.')
                player.take(item)
                current_location.remove_item(item)
                found = True
                #costly actions make chaser move
                for chaser in chasers_list:
                    move(chaser,player,current_location,locations_list)
        if not found:
            print('You don\'t see anything like that here.')
            
    #command - drop something
    elif command.upper().split()[0] =='DROP':
        com = command.lower().split()
        found = False
        for item in player.creature_items_list:
            if com[1] == item.short_name:
                print(f'You drop the {item.item_name}.')
                player.drop(item)
                current_location.add_item(item)
                found = True
                #costly action make chaser move
                for chaser in chasers_list:
                    move(chaser,player,current_location,locations_list)
        if not found:
            print('You don\'t have that in your inventory.')
    
    #command - look the item/chaser
    elif command.upper().split()[0] =='LOOK':
        com = command.lower().split()
        found = False
        #look for item in current_location
        for item in current_location.location_items_list:
            if com[1] == item.short_name:
                print(f'{item.item_name} - Terror Rating: {item.terror_rating}')
                found = True
        #look for item in inventory
        for item in player.creature_items_list:
            if com[1] == item.short_name:
                print(f'{item.item_name} - Terror Rating: {item.terror_rating}')
                found = True
        #look for chaser in the whole map
        for chaser in current_location.chasers_list:
            if com[1] == chaser.name.lower():
                if chaser.terror_rating - 5 >= player.terror_rating:
                    print(f'{chaser.name} doesn\'t seem very afraid of you.')
                    found = True
                elif player.terror_rating - 5 >= chaser.terror_rating:
                    print(f'{chaser.name} looks a little on-edge around you.')
                    found = True
                else:
                    print(f'Hmm. {chaser.name} is a bit hard to read.')
                    found = True
                    
        if not found:
            print('You don\'t see anything like that here.')
            
    #command - flee
    elif command == 'FLEE':
        if current_location.has_exit == True:
            print('You slip past the dastardly Goosechasers and run off into the wilderness! Freedom at last!')
            print('========= F R E E D O M =========')
            quit()
        else:
            print('There\'s nowhere you can run or hide! Find somewhere else to FLEE.')
            
    #command - honk
    elif command == 'HONK' or command == 'Y':
        #determine whether there is a chaser in current location
        if len(current_location.chasers_list) == 0:
            print('All shall quiver before the might of the goose! HONK!')
            continue
        print('You sneak up behind your quarry and honk with all the force of a really angry airhorn! HONK!')
        
        #determine whether or not chaser could be spooked
        for chaser in current_location.chasers_list:
            if player.terror_rating > chaser.terror_rating:
                print(f'{chaser.name} is spooked! They flee immediately!')
                chasers_list.remove(chaser)
            else:
                print(f'{chaser.name} is not spooked :(') 
                
        for chaser in current_location.chasers_list:
            if chaser not in chasers_list:
                current_location.chasers_list.remove(chaser)
                
        #alarming actions make chaser move
        for chaser in chasers_list:
            move(chaser,player,current_location,locations_list)
            
        if len(chasers_list) == 0:
            print()
            print('None can stand against the power of the goose!')
            print('========= V I C T O R Y =========')
            quit()
            
    #command - wait
    elif command == 'WAIT':
        print('You lie in wait.')
        for chaser in chasers_list:
            move(chaser,player,current_location,locations_list)
        
    #command - invalid
    else:
        print('You can\'t do that.')
# ===============================================
