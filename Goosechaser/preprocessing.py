from creature import Creature
from item import Item
from location import Location

def process_locations(source):
    try:
        f = open(source,'r')
        lines = f.readlines()
        i = 0
        j = 0
        k = 0
        newlines = []
        locations_list = []
        if len(lines) == 0:
            print('The game cannot run without any rooms :(')
            quit()
        while i < len(lines):
            if lines[i] == '\n':
                pass
            else:
                newlines.append(lines[i].rstrip('\n').strip().split(' > '))
            i += 1
        while j < len(newlines):
            if newlines[j][0] not in locations_list:
                locations_list.append(newlines[j][0])
            if newlines[j][2] not in locations_list:
                locations_list.append(newlines[j][2])
            j += 1
        #make the location become an Object
        while k < len(locations_list):
            locations_list[k] = Location(locations_list[k])
            k += 1
        return locations_list
        f.close()
        
    except FileNotFoundError:
        print('You have specified an invalid configuration file.')
        quit()
        
def process_items(source, locations):
    try:
        f = open(source,'r')
        lines = f.readlines()
        i = 0
        j = 0
        newlines = []
        items_list = []
        while i < len(lines):
            if lines[i] == '\n':
                pass
            else:
                newlines.append(lines[i].rstrip('\n').split(' | '))
            i += 1
        while j < len(newlines):
            items_list.append(Item(newlines[j][0],newlines[j][1],newlines[j][2],int(newlines[j][3]),newlines[j][4]))
            k = 0
            while k < len(locations):
                if newlines[j][4] == locations[k].name:
                    #make it become Object
                    for i in range(len(items_list)):
                        if newlines[j][0] == items_list[i].short_name:
                            item = items_list[i]
                    locations[k].location_items_list.append(item)
                k += 1
            j += 1
        return items_list
        f.close()
        
    except FileNotFoundError:
        print('You have specified an invalid configuration file.')
        quit()
        
def process_creatures(source, locations):
    try:
        f = open(source,'r')
        lines = f.readlines()
        i = 0
        j = 0
        k = 0
        newlines = []
        chasers_list = []
        if len(lines) == 0:
            print('There is nothing chasing you!')
            quit()
        while i < len(lines):
            newlines.append(lines[i].rstrip('\n').split(' | '))
            i += 1
        while j < len(newlines):
            chasers_list.append(Creature(newlines[j][0],newlines[j][1],newlines[j][2],newlines[j][3],newlines[j][4]))
            k = 0
            while k < len(locations):
                if newlines[j][3] == locations[k].name:
                    #make it become Object
                    for i in range(len(chasers_list)):
                        if newlines[j][0] == chasers_list[i].name:
                            chaser = chasers_list[i]
                    locations[k].chasers_list.append(chaser)
                    #make the chaser's location become a Location class with attributes
                    for i in range(len(locations)):
                        if newlines[j][3] == locations[i].name:
                            chasers_list[j].location = locations[i]
                k += 1
            j += 1
        
        if len(chasers_list) == 0:
            print("There is nothing chasing you!")
            quit()
        return chasers_list
        f.close()
        
    except FileNotFoundError:
        print('You have specified an invalid configuration file.')
        quit()

def process_exits(source, locations):
    try:
        f = open(source,'r')
        lines = f.readlines()
        i = 0
        exits_list = []
        while i < len(lines):
            exits_list.append(lines[i].rstrip('\n'))
            i += 1
        for exit in locations:
            if exit.name in exits_list:
                exit.has_exit = True
        return exits_list
        f.close()
        
    except FileNotFoundError:
        print('You have specified an invalid configuration file.')
        quit()

