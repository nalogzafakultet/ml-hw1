import csv

def load_dataset(path_to_file):
    X, y = [], []
    with open(path_to_file, 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        next(reader, None) # Skip header
        for row in reader:
            y.append(int(row[1]))
            X.append(row[2])
    return X, y
