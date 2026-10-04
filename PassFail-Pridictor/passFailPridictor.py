import pandas as pd
import xgboost as xgb

data = pd.DataFrame({
    "Name": ["Vansh Parmar", "Krish Robot", "Bhamshu", "Parshw Modh", "Ramlingan", "Frank"],
    "Total_Marks": [140, 95, 250, 275, 110, 190],
    "Attendance_Pct": [65, 45, 85, 90, 50, 75],
    "Result": [0, 0, 1, 1, 0, 1] # 1 = Pass, 0 = Fail
})

X_train = data[["Total_Marks", "Attendance_Pct"]]
y_train = data["Result"]

# We added min_child_weight=0 to force the model to learn from a tiny dataset
model = xgb.XGBClassifier(min_child_weight=0)
model.fit(X_train, y_train)

print("--- 1. Training Data Overview ---")
print(data.to_string(index=False))

print("\n--- 2. Model Feature Importance ---")
importance = model.feature_importances_
print(f"Total Marks Weight: {importance[0]*100:.2f}%")
print(f"Attendance Weight: {importance[1]*100:.2f}%")

print("\n--- 3. Batch Prediction Results ---")
new_students = pd.DataFrame({
    "Test_ID": ["New_Stu_01", "New_Stu_02"],
    "Total_Marks": [115, 210],
    "Attendance_Pct": [55, 82]
})

X_test = new_students[["Total_Marks", "Attendance_Pct"]]
predictions = model.predict(X_test)
probabilities = model.predict_proba(X_test)

for i in range(len(new_students)):
    status = "Pass" if predictions[i] == 1 else "Fail"
    prob = probabilities[i][predictions[i]] * 100
    marks = new_students['Total_Marks'].iloc[i]
    att = new_students['Attendance_Pct'].iloc[i]

    print(f"[{new_students['Test_ID'].iloc[i]}] Marks: {marks}, Attendance: {att}%")
    print(f" -> Predicted Status: {status} (Confidence: {prob:.1f}%)")