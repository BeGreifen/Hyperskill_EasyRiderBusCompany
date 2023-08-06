import nltk
#  nltk.download('punkt')  # Download the required data for tokenization

def split_sentences(text):
    # Use nltk.sent_tokenize to split the text into sentences
    return nltk.sent_tokenize(text)

# Test with sample input
sample_input = input()
result = split_sentences(sample_input)
print(result)
