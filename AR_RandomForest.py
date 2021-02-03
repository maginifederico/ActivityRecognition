import pandas as pd
from sklearn import metrics
from sklearn.ensemble import RandomForestClassifier

# load of data
features = pd.read_csv(r'UCI HAR Dataset\features.txt', sep='\n', names=["features"])
activity_labels = pd.read_csv(r'UCI HAR Dataset\activity_labels.txt', sep='\n', names=["activity_labels"])

X_test = pd.read_csv(r'UCI HAR Dataset\test\X_test.txt', sep='\s+', names=[i for i in range(561)])
X_train = pd.read_csv(r'UCI HAR Dataset\train\X_train.txt', sep='\s+', names=[i for i in range(561)])

y_test = pd.read_csv(r'UCI HAR Dataset\test\y_test.txt', names=["targets_test"])
y_train = pd.read_csv(r'UCI HAR Dataset\train\y_train.txt', names=["targets_train"])

# print of data
print("\nX_test:\n", X_test)
print("\nX_train:\n", X_train)
print("\ny_test:\n", y_test)
print("\ny_train:\n", y_train)
print("\nfeatures:\n", features)
print("\nactivity_labels:\n", activity_labels)


# function which create confusion matrix and classification report
def report(target, pred, target_names):
    cm = metrics.confusion_matrix(target, pred)
    print('\nContingency matrix:')
    print(cm)
    print('\nClassification report:')
    print(metrics.classification_report(target, pred, target_names=target_names))


# classifier definition and learning
classifier = RandomForestClassifier()
classifier.fit(X_train, y_train.values.ravel())
y_pred = classifier.predict(X_test)

report(y_test, y_pred, activity_labels)
