from posterior_probility import calculate_posterior_probability
from letter_prediction import predict_next_letter

import random
import string

class hangman:

    def extract_data(self, filename, total_count):
        sum = 0
        infile = open(filename, "r")
        data = {}
        sum = 0
        for line in infile:
            words = line.split()
            data[words[0]] = int(words[1])
            number = int(words[1])
            sum += number

        total_count.append(sum)
        infile.close()
        return data

    def calculateFrequencies(self):

        probabilities = {}
        total_count = []

        data = self.extract_data("word_counts.txt", total_count)

        print(total_count[0])

        for word, count in data.items():
            probabilities[word] = (count / total_count[0])

        return probabilities
   

    def playHangman(self, filename):


        total_count = []

        data = self.extract_data(filename, total_count)

        secret_word = random.choice(list(data.keys()))  # choose a random word from the list

        guess_list = [] # list of all guesses so far both incorrect and incorrect

        print("A secret word has been chosen.")
        mystery = ['?' for letter in secret_word]


        gameOver = False
        guessCount = 0
        guessString = ""

        while not gameOver:
            nextLetter= ""
            print("{0} guesses so far: {1}".format(guessCount, guessString))
            print(mystery)

            frequencies = calculateFrequencies()

            probab_dict = calculate_posterior_probability(mystery, guess_list, frequencies)

            letter_probab = predict_next_letter( mystery, guess_list,probab_dict)  # get the probabilities


            sorted_letter_probabs = []
            sorted_letter_probabs = sorted(letter_probab.items(), key=lambda x: x[1], reverse=True)

            nextLetter =sorted_letter_probabs[0][0]

            guess_list.append(nextLetter)



            guessCount += 1
            guessString += nextLetter
            missingLetters = 0
            for i in range(0, len(mystery)):
                if secret_word[i] == nextLetter:
                    mystery[i] = secret_word[i]
                if mystery[i] == "?": 
                    missingLetters += 1
            gameOver = missingLetters <= 0
        print("Game over. It took {0} guesses to get the word {1}.".format(guessCount, secret_word))



hangman().playHangman("word_counts.txt")

