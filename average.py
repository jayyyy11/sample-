# List of student grades
grades = [85, 90, 78, 92, 88, 76, 95]

# Calculate the average grade
average_grade = sum(grades) / len(grades)

# Create a string with the result
result = f"The average grade of the students is: {average_grade:.2f}"

# Write the result to a text file
with open("average_grade.txt", "w") as file:
    file.write(result)

print("The average grade has been written to 'average_grade.txt'.")
