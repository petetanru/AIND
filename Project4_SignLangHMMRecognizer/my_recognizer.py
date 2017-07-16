import warnings
from asl_data import SinglesData


def recognize(models: dict, test_set: SinglesData):
    """ Recognize test word sequences from word models set

   :param models: dict of trained models
       {'SOMEWORD': GaussianHMM model object, 'SOMEOTHERWORD': GaussianHMM model object, ...}
   :param test_set: SinglesData object
   :return: (list, list)  as probabilities, guesses
       both lists are ordered by the test set word_id
       probabilities is a list of dictionaries where each key a word and value is Log Liklihood
           [{SOMEWORD': LogLvalue, 'SOMEOTHERWORD' LogLvalue, ... },
            {SOMEWORD': LogLvalue, 'SOMEOTHERWORD' LogLvalue, ... },
            ]
       guesses is a list of the best guess words ordered by the test set word_id
           ['WORDGUESS0', 'WORDGUESS1', 'WORDGUESS2',...]
   """
    warnings.filterwarnings("ignore", category=DeprecationWarning)
    probabilities = []
    guesses = []
    # TODO implement the recognizer
    # return probabilities, guesses
    # raise NotImplementedError

    all_seq = test_set.get_all_sequences()
    all_Xlength = test_set.get_all_Xlengths()


    for seq in all_seq:
        X, length = all_Xlength[seq]
        prob = {}

        for word_model, model in models.items():
            try:
                score = model.score(X, length)
                prob[word_model] = score
            except:
                score = -float("inf")
                prob[word_model] = score

        v = list(prob.values())
        k = list(prob.keys())

        guesses.append( k[v.index(max(v))] )
        probabilities.append(prob)

    return probabilities, guesses


