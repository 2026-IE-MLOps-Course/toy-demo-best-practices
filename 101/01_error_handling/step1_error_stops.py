# Step 1: an error stops the program

hours = [2.5, 15.0, 8.0]
print("average hours:", sum(hours) / len(hours))

print("before")
number = int("ten")  # Python cannot turn the text "ten" into a number
print("after")  # never runs