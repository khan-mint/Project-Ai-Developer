import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

# 1. LOAD IRIS DATASET - Comes built-in with sklearn
iris = load_iris()
X = iris.data # features: sepal length, sepal width, petal length, petal width
y = iris.target # target: 0=Setosa, 1=Versicolor, 2=Virginica

print("Feature names:", iris.feature_names)
print("Target names:", iris.target_names)

# 2. SPLIT DATA: 80% Train, 20% Test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. CREATE AND TRAIN CLASSIFIER
# LogisticRegression is the simplest classifier
model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

# 4. MAKE PREDICTIONS
y_pred = model.predict(X_test)

# 5. CHECK ACCURACY
acc = accuracy_score(y_test, y_pred)
print("\n" + "="*40)
print(f"Model Accuracy: {acc*100:.2f}%")
print("="*40)

print("\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=iris.target_names))

# 6. CONFUSION MATRIX PLOT
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(6,4))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
            xticklabels=iris.target_names,
            yticklabels=iris.target_names)
plt.title('Confusion Matrix')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.savefig('iris_confusion_matrix.png')
plt.show()

# 7. TEST WITH 1 NEW FLOWER
new_flower = [[5.1, 3.5, 1.4, 0.2]] # sepal_len, sepal_wid, petal_len, petal_wid
prediction = model.predict(new_flower)
predicted_flower = iris.target_names[prediction][0]
print(f"\nPredicted Flower Type: {predicted_flower}")