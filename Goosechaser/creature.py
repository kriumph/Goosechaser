class Creature:
    def __init__(self, name, description, terror_rating, location, direction):
        self.creature_items_list = []
        self.name = name
        self.description = description
        self.terror_rating = int(terror_rating)
        self.location = location
        self.direction = direction
        self.caught_times = 1
        
    def take(self, item):
        self.terror_rating += item.terror_rating
        self.creature_items_list.append(item)
        
    def drop(self, item):
        self.terror_rating -= item.terror_rating
        self.creature_items_list.remove(item)

    def get_terror_rating(self):
        return self.terror_rating


