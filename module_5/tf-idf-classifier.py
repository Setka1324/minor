from pathlib import Path
import matplotlib.pyplot as plt

def tokenize_text(text):
    """
    Returns a list of words from string text.
    """
    words = []
    for word in text.split():
        clean = word.lower().strip(' ,;.:\'"[]()-_?!')
        if clean.isalpha():
            words.append(clean)
    return words

def get_text_file_names(path, extension='txt'):
    """
    Get all paths of files with given (.txt) extension.
    """
    return list(Path(path).glob(f'*.{extension}'))

def is_written_by_shakespeare(file_name):
    """
    Checks for a given filename if it contains the text "shakespeare"
    """
    by_shakespeare = file_name.name.split('.')[0] == "shakespeare"
    return by_shakespeare

def calculate_accuracy(actual, predicted):
    """
    Calculates the accuracy by comparing actual and predicted authorship lists.
    """
    correct_predictions = sum(1 for a, p in zip(actual, predicted) if a == p)
    return correct_predictions / len(actual)

def load_shakespeare_tf_idf_scores(filename='shakespeare-tf-idf.csv'):
    """
    Loads Shakespeare's TF-IDF scores from a CSV file and returns them as a dictionary.
    """
    tf_idf_scores = {}
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            word, score = line.strip().split(',')
            tf_idf_scores[word] = float(score)
    return tf_idf_scores

def calculate_shakespeare_score(text, shakespeare_scored_words):
    """
    Calculates the Shakespeare score for a given text. This score is the average of the TF-IDF
    scores of the words in the text. Words not in the dictionary have a score of 0.
    """
    words = tokenize_text(text)
    total_score = 0
    word_count = 0

    for word in words:

        # Default to 0 if word not found
        score = shakespeare_scored_words.get(word, 0)
        total_score += score
        word_count += 1

    # Average score, avoid division by zero
    if word_count == 0:
        return 0
    return total_score / word_count

def predict_authorship(file_paths, shakespeare_scores, threshold):
    """
    Predicts authorship for each text fragment based on its Shakespeare score and the given threshold.
    """
    predictions = []
    for file_path in file_paths:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
            score = calculate_shakespeare_score(text, shakespeare_scores)

            # Predict True if score >= threshold
            predictions.append(score >= threshold)

    return predictions

if __name__ == "__main__":
    # Load Shakespeare TF-IDF scores
    shakespeare_scores = load_shakespeare_tf_idf_scores('shakespeare-tf-idf.csv')

    # Get all text files from the 'test-set' folder
    file_paths = get_text_file_names('test-set')

    # Determine the actual authorship for all files
    actual_authorship = [is_written_by_shakespeare(file) for file in file_paths]

    # Experiment with different thresholds between 0 and 0.01 in 40 steps
    thresholds = [i * 0.01 / 40 for i in range(41)]
    accuracies = []

    # Loop through each threshold and calculate accuracy
    for threshold in thresholds:
        predictions = predict_authorship(file_paths, shakespeare_scores, threshold)
        accuracy = calculate_accuracy(actual_authorship, predictions)
        accuracies.append(accuracy)

    # Plot the results
    plt.plot(thresholds, accuracies, 'o-')
    plt.xlabel("Score Threshold")
    plt.ylabel("Accuracy")
    plt.title("Classifier Performance (TF-IDF)")
    plt.grid(True)
    plt.savefig("tf-idf-classifier.png")
    plt.show()
