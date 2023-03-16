import random

# list of words with different probabilities
word_list = [
    "the", "the", "the", "the", "the", "the", "the", "the", "the", "the",
    "a", "a", "a", "a", "a",
    "to", "to", "to", "to", "to",
    "and", "and", "and",
    "in", "in", "in", "in",
    "that", "that", "that",
    "it", "it", "it", "it",
    "of", "of", "of",
    "for", "for", "for",
    "with", "with", "with",
    "on", "on", "on",
    "at", "at", "at",
    "by", "by", "by",
    "this", "this", "this",
    "from", "from", "from",
    "not", "not", "not",
    "but", "but", "but",
    "are", "is", "was", "were",
    "be", "been", "being",
    "have", "has", "had",
    "do", "does", "did",
    "can", "could",
    "will", "would",
    "should", "shall",
    "if", "as", "or", "so", "an", "any", "all", "no", "now",
    "up", "out", "down", "off", "over", "under",
    "just", "more", "most", "only", "then",
    "other", "some", "such", "than", "these", "those",
    "when", "where", "which", "while", "who", "whom", "whose",
    "about", "after", "before", "between", "through",
    "how", "why", "what", "which",
    "their", "our", "your", "my",
    "here", "there", "near", "far"
]

word_list += [
    "red", "blue", "green", "yellow", "orange", "purple",
    "big", "small", "tall", "short", "fat", "thin",
    "happy", "sad", "angry", "excited", "bored", "tired",
    "hot", "cold", "warm", "cool",
    "fast", "slow", "quick", "long", "short",
    "loud", "quiet", "noisy", "peaceful",
    "hard", "soft", "rough", "smooth",
    "beautiful", "ugly", "pretty", "handsome", "cute",
    "old", "young", "new", "modern",
    "funny", "serious", "silly", "crazy",
    "busy", "lazy", "active", "calm"
]

word_list += [
    "run", "walk", "jump", "hop", "skip", "crawl",
    "sing", "dance", "play", "laugh", "cry", "smile",
    "eat", "drink", "cook", "bake", "chew", "swallow",
    "see", "look", "watch", "observe", "stare", "glance",
    "hear", "listen", "pay attention", "ignore", "whisper", "shout",
    "touch", "feel", "hold", "grab", "squeeze", "kiss",
    "sleep", "rest", "relax", "meditate", "dream", "snore",
    "study", "learn", "read", "write", "teach", "think",
    "work", "clean", "fix", "build", "create", "design",
    "travel", "explore", "visit", "discover", "get lost", "return",
    "love", "hate", "like", "dislike", "admire", "despise",
    "need", "want", "desire", "crave", "require", "demand"
]

word_list += [
    "cat", "dog", "bird", "fish", "mouse", "rat",
    "car", "bus", "train", "bike", "boat", "plane",
    "house", "building", "tree", "flower", "rock", "mountain",
    "book", "pen", "pencil", "paper", "notebook", "computer",
    "phone", "tablet", "television", "camera", "radio", "speaker",
    "food", "drink", "snack", "meal", "dessert", "fruit",
    "person", "woman", "man", "child", "friend", "teacher",
    "city", "country", "world", "universe", "planet", "galaxy",
    "time", "day", "night", "week", "month", "year",
    "game", "sport", "hobby", "music", "art", "dance",
    "job", "career", "office", "worker", "boss", "customer",
    "linux"
]

word_list += [
    "harm", "kill", "injure", "death", "poverty", "hunger", "evil", "hurt",
    "treat", "love", "care", "hold", "hug", "fancy", "enjoy"
]

word_list += [
    "me", "you", "he", "she", "it",
    "my", "your", "his", "hers", "its",
    "mine", "yours", "him", "her",
    "us", "them", "they", "theirs", "ours", "our"
]

#
# generate 10 random sentences
#for i in range(10):
    # choose a random number of words for the sentence
#    num_words = random.randint(1, 10)
#    
#    # choose that many random words from the list
#    sentence = " ".join([random.choice(word_list) for j in range(num_words)])
#    
#    # print the sentence
#    print(sentence.capitalize() + ".")
#

# Define the number of stanzas and lines per stanza
num_stanzas = random.randint(2, 50)
lines_per_stanza = random.randint(2, 8)

# Open a file for writing the poem
with open("poem.txt", "w") as f:

    # Generate the stanzas
    for i in range(num_stanzas):
        f.write("\n")

        # Generate the lines
        for j in range(lines_per_stanza):
            # choose a random number of words for the sentence
            num_words = random.randint(3, 10)
    
            # choose that many random words from the list
            sentence = " ".join([random.choice(word_list) for k in range(num_words)])
    
            # capitalize the first letter of the sentence
            sentence = sentence.capitalize()
    
            # add punctuation to the end of the sentence
            if j == lines_per_stanza - 1:
                sentence += "."
            else:
                sentence += ","
    
            # write the line to the file
            f.write(sentence + "\n")