#a new function used to process the directions and destinations
def process_directions(source, locations_list):
    try:
        f = open(source,'r')
        lines = f.readlines()
        i = 0
        j = 0
        k = 0
        newlines = []
        
        while i < len(lines):
            if lines[i] == '\n':
                pass
            else:
                newlines.append(lines[i].rstrip('\n').strip().split(' > '))
            i += 1
        
        #append direction and destination for each location
        while j < len(locations_list):
            k = 0
            while k < len(newlines):
                if newlines[k][0] == locations_list[j].name:
                    if newlines[k][1].lower() == 'northwest':
                        locations_list[j].directions_list[0] = 'northwest'
                        locations_list[j].destinations_list[0] = newlines[k][2]
                    if newlines[k][1].lower() == 'north':
                        locations_list[j].directions_list[1] = 'north'
                        locations_list[j].destinations_list[1] = newlines[k][2]
                    if newlines[k][1].lower() == 'northeast':
                        locations_list[j].directions_list[2] = 'northeast'
                        locations_list[j].destinations_list[2] = newlines[k][2]
                    if newlines[k][1].lower() == 'east':
                        locations_list[j].directions_list[3] = 'east'
                        locations_list[j].destinations_list[3] = newlines[k][2]
                    if newlines[k][1].lower() == 'southeast':
                        locations_list[j].directions_list[4] = 'southeast'
                        locations_list[j].destinations_list[4] = newlines[k][2]
                    if newlines[k][1].lower() == 'south':
                        locations_list[j].directions_list[5] = 'south'
                        locations_list[j].destinations_list[5] = newlines[k][2]
                    if newlines[k][1].lower() == 'southwest':
                        locations_list[j].directions_list[6] = 'southwest'
                        locations_list[j].destinations_list[6] = newlines[k][2]
                    if newlines[k][1].lower() == 'west':
                        locations_list[j].directions_list[7] = 'west'
                        locations_list[j].destinations_list[7] = newlines[k][2]
                        
                    #make the destionation list cotains list of object
                    for i in range(len(locations_list)):
                        if locations_list[j].destinations_list[0] == locations_list[i].name:
                            locations_list[j].destinations_list[0] = locations_list[i]
                        if locations_list[j].destinations_list[1] == locations_list[i].name:
                            locations_list[j].destinations_list[1] = locations_list[i]
                        if locations_list[j].destinations_list[2] == locations_list[i].name:
                            locations_list[j].destinations_list[2] = locations_list[i]
                        if locations_list[j].destinations_list[3] == locations_list[i].name:
                            locations_list[j].destinations_list[3] = locations_list[i]
                        if locations_list[j].destinations_list[4] == locations_list[i].name:
                            locations_list[j].destinations_list[4] = locations_list[i]
                        if locations_list[j].destinations_list[5] == locations_list[i].name:
                            locations_list[j].destinations_list[5] = locations_list[i]
                        if locations_list[j].destinations_list[6] == locations_list[i].name:
                            locations_list[j].destinations_list[6] = locations_list[i]
                        if locations_list[j].destinations_list[7] == locations_list[i].name:
                            locations_list[j].destinations_list[7] = locations_list[i]
                k += 1
            j += 1
        return locations_list
        f.close()
        
    except FileNotFoundError:
        print('You have specified an invalid configuration file.')
        quit()

