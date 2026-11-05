# Step 6: tell the next tool with an exit code
import sys  # new

hours = -3.0  # try 8.0 to see exit code 0
threshold = 10.0

try:
    if hours < 0:
        raise ValueError(f"{hours} is a negative usage; fix the source data")
    if hours < threshold:
        print(hours, "h -> churn")
    else:
        print(hours, "h -> stay")
except ValueError as error:
    print("Stopped:", error, file=sys.stderr)  # new: the error channel
    raise SystemExit(1)  # new: end with failure status 1
