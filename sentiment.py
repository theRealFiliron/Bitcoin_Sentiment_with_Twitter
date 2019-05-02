import sklearn
from sklearn.feature_extraction.text import CountVectorizer

# example

count = 0

data = []
data_labels = []
with open("pos.txt") as f:
    for i in f:
       if count < 50000:
           data.append(i) 
           data_labels.append('pos')
           count += 1

count = 0
with open("neg.txt") as f:
    for i in f: 
       if count < 50000:
          data.append(i)
          data_labels.append('neg')
          count += 1

# features

vectorizer = CountVectorizer(
    analyzer = 'word',
    lowercase = False,
)
features = vectorizer.fit_transform(
    data
)
features_nd = features.toarray()

# scikit-learn, train/test

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test  = train_test_split(
        features_nd, 
        data_labels,
        train_size=0.80, 
        random_state=1234)

# logistic regression

from sklearn.linear_model import LogisticRegression

log_model = LogisticRegression()

# fit

log_model = log_model.fit(X=X_train, y=y_train)

# results

y_pred = log_model.predict_proba(X_test)

neg_count = 0
pos_count = 0

for sent in y_pred:
    if sent == 'pos':
        pos_count += 1
    else:
        neg_count += 1
