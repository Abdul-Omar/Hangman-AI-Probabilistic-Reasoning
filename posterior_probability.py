
 def calculate_posterior_probability( mystery, guess_list, frequencies):

        probab_dict = {}  # hold prob each word is a viable option

        # frequencies of all the words from file=> stuff we calculated in the previous step step 1
        frequency = self.calculateFrequencies()
        for word in frequency.keys():
            matched = True;
            for i in range(len(word)):

                if mystery[i] != "?":
                    if word[i] != mystery[i]:
                        matched = False;
                else:

                    if word[i] in guess_list:
                        matched = False

            if matched:

                probab_dict[word] = 1 * frequency[word]
            else:

                probab_dict[word] = 0

        prob_sum = 0;

        for word in probab_dict.keys():

            prob_sum += probab_dict[word]

        for word in probab_dict.keys():
            probab_dict[word] = (probab_dict[word]) / prob_sum

        return probab_dict