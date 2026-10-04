import pandas as pd
import json
import re

# Read the JavaScript file
with open("/content/student_data.js", "r") as file:
    content = file.read()

# Extract the student array from the JavaScript file
data = re.search(r'\[(.*?)\]', content, re.DOTALL).group(0)

# Convert JavaScript object keys to JSON format
data = re.sub(r'(\w+):', r'"\1":', data)

# Convert JavaScript data into Python data
students = json.loads(data)

# Convert scraped student information into DataFrame
student_df = pd.DataFrame(students)

print("Student information scraped from JavaScript file:")
display(student_df)

# Existing student marks DataFrame
marks_df = pd.DataFrame({
    "Roll_No": [101, 102, 103, 104, 105],
    "Python": [85, 78, 65, 92, 74],
    "DBMS": [80, 75, 70, 88, 72],
    "Maths": [76, 82, 68, 90, 70]
})

print("\nStudent Marks:")
display(marks_df)

# Merge student information with marks
merged_df = pd.merge(student_df, marks_df, on="Roll_No")

print("\nMerged Student Data:")
display(merged_df)