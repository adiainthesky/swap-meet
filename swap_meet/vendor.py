class Vendor:
    def __init__(self, inventory = None):
        #  if self.inventory == None:
        #     self.inventory = []
        # else:
        #     self.inventory = inventory
        
        self.inventory = inventory
        if self.inventory is None:
            self.inventory = []
    
    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item not in self.inventory:
            return False
        self.inventory.remove(item)
        return item
