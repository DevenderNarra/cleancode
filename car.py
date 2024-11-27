class Car:
    def __init__(self,color,max_speed,acceleration,tyre_friction):
        if max_speed <= 0:
            raise ValueError("Invalid value for max_speed")

        self.color = color
        self.max_speed = max_speed
        self.acceleration = acceleration
        self.tyre_friction = tyre_friction
        self.is_engine_started = False
        self.current_speed=0
    def get_current_speed(self):
        return self.current_speed


    def start_engine(self):
        self.is_engine_started = True

    def accelerate(self):
        if self.is_engine_started:
            self.current_speed += self.acceleration
        else:
            print("Start the engine to accelerate")

    def apply_brakes(self):
        self.current_speed -= self.tyre_friction

    def sound_horn(self):
        return "Beep Beep"

    def stop_engine(self):
        self.is_engine_started = False

    def __str__(self):
        return self.color

