import tkinter as tk
from tkinter import messagebox
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

def generate_sentence():
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

    # Create correct sentence
    correct_sentence = f"{subject} {correct_verb} {correct_obj}."
    return correct_sentence, correct_verb, verb

def shuffle_sentence(sentence, correct_verb, incorrect_verb):
    words = sentence[:-1].split()  # Remove period and split into words
    # Add incorrect verb form for challenge (if they are different forms)
    if (incorrect_verb != correct_verb):
        words.append(incorrect_verb)
    random.shuffle(words)
    return words

def generate_challenge():
    global current_correct_sentence, current_correct_verb
    # Generate a sentence
    correct_sentence, correct_verb, incorrect_verb = generate_sentence()
    shuffled_words = shuffle_sentence(correct_sentence, correct_verb, incorrect_verb)

    # Display the shuffled words
    words_frame.destroy()
    populate_words_frame(shuffled_words)

    # Store the correct sentence for validation
    current_correct_sentence = correct_sentence
    current_correct_verb = correct_verb

def populate_words_frame(words):
    global words_frame
    words_frame = tk.Frame(window)
    words_frame.pack(pady=10)

    for word in words:
        word_button = tk.Button(words_frame, text=word, font=("Arial", 12), command=lambda w=word: select_word(w))
        word_button.pack(side=tk.LEFT, padx=5)

def select_word(word):
    user_sentence_var.set(user_sentence_var.get() + word + " ")

def remove_last_word():
    current_sentence = user_sentence_var.get().strip().split()
    if current_sentence:
        current_sentence.pop()  # Remove the last word
        user_sentence_var.set(" ".join(current_sentence) + " ")

def check_sentence():
    user_sentence = user_sentence_var.get().strip() + "."
    if user_sentence == current_correct_sentence:
        messagebox.showinfo("Result", "Correct! Well done!")
    else:
        messagebox.showerror("Result", f"Incorrect. The correct sentence is:\n{current_correct_sentence}")
    # Reset for the next challenge
    user_sentence_var.set("")
    generate_challenge()

# Initialize the main application window
window = tk.Tk()
window.title("Subject-verb agreement practice")
window.geometry("600x500")

# Instructions label
instructions = tk.Label(window, text="Reorder the words to form the correct sentence:", font=("Arial", 14))
instructions.pack(pady=10)

# Words frame to hold shuffled words
words_frame = tk.Frame(window)
words_frame.pack(pady=10)

# User input field
user_sentence_var = tk.StringVar()
user_sentence_label = tk.Label(window, textvariable=user_sentence_var, font=("Arial", 12), bg="white", height=2, width=50, relief=tk.SUNKEN)
user_sentence_label.pack(pady=10)

# Buttons for actions
button_frame = tk.Frame(window)
button_frame.pack(pady=5)

check_button = tk.Button(button_frame, text="Check Sentence", font=("Arial", 14), command=check_sentence)
check_button.pack(side=tk.LEFT, padx=10)

remove_button = tk.Button(button_frame, text="Remove Last Word", font=("Arial", 14), command=remove_last_word)
remove_button.pack(side=tk.LEFT, padx=10)

# Generate a challenge initially
current_correct_sentence = ""
current_correct_verb = ""
generate_challenge()

# Run the application
window.mainloop()
