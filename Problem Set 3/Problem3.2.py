midi = int(input("Please enter a MIDI number between 0 and 127"))
freq = 440 * (2 ** ((midi - 69) / 12))
print("The frequency of the MIDI note number ", midi, "is ", freq, "Hz.")