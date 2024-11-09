"""
unique-words-classifier.py: The program takes an arbitrary file from the folder
`test-set` and predicts whether it is written by Shakespeare.

Author: ...
"""

from pathlib import Path
import matplotlib.pyplot as plt


SHAKESPEARE_WORDS_FILE = "shakespeare-words.txt"
TEST_SET_PATH = Path("test-set")

def main():
    # Get shakespeare words
    shakespeare_words = load_shakespeare_words(SHAKESPEARE_WORDS_FILE)

    # Get an arbitrary file from the dataset
    text_file_name = get_text_file_names(TEST_SET_PATH)[300]

    # Check if the file was written by shakespeare
    is_shakespeare = is_written_by_shakespeare(text_file_name)

    if is_shakespeare:
        print(f"The text {text_file_name} is written by Shakespeare")
    else:
        print(f"The text {text_file_name} is not written by Shakespeare")

    # Predict step 1, get scores
    with open(text_file_name, 'r', encoding='UTF-8') as file:
        score = calculate_shakespeare_score(file.read(), shakespeare_words)

    # Predict step 2, try multiple thresholds
    thresholds = [t/20 for t in list(range(0, 4))]
    for threshold in thresholds:
        if score >= threshold:
            print(f"With a threshold of {threshold} we predict that Shakespeare is the author.")
        else:
            print(f"With a threshold of {threshold} we predict that Shakespeare is not the author.")


def load_shakespeare_words(filename):
    """
    Load the file containing words typicaly for Shakespearean language. Assumes
    that the input file does not contain any duplicate words.
    """
    words = []
    with open(filename, 'r', encoding='UTF-8') as file:
        for line in file:
            words.append(line.rstrip('\n'))
    return words

def get_text_file_names(path, extension='txt'):
    """
    Get all paths of files with given (.txt) extension.
    """
    return list(Path(path).glob(f'*.{extension}'))


# Change this function in favor of efficiency.
# With N being the length of shakespeare_words:
# Complexity before changes: O(N^2)
# Complexity after changes: O(N)
def calculate_shakespeare_score(text, shakespeare_words):
    """
    Compute the score of a text fragment by checking the relative overlap of
    words in the text with the shakespeare word list.
    """
    word_list = tokenize_text(text)

    # All unique words in the text
    unique_words = set(word_list)

    # Words in both text and Shakespeare's set
    shakespeare_words_in_text = unique_words.intersection(shakespeare_words)

    shakespeare_score = len(shakespeare_words_in_text)/len(unique_words)
    return shakespeare_score

def is_written_by_shakespeare(file_name):
    """
    Checks for a given filename if it contains the text "shakespeare"
    """
    by_shakespeare = file_name.name.split('.')[0] == "shakespeare"
    return by_shakespeare

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

def calculate_accuracy(actual, predicted):
    """
    Calculates the accuracy by comparing actual and predicted authorship lists.
    """
    correct_predictions = sum(1 for a, p in zip(actual, predicted) if a == p)
    return correct_predictions / len(actual)

#if __name__ == "__main__":
    #main()


file_paths = get_text_file_names('test-set')
actual_authorship = [is_written_by_shakespeare(file) for file in file_paths]
shakespeare_words = load_shakespeare_words("shakespeare-words.txt")

thresholds = [i * 0.1 / 40 for i in range(41)]
accuracies = []

for threshold in thresholds:
    predictions = predict_authorship(file_paths, shakespeare_words, threshold)
    accuracy = calculate_accuracy(actual_authorship, predictions)
    accuracies.append(accuracy)

# Plot the results
plt.plot(thresholds, accuracies, 'o-')
plt.xlabel("Score Threshold")
plt.ylabel("Accuracy")
plt.title("Classifier Performance")
plt.grid(True)
plt.show()

#import timeit

#time = timeit.timeit(
#    "calculate_shakespeare_score(text, shakespeare_words)",
#    setup="""from __main__ import load_shakespeare_words, calculate_shakespeare_score
#shakespeare_words = load_shakespeare_words('shakespeare-words.txt')
#with open('./test-set/shakespeare.0350.txt', 'r', encoding='UTF-8') as file:
#    text = file.read()
#""",
#    number=1000
#)

#print(f"Time taken: {time} seconds")
