import joblib
from sklearn import svm
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split

# Dummy training with sklearn digits (replace with Hindi digits)
data = load_digits()
X, y = data.data, data.target

model = svm.SVC()
model.fit(X, y)

joblib.dump(model, "hindi_digit_model.pkl")
print("Model saved as hindi_digit_model.pkl")
