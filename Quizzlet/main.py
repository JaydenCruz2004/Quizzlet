def main():
    translations = {
        "hello": "hola",
        "dog": "perro",
        "cat": "gato",
        "well": "bien",
        "us": "nos",
        "nothing": "nada",
        "house": "casa",
        "time": "tiempo"
    }

    correct_count = 0
    total_questions = len(translations)

    #print("Welcome to the Spanish translation quiz!\n")

    for english_word, spanish_translation in translations.items():
        user_answer = input(f"What is the Spanish translation for {english_word}?").strip().lower()
        if user_answer == spanish_translation:
            print("That is correct!\n")
            correct_count += 1
        else:
            print(f"That is incorrect, the Spanish translation for {english_word} is {spanish_translation}.\n")

    print(f"You got {correct_count}/{total_questions} words correct, come study again soon!")

if __name__ == '__main__':
    main()
