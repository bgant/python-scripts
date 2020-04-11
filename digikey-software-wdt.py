# Source: https://www.digikey.com/en/articles/a-designers-guide-to-watchdog-timers
# 
# From the article: "never put a WDT tickle in an interrupt service routine"
#

from machine import reset

main():
    # Check CPU and Memory Round 1
    state = 0x5555
    wdt_a()

    #<code to run>
    #
    #
    #

    # Check CPU and Memory Round 2
    state += 0x2222
    wdt_b()


wdt_a():
    if state != 0x5555:
        reset()
    state += 0x1111


wdt_b():
    if state != 0x8888:
        reset()
    #<reset watchdog timer>
    state = 0

