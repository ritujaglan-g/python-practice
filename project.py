# Student names
students = [
    {"name": "ty", "stream": "arts"},
    {"name": "ry", "stream": "medical"},
    {"name": "py", "stream": "non-medical"},
    {"name": "wy", "stream": "non-medical"},
    {"name": "again", "stream": "medical"}
]

# Print student details
for student in students:
    print(f"Name: {student['name']}, Stream: {student['stream']}")
