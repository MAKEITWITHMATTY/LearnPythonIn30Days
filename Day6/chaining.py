temp = 25
raining = False
is_warm = 0 < temp < 30
comfortable = is_warm and not raining
if comfortable:
    print("Go outside!")
