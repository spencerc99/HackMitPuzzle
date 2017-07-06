import urllib
import string

"""
Function to remove duplicates from list and preserve order
"""
def f7(seq):
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]

data = urllib.urlopen('http://www.scifiscripts.com/scripts/backtothefuture_transcript.txt').read() # it's a file like object and works just like a file
# remove punctuation
data = data.lower()
data = data.replace('\n', ' ')
data = data.translate(None, string.punctuation)
# remove new line characters
# split into words
# data = data.strip()
words = data.split(" ")
# get rid of blank ''
# words = filter(None, words)
def isalpha(word):
    for letter in word:
        if letter.isalpha():
            return True
    return False

words = filter(isalpha, words)
words = f7(words)

print words
print len(words)

inp = "the microsoft of ecommerce but like mongodb"
# inp = "the pandora of sports but like paypal"
# inp = "the hubspot of hotels but like houzz"
print words[32 * 3 + 26]

result = []
for idx, letter in enumerate(inp):
    val = ord(letter) if letter.isalpha() else ord('a') + 26
    result.append(words[(32 * idx) + (val - ord('a'))])

print " ".join(result)
