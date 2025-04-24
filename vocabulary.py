#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 23 18:13:29 2025

@author: anuppaul
"""

import pandas as pd
import random
import matplotlib.pyplot as plt

# Load the Excel file (from the specified path)
file_path = '/Users/anuppaul/Downloads/spyder/flashcard/data/HSK1_Vocabulary.xlsx'
df = pd.read_excel(file_path)

# Store the results for correct and incorrect answers
correct_words_chinese_to_english = []
incorrect_words_chinese_to_english = []
total_questions_chinese_to_english = 0

correct_words_english_to_chinese = []
incorrect_words_english_to_chinese = []
total_questions_english_to_chinese = 0

def show_results(chinese_to_english=True):
    global correct_words_chinese_to_english, incorrect_words_chinese_to_english, total_questions_chinese_to_english
    global correct_words_english_to_chinese, incorrect_words_english_to_chinese, total_questions_english_to_chinese

    if chinese_to_english:
        # Results for Chinese-to-English session
        correct_count = len(correct_words_chinese_to_english)
        incorrect_count = len(incorrect_words_chinese_to_english)
        total_questions = total_questions_chinese_to_english
    else:
        # Results for English-to-Chinese session
        correct_count = len(correct_words_english_to_chinese)
        incorrect_count = len(incorrect_words_english_to_chinese)
        total_questions = total_questions_english_to_chinese

    # Display the score and results
    print(f"\nRESULTS:")
    print(f"Total Questions Attempted: {total_questions}")
    print(f"Correct Answers: {correct_count}")
    print(f"Incorrect Answers: {incorrect_count}")
    
    # Create a bar chart for results
    categories = ['Total Questions', 'Correct Answers', 'Incorrect Answers']
    values = [total_questions, correct_count, incorrect_count]
    
    # Plot the bar chart
    plt.bar(categories, values, color=['blue', 'green', 'red'])
    plt.title('Flashcard Results')
    plt.ylabel('Number of Answers')
    plt.show()

def chinese_to_english_flashcard():
    global total_questions_chinese_to_english, correct_words_chinese_to_english, incorrect_words_chinese_to_english
    
    # Show the prompt only once
    print("\nFlashcard Session Started for Chinese to English. Type 'end' to stop, 'result' to see results, or 'dk' to show the correct answer and continue.\n")
    
    while True:
        # Randomly select a row from the DataFrame
        word = df.sample(n=1).iloc[0]
        chinese_char = word['Chinese']
        correct_answer = word['English']
        print(f"Chinese: {chinese_char}")
        
        user_answer = input("What is the English meaning? ").strip()

        if user_answer.lower() == 'end':
            print("Practice session ended.")
            break
        elif user_answer.lower() == 'result':
            show_results(chinese_to_english=True)
            continue
        elif user_answer.lower() == 'dk':
            # Show the correct answer and continue to the next word
            print(f"The correct answer is: {correct_answer} (Pinyin: {word['Pinyin']})\n")
            incorrect_words_chinese_to_english.append(word)  # Add to incorrect answers
            continue

        # First check if the answer is correct
        total_questions_chinese_to_english += 1
        if user_answer.lower() == correct_answer.lower():
            print("Correct! Moving to the next word.\n")
            correct_words_chinese_to_english.append(word)
        else:
            # Retry mechanism
            retry_count = 0
            while retry_count < 1:
                user_answer = input(f"Wrong. Try again. What is the English meaning for '{chinese_char}'? ").strip()
                if user_answer.lower() == 'end':
                    print("Practice session ended.")
                    return
                elif user_answer.lower() == 'result':
                    show_results(chinese_to_english=True)
                    continue
                elif user_answer.lower() == 'dk':
                    # Show the correct answer and continue to the next word
                    print(f"The correct answer is: {correct_answer} (Pinyin: {word['Pinyin']})\n")
                    incorrect_words_chinese_to_english.append(word)  # Add to incorrect answers
                    break

                if user_answer.lower() == correct_answer.lower():
                    print("Good! Moving to the next word.\n")
                    correct_words_chinese_to_english.append(word)
                    break
                else:
                    retry_count += 1
                    if retry_count == 1:  # After one wrong attempt, show the correct answer and pinyin
                        print(f"Wrong again. The correct answer is: {correct_answer} (Pinyin: {word['Pinyin']})\n")
                        print("Moving to the next word.\n")
                        incorrect_words_chinese_to_english.append(word)
                        break

# Run the Chinese to English flashcard system
chinese_to_english_flashcard()

def english_to_chinese_flashcard():
    global total_questions_english_to_chinese, correct_words_english_to_chinese, incorrect_words_english_to_chinese
    
    # Show the prompt only once
    print("\nFlashcard Session Started for English to Chinese. Type 'end' to stop, 'result' to see results, or 'dk' to show the correct answer and continue.\n")
    
    while True:
        # Randomly select a row from the DataFrame
        word = df.sample(n=1).iloc[0]
        english_word = word['English']
        correct_answer = word['Chinese']
        print(f"English: {english_word}")
        
        user_answer = input("What is the Chinese translation? ").strip()

        if user_answer.lower() == 'end':
            print("Practice session ended.")
            break
        elif user_answer.lower() == 'result':
            show_results(chinese_to_english=False)
            continue
        elif user_answer.lower() == 'dk':
            # Show the correct answer and continue to the next word
            print(f"The correct answer is: {correct_answer} (Pinyin: {word['Pinyin']})\n")
            incorrect_words_english_to_chinese.append(word)  # Add to incorrect answers
            continue

        # First check if the answer is correct
        total_questions_english_to_chinese += 1
        if user_answer == correct_answer:
            print("Good! Moving to the next word.\n")
            correct_words_english_to_chinese.append(word)
        else:
            # Retry mechanism
            retry_count = 0
            while retry_count < 1:
                user_answer = input(f"Wrong. Try again. What is the Chinese translation for '{english_word}'? ").strip()
                if user_answer.lower() == 'end':
                    print("Practice session ended.")
                    return
                elif user_answer.lower() == 'result':
                    show_results(chinese_to_english=False)
                    continue
                elif user_answer.lower() == 'dk':
                    # Show the correct answer and continue to the next word
                    print(f"The correct answer is: {correct_answer} (Pinyin: {word['Pinyin']})\n")
                    incorrect_words_english_to_chinese.append(word)  # Add to incorrect answers
                    break

                if user_answer == correct_answer:
                    print("Good! Moving to the next word.\n")
                    correct_words_english_to_chinese.append(word)
                    break
                else:
                    retry_count += 1
                    if retry_count == 1:  # After one wrong attempt, show the correct answer and pinyin
                        print(f"Wrong again. The correct answer is: {correct_answer} (Pinyin: {word['Pinyin']})\n")
                        print("Moving to the next word.\n")
                        incorrect_words_english_to_chinese.append(word)
                        break

# Run the English to Chinese flashcard system
english_to_chinese_flashcard()
