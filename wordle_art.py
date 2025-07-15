goal = """BYBYB
YYYYY
YYYYY
BYYYB
BBYBB
BBBBB
"""

def main():
    wotd = input("Enter the Word of the Day: ").strip().upper()

    if len(wotd) != 5:
        print("The Word of the Day must be exactly 5 letters long.")
        return
    
    word_list = read_word_list()

    # with open("wordle-answers-alphabetical.txt", "r") as file:
    #     wordle_answers = [line.strip().upper() for line in file if len(line.strip()) == 5]

    # total_answers = len(wordle_answers)
    # valid_answers = 0

    # for word in wordle_answers:
    #     if pattern_is_possible(word, goal, word_list):
    #         valid_answers += 1
    #         print(f"Possible word: {word}")

    # print(f"{valid_answers / total_answers * 100}% of the answers are possible with the given pattern.")



    output = []
    
    for line in goal.splitlines():

        line = line.strip()

        word_i = 0
        found = False

        while not found:

            if word_i >= len(word_list):
                print("No suitable word found for line:", line)
                return

            word_line = display(word_list[word_i], wotd)
            if word_line == line:
            
                found = True
                output.append(word_list[word_i])

            word_i += 1

    print(output)
    return


def pattern_is_possible(wotd, pattern, word_list):
    output = []
    
    for line in goal.splitlines():

        line = line.strip()

        word_i = 0
        found = False

        while not found:

            if word_i >= len(word_list):
                #print("No suitable word found for line:", line)
                return False

            word_line = display(word_list[word_i], wotd)
            if word_line == line:
            
                found = True
                output.append(word_list[word_i])

            word_i += 1
    return True


def read_word_list():
    with open("valid-wordle-words.txt", "r") as file:
        return [line.strip().upper() for line in file if len(line.strip()) == 5]
    
def display(word, wotd):
    output = ""
    occurences = {}
    for pos, letter in enumerate(word):
        if word[pos] == wotd[pos]:
            output += "G"

        elif letter in wotd:
            if letter not in occurences.keys():
                occurences[letter] = 0

            if occurences[letter] < wotd.count(letter):
                output += "Y"
            else:
                output += "B"
        else:
            output += "B"
        
        if letter in occurences.keys():
            occurences[letter] += 1
        else:
            occurences[letter] = 1

    return output

if __name__ == "__main__":
    main()