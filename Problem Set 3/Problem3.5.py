sec = int(input("Please enter song's duratoin in seconds"))
bps = float(int(input("Please enter song's speed in BPM")) / 60)
beats = 0
current_sec = 1

while current_sec <= sec:
    beats = bps * current_sec
    print("At second ", current_sec, ", total beats: ", round(beats, 2))
    current_sec += 1