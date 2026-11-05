# Step 6: tell the next tool with an exit code
import sys


def check_hours(value):
    if value < 0:
        raise ValueError(f"{value} is a negative usage_hours; fix the source data")
    print(value, "is valid")


hours = -3  # change to 5, save and run again

try:
    check_hours(hours)
except ValueError as error:
    print(f"Stopped: {error}", file=sys.stderr)  # the error channel
    raise SystemExit(1)  # end with failure status 1

print("finished OK")  # reaching the end means exit code 0
