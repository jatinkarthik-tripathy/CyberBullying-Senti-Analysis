import matplotlib.pyplot as plt
import csv
from sklearn.metrics import accuracy_score, confusion_matrix, f1_score, precision_score, recall_score, roc_curve, auc

test_results = []
with open('outputs/submit_results.tsv') as file:
    rd = csv.reader(file, delimiter="\t")
    next(rd, None)
    for row in rd:
        data = [i for i in row]
        test_results.append(int(data[1]))

actual = []
with open('data/CoLA/test_labels.tsv') as file:
    rd = csv.reader(file, delimiter="\t")
    next(rd, None)
    for row in rd:
        data = [i for i in row]
        actual.append(int(data[1]))

print(f'accuracy score: {accuracy_score(actual, test_results)}\n')
print(f'confusion matrix:\n{confusion_matrix(actual, test_results)}\n')
print(f'precision score: {precision_score(actual, test_results, average="weighted")}\n')
print(f'recall score: {recall_score(actual, test_results, average="weighted")}\n')
print(f'f1 score: {f1_score(actual, test_results, average="weighted")}\n')
fpr, tpr, threshold = roc_curve(actual, test_results)
roc_auc = auc(fpr, tpr)
plt.title('Receiver Operating Characteristic')
plt.plot(fpr, tpr, 'b', label='AUC = %0.2f' % roc_auc)
plt.legend(loc='lower right')
plt.plot([0, 1], [0, 1], 'r--')
plt.xlim([0, 1])
plt.ylim([0, 1])
plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')
plt.show()
