class Decor:
    def __init__(self, condition = 0, category = "Decor"):
        self.condition = condition
        self.category = category
        

    def __str__(self):
        return "Something to decorate your space."  

    def condition_description(self):
        return str(self.condition) 