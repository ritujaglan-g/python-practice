subjects = ["Maths", "English", "Science", "Hindi", "Bio"]
marks = []
total = 0

for subject in subjects:
    submarks = int(input(f"{subject} ke marks daaliye: "))
    marks.append(submarks)

for mark in marks:
    total+=mark

print(total)




    


