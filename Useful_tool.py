import random

feet_in_mile = 5000
meters_in_KM = 1000
beatles = ["santhosh","ramesh","suresh"]

def get_file_ext(filename):
    return filename[filename.index(".")+1:]

def roll_dice(num):
    return random.randint(1,num)