def draw_map(current_location, locations_list, items_list, exits_list):
    global destination
    line1 = list('           ')
    line2 = list('           ')
    line3 = list('    [x]    ')
    line4 = list('           ')
    line5 = list('           ')
    descriptions_list = []
    i = 0
    while i < len(current_location.directions_list):
        destination = current_location.destinations_list[i]
        if current_location.directions_list[i] == 'north':
            if len(destination.chasers_list) != 0:
                line1[4] = '['
                line1[5] = 'C'
                line1[6] = ']'
                line2[5] = '|'
            else:
                line1[4] = '['
                line1[6] = ']'
                line2[5] = '|'
        if current_location.directions_list[i] == 'northwest':
            if len(destination.chasers_list) != 0:
                line1[0] = '['
                line1[1] = 'C'
                line1[2] = ']'
                line2[3] = '\\'
            else:
                line1[0] = '['
                line1[2] = ']'
                line2[3] = '\\'
        if current_location.directions_list[i] == 'northeast':
            if len(destination.chasers_list) != 0:
                line1[8] = '['
                line1[9] = 'C'
                line1[10] = ']'
                line2[7] = '/'
            else:
                line1[8] = '['
                line1[10] = ']'
                line2[7] = '/'
        if current_location.directions_list[i] == 'west':
            if len(destination.chasers_list) != 0:
                line3[0] = '['
                line3[1] = 'C'
                line3[2] = ']'
                line3[3] = '-'
            else:
                line3[0] = '['
                line3[2] = ']'
                line3[3] = '-'
        if current_location.directions_list[i] == 'east':
            if len(destination.chasers_list) != 0:
                line3[8] = '['
                line3[9] = 'C'
                line3[10] = ']'
                line3[7] = '-'
            else:
                line3[8] = '['
                line3[10] = ']'
                line3[7] = '-'
        if current_location.directions_list[i] == 'southwest':
            if len(destination.chasers_list) != 0:
                line5[0] = '['
                line5[1] = 'C'
                line5[2] = ']'
                line4[3] = '/'
            else:
                line5[0] = '['
                line5[2] = ']'
                line4[3] = '/'
        if current_location.directions_list[i] == 'south':
            if len(destination.chasers_list) != 0:
                line5[4] = '['
                line5[5] = 'C'
                line5[6] = ']'
                line4[5] = '|'
            else:
                line5[4] = '['
                line5[6] = ']'
                line4[5] = '|'
        if current_location.directions_list[i] == 'southeast':
            if len(destination.chasers_list) != 0:
                line5[8] = '['
                line5[9] = 'C'
                line5[10] = ']'
                line4[7] = '\\'
            else:
                line5[8] = '['
                line5[10] = ']'
                line4[7] = '\\'
        i += 1
    print(''.join(line1).rstrip(' '))
    print(''.join(line2).rstrip(' '))
    print(''.join(line3).rstrip(' '))
    print(''.join(line4).rstrip(' '))
    print(''.join(line5).rstrip(' '))
    print(f'You are now at: {current_location.name}.')
    
    #items description
    if len(current_location.location_items_list) ==0 and len(current_location.chasers_list) == 0:
        print('There is nothing here.')
    else:
        for item in current_location.location_items_list:
            descriptions_list.append(item.full_desc)
        for chaser in current_location.chasers_list:
            descriptions_list.append(chaser.description)
        i = 0
        description = ""
        for i in range(len(descriptions_list)):
            if i == 0:
                description += descriptions_list[i]
            else:
                description += " " + descriptions_list[i]
        print(description)
        
    #flee reminder
    if current_location.has_exit == True:
        print('The path to freedom is clear. You can FLEE this place.')
        
