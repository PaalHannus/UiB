
class SentimentAnalysis():
    '''A tool for sentiment analysis using the Naïve Bayes approach'''

    def __init__(self):
        self.isFit = False
        self.vocab = set()
        self.class_sentences = {}
        self.class_len = {}
        self.n_training_examples = 0

    def reset(self):
        self.isFit = False
        self.vocab = set()
        self.class_sentences = {}
        self.class_len = {}
        self.n_training_examples = 0

    def fit(self, data):
        '''
        Fit the data structure to the training data / training corpus. There is no need to define the sentiment classes
        as they are picked up by the data structure automatically. This means the SentimentAnalysis tool is more dynamic
        than requested in the assignment.

        Intuition: Gather all neccessary information in the training data to make predictions.

        Input: 
            - List of 2-tuples. In the first position a sentence, in the second position the sentiment/ground-truth.
        '''

        self.n_training_examples += len(data)
        for sentence, _class in data:

            sentences_in_class = self.class_sentences.get(_class, [])
            sentences_in_class.append(sentence)
            self.class_sentences[_class] = sentences_in_class

            total_words_in_class = self.class_len.get(_class, 0)
            self.class_len[_class] = total_words_in_class + \
                len(sentence.split())

            [self.vocab.add(word.lower()) for word in sentence.split()]
            self.isFit = True

    def predict(self, sentence, k=1):
        '''
        Predict the sentiment of an input sentence. Assures that the model has been trained before use.

        Intuition: 
            - Loop over all classes (To generate a prediction for each).
                - Gather some statistics about the class used for the calculation.
                - Loop over all words in the input sentence, and accumulate the multiplicative values.
                - Add result to output list

        Input:
            - String: Sentence we want to predict
            - (Optional) Int: representing k in addk smoothing. Default = 1

        Output:
            - A list of tuples: The first position refers to the class-label, the second position to the result of bayes.
        '''

        if not self.isFit:
            raise AssertionError(
                "ERROR: Tool must first be fit to training data")

        output = []
        for c in self.class_sentences.keys():
            naive_bayes_for_class = len(
                self.class_sentences[c]) / self.n_training_examples
            words_in_class = sum([len(s.split())
                                 for s in self.class_sentences[c]])

            for word in sentence.split():
                if word.lower() in self.vocab:
                    occurences = self._count_occurrences(word, c)
                    naive_bayes_for_class *= ((occurences + k) /
                                              (words_in_class + len(self.vocab)))
            output.append((c, naive_bayes_for_class))
        return output

    def _count_occurrences(self, word, word_class):
        ''' Helper function used to find how many occurences a word has in a given class'''
        counter = 0
        for sentence in self.class_sentences[word_class]:
            for w in sentence.split():
                if w.lower() == word.lower():
                    counter += 1
        return counter
