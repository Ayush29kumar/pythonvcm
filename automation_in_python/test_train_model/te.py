import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
data = pd.read_csv('a.csv')
X = data['sentence']
y = data['catagory']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
vectorizer = TfidfVectorizer()
X_train_features = vectorizer.fit_transform(X_train)
X_test_features = vectorizer.transform(X_test)
model = LogisticRegression()
model.fit(X_train_features, y_train)
y_pred = model.predict(X_test_features)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
while True :
    user_input = input("Enter a command: ")
    user_input = user_input.lower()
    user_input_features = vectorizer.transform([user_input])
    prediction = model.predict(user_input_features)
    class_labels = {'command sentence': 'Command Sentence', 'normal sentence': 'Normal Sentence'}


    if class_labels[prediction[0]] == 'Command Sentence':
        print("command sentence")
    elif class_labels[prediction[0]] == 'Normal Sentence':
        print("normal sentence")
    else:
        print("------------")



