def count_vowels_and_consonants(word):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    consonant_count = 0

    for char in word:
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1

    return vowel_count, consonant_count

def main():
    user_word = input("Enter a word: ")
    vowel_count, consonant_count = count_vowels_and_consonants(user_word)

    print(f"Number of vowels: {vowel_count}")
    print(f"Number of consonants: {consonant_count}")

if __name__ == "__main__":
    main()
