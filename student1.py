record = "102,Meera,Math:45|Physics:55|Chemistry:60"
parts = record.split(",")

student_id = parts[0]
student_name = parts[1]
subjects_data = parts[2]

print("ID:", student_id)
print("Name:", student_name)
print("Subjects:", subjects_data)