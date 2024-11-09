def tokenize(text):
    return [word.strip(" ,\n.);(!?)'").lower() for word in text.split()]

def count_lemmas(text, lemmas):
    words = tokenize(text)
    lemma_counts = {}

    for word in words:
        # If the word has a lemma, use it; otherwise, use the word itself
        lemma = lemmas.get(word, word)
        # Increment the count for the lemma
        lemma_counts[lemma] = lemma_counts.get(lemma, 0) + 1

    return lemma_counts

def count_category(lemma_counts, category):
    count = 0
    for lemma in category:
        # Add the count of the lemma if it exists in lemma_counts
        count += lemma_counts.get(lemma, 0)
    return count

def group_titles_by_genre(library):
    genre_groups = {}
    for title, genre in library.items():
        # Append the title to the list of the corresponding genre
        if genre not in genre_groups:
            genre_groups[genre] = []
        genre_groups[genre].append(title)
    return genre_groups

def unify(dict1, dict2):
    result = {}
    # Add entries from dict1
    for key, values in dict1.items():
        result[key] = sorted(set(values))
    # Add entries from dict2
    for key, values in dict2.items():
        if key in result:
            result[key] = sorted(set(result[key] + values))
        else:
            result[key] = sorted(set(values))
    return result

def melt(dict):
    result = []
    for key, values in dict.items():
        for value in values:
            result.append((key, value))
    return result

def n_intersection(sets):
    if not sets:
        # If the input list is empty, return an empty set
        return set()

    # Start with the first set as the base for intersection
    intersection_result = sets[0]

    # Iteratively intersect with each subsequent set
    for s in sets[1:]:
        intersection_result = intersection_result.intersection(s)

    return intersection_result

def sentiment_of_text(text, sentiment_of_word):
    words = tokenize(text)
    score = 0
    for word in words:
        # Add score if word is in sentiment_of_word, otherwise add 0
        score += sentiment_of_word.get(word, 0)
    return score
