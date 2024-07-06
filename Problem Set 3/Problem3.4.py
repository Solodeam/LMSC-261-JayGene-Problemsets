duration = float(input("Please enter the song duration in minutes"))
if duration <= 2:
    print("Short song")
elif 2 < duration < 4:
    print("Medium song")
elif 4 <= duration:
    print("Long song")