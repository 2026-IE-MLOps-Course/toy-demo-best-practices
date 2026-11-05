# Step 5: catch only the errors you expect

try:
    rate = 10 / 0  # a bug, not bad data
except ValueError as error:
    print("Stopped:", error)  # not used: this is not a ValueError
