import sensor, image, time

sensor.reset()
sensor.set_pixformat(sensor.GRAYSCALE)
sensor.set_framesize(sensor.QQVGA)
sensor.skip_frames(time=2000)

clock = time.clock()

while True:
    clock.tick()
    #img = sensor.snapshot()
    print(clock.fps())
