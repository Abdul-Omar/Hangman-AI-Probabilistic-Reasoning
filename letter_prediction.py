    def predict_next_letter(mystery, guess_list,probab_dict):
      """ calculates the probability of each letter to be the next letter"""

        alphabet = list(string.ascii_uppercase);

        letter_probab = {}

        # calculate probabiltiy for each letter
        for letter in alphabet:

            sum = 0.0;
            for word in probab_dict.keys():

                if letter in word and letter not in guess_list:

                    sum += (1 * probab_dict[word])

            letter_probab[letter] = sum

        return letter_probab
