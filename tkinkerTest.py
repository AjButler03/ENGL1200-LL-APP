import tkinter as tk
from tkinter import scrolledtext
import random

# Subjects
singular_subjects = ["He", "She", "The cat", "A boy"]
plural_subjects = ["They", "We", "The cats", "Some boys"]

# Verbs and rules for "to" inclusion
verbs_with_to = ["go", "run", "travel"]
verbs_without_to = ["eat", "play", "watch", "see"]

# Objects
objects_needing_to = ["the park", "school", "the store"]
objects_no_to = ["an apple", "football", "a movie", "fast"]

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
            correct_verb = verb + "es" if (verb.endswith("o") or verb.endswith("h")) else (verb + "s")
        else:
            correct_verb = verb
        
        # Add "to" if needed
        correct_obj = f"to {obj}" if needs_to else obj
        
        # Create sentences
        incorrect_sentence = f"{subject} {verb} {obj}."  # Base form used for error
        correct_sentence = f"{subject} {correct_verb} {correct_obj}."  # Adjusted for grammar
        
        sentences.append((incorrect_sentence, correct_sentence))
    
    return sentences

def display_sentences():
    text_box.delete('1.0', tk.END)  # Clear the text box
    sentences = generate_sentences()
    for incorrect, correct in sentences:
        # text_box.insert(tk.END, f"Incorrect: {incorrect}\n") # not needed
        text_box.insert(tk.END, f"Correct:   {correct}\n\n")

# Create the main application window
window = tk.Tk()
window.title("Subject-Verb Agreement Example Generator")
window.geometry("600x400")

# Add a button to generate sentences
generate_button = tk.Button(window, text="Generate Sentences", command=display_sentences, font=("Arial", 14))
generate_button.pack(pady=10)

# Add a scrollable text box to display sentences
text_box = scrolledtext.ScrolledText(window, wrap=tk.WORD, font=("Arial", 12), width=70, height=20)
text_box.pack(pady=10)

# Run the application
window.mainloop()
