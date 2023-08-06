import logging
import inspect
import sys

import nltk
from nltk.tokenize import word_tokenize
from nltk import sent_tokenize
from nltk.tag import pos_tag


def logger(func):
    def wrap(*args, **kwargs):
        logging.info("%s - line no: %d with args: %s, kwargs: %s" % (
            func.__name__,
            inspect.getframeinfo(inspect.currentframe().f_back).lineno,
            args,
            kwargs
        ))
        # Log the function name and arguments

        # Call the original function
        result = func(*args, **kwargs)

        # Log the return value
        logging.info("%s returned: %s" % (func.__name__, result))

        # Return the result
        return result

    return wrap


@logger
def download_nltk_packages():
    # Download the required NLTK data (if not already downloaded)
    nltk.download('punkt')
    nltk.download('averaged_perceptron_tagger')


@logger
def check_if_nltk_packages_are_installed():
    try:
        nltk.data.find('tokenizers/punkt')
    except LookupError:
        print("the nltk packges were not found.")
        print("starting installation")
        download_nltk_packages()
        print("Installation has finished.\nAnyway, you need to rerun the script,\nto be able to access the packages.")
        sys.exit()
    return True


@logger
def find_verbs(sentence):
    # Tokenize the sentence into words
    words = word_tokenize(sentence)

    # Perform POS tagging to get the POS tags for each word
    tagged_words = pos_tag(words)

    # Filter words with POS tags that correspond to verbs
    return [word for word, tag in tagged_words if tag.startswith('VB')]


def topic_tokenization():

    text = '''Louis XVI (born 1754 A.D.) also encouraged major voyages of exploration. 
    In 1785, he appointed La Pérouse to lead a sailing expedition around the world. 
    (La Pérouse and his fleet disappeared after leaving Botany Bay in March 1788. 
    Louis is recorded as having asked, on the morning of his execution, "Any news of La Pérouse?".)'''

    print(len(sent_tokenize(text)))


@logger
def tokenize_sentences_and_words(text):
    # Use nltk.sent_tokenize to split the text into sentences
    sentences = nltk.sent_tokenize(text)
    # Tokenize each sentence into words
    return [nltk.word_tokenize(sentence) for sentence in sentences]


@logger
def main():
    packages_installed = check_if_nltk_packages_are_installed()
    if packages_installed:
        logging.info("The necessary nltk packages are installed. The program can continue.")

    # Test the function with a sample sentence
    sentence = str(input())  # input sentence
    # topic_tokenization()
    # verbs_list = find_verbs(sentence)
    # print(verbs_list)
    word_list = tokenize_sentences_and_words(sentence)
    print(*word_list)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s',
                        filename='app.log',  # Specify the file name for logging
                        filemode='w'  # Use 'w' mode to overwrite the log file on each run, or 'a' to append
                        )
    logging.info("**** solution started ****")
    main()
