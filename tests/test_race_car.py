def test_apply_brakes(racecar):
    racecar.start()
    racecar.apply_breaks()
    assert racecar.nitro == 10

def test_racecar_engine_start(racecar):
    racecar.start()
    assert racecar.is_engine_started==True

def test_racecar_accelerate(racecar):
    act=racecar.accelerate()
    assert "Start the engine to accelerate" == act

def test_get_racecar_current_speed(racecar):
    racecar.start()
    act=racecar.get_current_speed()
    assert racecar.current_speed == act

def test_sound_horn(racecar):
    act=racecar.sound_horn()
    assert "Peep Peep\nBeep Beep"==act

def test_racecar_stop_engine(racecar):
    racecar.stop_engine()
    assert racecar.is_engine_started==False


