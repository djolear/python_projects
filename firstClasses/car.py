class Car(object):
    condition = 'New'
    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color

    def drive(self):
        self.condition = 'Used'