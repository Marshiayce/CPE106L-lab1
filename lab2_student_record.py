student = {
    "id" : "2025-001",
    "name" : "Juan Dela Cruz",
    "grades" : [80,90,85]
}

average = sum(student["grades"])/len(student["grades"])
print("Average:", average)

student["grades"].extend([73,78,96])

average = sum(student["grades"])/len(student["grades"])
print("New Average:", average)