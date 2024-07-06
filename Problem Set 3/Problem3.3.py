bpm = int(input("Please enter song's speed in BPM"))
result = f"A quater note delay in miliseconds for {bpm} BPM is {int((60 * 1000) / bpm)} ms."
print(result)
