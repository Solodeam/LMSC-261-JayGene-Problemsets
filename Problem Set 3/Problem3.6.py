for beat in range(1, 16):
    if beat % 4 == 1:
        print("B", end="\t")
    elif beat % 4 == 3:
        print("K", end="\t")
    elif beat % 4 == 2:
        print("t", end="\t")
    else:
        print("t", end="\t")