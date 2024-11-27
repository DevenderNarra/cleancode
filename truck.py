class Truck:
    def __init__(self, color, max_speed, acceleration, tyre_friction, max_cargo_weight):
            if max_speed <= 0:
                raise ValueError("Invalid value for max_speed")

            self.color = color
            self.max_speed = max_speed
            self.acceleration = acceleration
            self.tyre_friction = tyre_friction
            self.max_cargo_weight = max_cargo_weight

    def load(self,value):
            if value < 0:
                raise ValueError("Invalid value for max_cargo_weight")
            if value>=self.max_cargo_weight:
                return "Cannot load cargo more than max limit: 100"
            if value<100 and value>0:
                return "Cannot load cargo during motion"


    def unload(self,value):
            if value < 0:
                raise ValueError("Invalid value for max_cargo_weight")
            if value>=self.max_cargo_weight:
                return "Cannot load cargo more than max limit: 100"
            if value<100 and value>0:
                return "Cannot load cargo during motion"

    def sound_horn(self):
            return "Honk Honk"
