import random

# Subjects
singular_subjects = ["He", "She", "The cat", "A boy"]
plural_subjects = ["They", "We", "The cats", "Some boys"]

# Verbs
verbs = ["go", "eat", "play", "run", "watch"]

# Objects
objects = ["to the park", "an apple", "football", "fast", "a movie"]

def generate_sentences():
    sentences = []
    for _ in range(5):
        # Randomly select subject, verb, and object
        if random.choice([True, False]):  # Randomly decide singular or plural
            subject = random.choice(singular_subjects)
            is_singular = True
        else:
            subject = random.choice(plural_subjects)
            is_singular = False
        
        verb = random.choice(verbs)
        obj = random.choice(objects)
        
        # Determine the correct verb form
        if is_singular:
            correct_verb = verb + "es" if (verb.endswith("o") or verb.endswith("h")) else (verb + "s")
        else:
            correct_verb = verb  # Plural subjects use base form of the verb
        
        # Create incorrect and correct sentences
        incorrect_sentence = f"{subject} {verb} {obj}."  # Base form used for error
        correct_sentence = f"{subject} {correct_verb} {obj}."  # Adjusted for grammar
        
        sentences.append((incorrect_sentence, correct_sentence))
    
    return sentences

# Generate and display sentences
sentences = generate_sentences()
for incorrect, correct in sentences:
    print(f"Incorrect: {incorrect}")
    print(f"Correct:   {correct}")
    print()