def move(chaser,player,current_location,locations_list):
    catch_time = 0 #if catch time is 1, the chaser doesnot move
    #firstly catch goose by comparing terror_rating
    if chaser.location.name == current_location.name:
        print()
        print(f'{chaser.name} is trying to catch you!')
        catch_time = 1
        if chaser.terror_rating >= player.terror_rating:
            print('Oh no, you\'ve been caught!')
            print('========= GAME OVER =========')
            quit()
        elif player.terror_rating > chaser.terror_rating:
            if chaser.caught_times == 1:
                print('But your presence still terrifies them...')
                chaser.caught_times += 1
            elif chaser.caught_times == 2:
                print('Oh no, you\'ve been caught!')
                print('========= GAME OVER =========')
                quit()
    #sencondly move to the room where goose is (if the room is close to chaser)
    if current_location in chaser.location.destinations_list:
        for location in locations_list:
            if location.name == chaser.location.name:
                for chasers in location.chasers_list:
                    if chasers.name == chaser.name:
                        location.chasers_list.remove(chaser)
                        current_location.chasers_list.append(chaser)
        chaser.location = current_location
        print()
        print(f'{chaser.name} has arrived at {chaser.location.name}.')
    
    #thirdly take the item if there is, when chaser doesnot move to another room before change direction
    elif chaser.location.location_items_list:
        if catch_time == 0:
            for location in locations_list:
                if chaser.location.name == location.name:
                    chaser.take(location.location_items_list[0])
                    location.location_items_list.remove(location.location_items_list[0])
    
    #change the direction and move
    else:
        i = 0
        while i < 8:
            if chaser.direction.upper() == 'NORTHWEST':
                if chaser.location.destinations_list[0] == None:
                    chaser.direction = 'NORTH'
                else:
                    if catch_time == 0:
                        for location in locations_list:
                            if location.name == chaser.location.name:
                                location.chasers_list.remove(chaser)
                        chaser.location = chaser.location.destinations_list[0]
                        for location in locations_list:
                            if location.name == chaser.location.name:
                                location.chasers_list.append(chaser)
                    break
                    
                        
            elif chaser.direction.upper() == 'NORTH':
                if chaser.location.destinations_list[1] == None:
                    chaser.direction = 'NORTHEAST'
                else:
                    if catch_time == 0:
                        for location in locations_list:
                            if location.name == chaser.location.name:
                                location.chasers_list.remove(chaser)
                        chaser.location = chaser.location.destinations_list[1]
                        for location in locations_list:
                            if location.name == chaser.location.name:
                                location.chasers_list.append(chaser)
                    break

            elif chaser.direction.upper() == 'NORTHEAST':
                if chaser.location.destinations_list[2] == None:
                    chaser.direction = 'EAST'
                else:
                    if catch_time == 0:
                        for location in locations_list:
                            if location.name == chaser.location.name:
                                location.chasers_list.remove(chaser)
                        chaser.location = chaser.location.destinations_list[2]
                        for location in locations_list:
                            if location.name == chaser.location.name:
                                location.chasers_list.append(chaser)
                    break

            elif chaser.direction.upper() == 'EAST':
                if chaser.location.destinations_list[3] == None:
                    chaser.direction = 'SOUTHEAST'
                else:
                    if catch_time == 0:
                        for location in locations_list:
                            if location.name == chaser.location.name:
                                location.chasers_list.remove(chaser)
                        chaser.location = chaser.location.destinations_list[3]
                        for location in locations_list:
                            if location.name == chaser.location.name:
                                location.chasers_list.append(chaser)
                    break

            elif chaser.direction.upper() == 'SOUTHEAST':
                if chaser.location.destinations_list[4] == None:
                    chaser.direction = 'SOUTH'
                else:
                    if catch_time == 0:
                        for location in locations_list:
                            if location.name == chaser.location.name:
                                location.chasers_list.remove(chaser)
                        chaser.location = chaser.location.destinations_list[4]
                        for location in locations_list:
                            if location.name == chaser.location.name:
                                location.chasers_list.append(chaser)
                    break

            elif chaser.direction.upper() == 'SOUTH':
                if chaser.location.destinations_list[5] == None:
                    chaser.direction = 'SOUTHWEST'
                else:
                    if catch_time == 0:
                        for location in locations_list:
                            if location.name == chaser.location.name:
                                location.chasers_list.remove(chaser)
                        chaser.location = chaser.location.destinations_list[5]
                        for location in locations_list:
                            if location.name == chaser.location.name:
                                location.chasers_list.append(chaser)
                    break

            elif chaser.direction.upper() == 'SOUTHWEST':
                if chaser.location.destinations_list[6] == None:
                    chaser.direction = 'WEST'
                else:
                    if catch_time == 0:
                        for location in locations_list:
                            if location.name == chaser.location.name:
                                location.chasers_list.remove(chaser)
                        chaser.location = chaser.location.destinations_list[6]
                        for location in locations_list:
                            if location.name == chaser.location.name:
                                location.chasers_list.append(chaser)
                    break

            elif chaser.direction.upper() == 'WEST':
                if chaser.location.destinations_list[7] == None:
                    chaser.direction = 'NORTHWEST'
                else:
                    if catch_time == 0:
                        for location in locations_list:
                            if location.name == chaser.location.name:
                                location.chasers_list.remove(chaser)
                        chaser.location = chaser.location.destinations_list[7]
                        for location in locations_list:
                            if location.name == chaser.location.name:
                                location.chasers_list.append(chaser)
                    break
            i  += 1       
        
            
                
        
        
        



