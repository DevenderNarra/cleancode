import math

class RaceCar:
    def __init__(self,color,max_speed,acceleration,tyre_friction):
        if max_speed <= 0:
            raise ValueError("Invalid value for max_speed")

        self.color = color
        self.max_speed = max_speed
        self.acceleration = acceleration
        self.tyre_friction = tyre_friction
        self.nitro = 0
        self.is_engine_started=False
        self.current_speed=0

    def get_current_speed(self):
        return self.current_speed

    def start(self):
        self.is_engine_started=True

    def apply_breaks(self):
        if self.current_speed >= self.current_speed//2:
             self.nitro=10
        self.current_speed -= self.tyre_friction

    def accelerate(self):
        if self.is_engine_started:
            self.current_speed += self.acceleration
        if self.nitro >= 10:
            # Use nitro
            extra_speed = math.ceil(0.3 * self.acceleration)
            self.current_speed += extra_speed
            self.nitro -= 10
        else:
            return "Start the engine to accelerate"

    def sound_horn(self):
        return "Peep Peep\nBeep Beep"