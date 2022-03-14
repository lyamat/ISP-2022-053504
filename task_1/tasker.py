import re


class Tasker:

    def get_words(self, sentence):
        return re.split(r"\s[-]\s|[\,,:,;]\s|\s", sentence)

    def __init__(self, text: str):
        self.text = text
        self.sentences = re.split(r"[.!?]\s", text)
        self.words = []
        for sentence in self.sentences:
            self.words += list(
                map(lambda x: x.lower(),
                    self.get_words(sentence)
                    )
            )

    def get_ngrams(self, k=10, n=4):
        ngrams = {}

        for word in self.words:
            start = 0
            end = n
            len_word = len(word)
            for i in range(0, len_word):
                if end <= len_word:
                    if ngrams.get(word[start:end]):
                        ngrams[word[start:end]] = ngrams.get(
                            word[start:end]) + 1
                    else:
                        ngrams[word[start:end]] = 1
                    start += 1
                    end += 1
                else:
                    break
        ngrams = sorted(ngrams.items(), key=lambda x: x[1], reverse=True)

        for i in range(0, k):
            print("\"%s\" in a quantity of %s" % (ngrams[i][0], ngrams[i][1]))

    def get_occurrences_of_words(self, k=5):
        d = dict()
        for word in self.words:
            if word in d:
                d[word] = d[word] + 1
            else:
                d[word] = 1
        print(d)

    def get_average_count_of_words(self):
        return len(self.words) / len(self.sentences)

    def get_median_count_of_words(self):
        word_counts = []
        for sentence in self.sentences:
            word_counts.append(len(self.get_words(sentence)))
        word_counts.sort()
        length = len(word_counts)

        if length % 2:
            return word_counts[length // 2]
        else:
            return (word_counts[length / 2 - 1] - word_counts[length / 2]) / 2
