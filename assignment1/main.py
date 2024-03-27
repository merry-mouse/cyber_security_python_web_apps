import re

total_errors = 0
with open("example.log", "r") as file:
    for line in file:
        error = re.findall(r"ERROR", line)
        if error:
            total_errors += 1

print(f"There are {total_errors} errors found in the log file.")
