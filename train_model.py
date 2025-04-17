# train_model.py

from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_digits
from sklearn.metrics import accuracy_score
import joblib

# Simulate training data using sklearn digits dataset (for demo purposes)
digits = load_digits()
X = digits.data
y = digits.target

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train an SVM classifier
model = SVC(kernel='rbf', probability=True)
model.fit(X_train, y_train)

# Accuracy check
preds = model.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, preds)}")

# Save the model
joblib.dump(model, "hindi_digit_model.pkl")
print("✅ Model saved as hindi_digit_model.pkl")
