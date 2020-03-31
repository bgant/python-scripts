# Source: https://learn.sparkfun.com/tutorials/python-programming-tutorial-getting-started-with-the-raspberry-pi/experiment-2-play-sounds
# Source: https://www.pygame.org/docs/ref/mixer.html

from pygame import mixer

mixer.init()

sound = mixer.Sound('applause-1.wav')

sound.play()

# mixer.get_busy()  <-- 1 still playing / 0 finished playing
