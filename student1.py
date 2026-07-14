record = "101,Arun,Math:80|Physics:70|Chemistry:90"

parts = record.split(",")
print(parts)

student_id = parts[0]
student_name = parts[1]
subject_data = parts[2]

print("Student ID:", student_id)
print("Student Name:", student_name)
print("Subject Data:", subject_data)