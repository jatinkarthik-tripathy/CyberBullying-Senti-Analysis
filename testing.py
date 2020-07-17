import csv

test_results = []
with open('outputs/submit_results.tsv') as file:
    rd = csv.reader(file, delimiter="\t")
    for row in rd:
      data = [i for i in row]
      test_results.append(data[1])

actual = []
with open('data/CoLA/test_labels.tsv') as file:
    rd = csv.reader(file, delimiter="\t")
    for row in rd:
      data = [i for i in row]
      actual.append(data[1])

print(sum([1 for i, j in zip(test_results, actual) if i == j])/len(actual))
