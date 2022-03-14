import tasker


class Main:
    def __init__(self, path):
        with open(path) as f:
            self.text = f.read()
        self.text_reader = tasker.Tasker(self.text)

    def begin(self):
        try:
            k, n = map(
                int,
                input(
                    "k and n: "
                ).split()
            )
        except TypeError:
            k, n = 10, 4

        print("\tYour text:\n", self.text, "\n")

        self.text_reader.get_occurrences_of_words(k)
        print("\n\tAverage count of words in sentences: ",
              self.text_reader.get_average_count_of_words())
        print("\tMedian count of words in sentences: ",
              self.text_reader.get_median_count_of_words(), "\n")
        self.text_reader.get_ngrams(k, n)
