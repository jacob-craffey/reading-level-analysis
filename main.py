def syllable_count(word):
    word = word.lower()
    count = 0
    vowels = "aeiouy"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("e") or word.endswith("ed"):
        count -= 1
    if count == 0:
        count += 1
    print(str(word) + ": " + str(count))
    return count


def get_school_level(read_level):
    if read_level > 100:
        return "Below 5th grade"
    if read_level <= 100.00 and read_level >= 90.00:
        return "5th grade"
    elif read_level <= 90.0 and read_level >= 80.0:
        return "6th grade"
    elif read_level <= 80.0 and read_level >= 70.0:
        return "7th grade"
    elif read_level <= 70.0 and read_level >= 60.0:
        return "8th & 9th grade"
    elif read_level <= 60.0 and read_level >= 50.0:
        return "10th to 12th grade"
    elif read_level <= 50.0 and read_level >= 30.0:
        return "College"
    elif read_level <= 30.0 and read_level >= 0:
        return "College graduate"
    else:
        return "error"


def load_synonyms():
    global  synonyms
    with open("Synonyms.txt", "r") as s_file:
        synonyms = [line.split() for line in s_file]


def make_word_better(word):
    for pairs in synonyms:
        if pairs[0] == word:
            print("Changing " + pairs[0] + " to " + pairs[1])
            return pairs[1]
    return word


def make_word_worse(word):
    for pairs in synonyms:
        if pairs[1] == word:
            print("Changing " + pairs[1] + " to " + pairs[0])
            return pairs[0]
    return word


def main():
    total_words = 0
    total_sentences = 0
    total_syllables = 0

    load_synonyms()

    # Read the text file one line at a time
    fname = input("Enter a text file: ")
    with open(fname, 'r') as f:
        for line in f:
            words = line.split()
            # Counts the amount of periods in each line
            for word in words:
                #word = make_word_better(word)
                word = make_word_worse(word)
                total_syllables += syllable_count(word)
                if "." in word or '?' in word or ';' in word or '!' in word:
                    # print word
                    total_sentences += 1

            # Counts each word on the current line
            total_words += len(words)

    print("\nSentences: ", total_sentences)
    print("Words:     ", total_words)
    print("Syllables: ", total_syllables)

    read_level = 206.835 - 1.015 * (total_words / total_sentences) - (84.6 * (total_syllables / total_words))
    grade = get_school_level(read_level)
    print(grade + " " + str(read_level))
    return


if __name__ == '__main__':
    main()
