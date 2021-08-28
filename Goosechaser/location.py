class Location:
    def __init__(self, name):
        self.name = name
        self.location_items_list = []
        #The order is           NW0  N1   NE2  E3   SE4  S5   SW6  W7
        self.directions_list = [None,None,None,None,None,None,None,None]
        self.destinations_list = [None,None,None,None,None,None,None,None]
        self.chasers_list = []
        self.has_exit = False
        
    def add_item(self, item):
        self.location_items_list.append(item)

    def remove_item(self, item):
        self.location_items_list.remove(item)
