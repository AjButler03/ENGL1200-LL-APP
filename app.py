import random

# Subjects
singular_subjects = ["He", "She", "The cat", "A boy"]
plural_subjects = ["They", "We", "The cats", "Some boys"]

# Verbs and rules for "to" inclusion
verbs_with_to = ["go", "run", "travel"]  # Require "to" before certain objects
verbs_without_to = ["eat", "play", "watch", "see"]  # Do not require "to"

# Objects
objects_needing_to = ["the park", "school", "the store"]
objects_no_to = ["an apple", "football", "a movie", "fast"]

def generate_sentences():
    sentences = []
    for _ in range(10):
        # Randomly select subject, verb, and object
        if random.choice([True, False]):  # Randomly decide singular or plural
            subject = random.choice(singular_subjects)
            is_singular = True
        else:
            subject = random.choice(plural_subjects)
            is_singular = False
        
        # Choose verb and object
        if random.choice([True, False]):  # Randomly decide verb type
            verb = random.choice(verbs_with_to)
            obj = random.choice(objects_needing_to)
            needs_to = True
        else:
            verb = random.choice(verbs_without_to)
            obj = random.choice(objects_no_to)
            needs_to = False
        
        # Determine correct verb form
        if is_singular:
            correct_verb = verb + "es" if verb.endswith("o") else (verb + "s")
        else:
            correct_verb = verb
        
        # Add "to" if needed
        correct_obj = f"to {obj}" if needs_to else obj
        
        # Create sentences
        incorrect_sentence = f"{subject} {verb} {obj}."  # Base form used for error
        correct_sentence = f"{subject} {correct_verb} {correct_obj}."  # Adjusted for grammar
        
        sentences.append((incorrect_sentence, correct_sentence))
    
    return sentences

# Generate and display sentences
sentences = generate_sentences()
for incorrect, correct in sentences:
    # print(f"Incorrect: {incorrect}") # not always incorrect; not needed for my idea of the app anyway
    print(f"Correct:   {correct}")
    print()
