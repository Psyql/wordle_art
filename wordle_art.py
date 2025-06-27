goal = """BYBYB
BGBGB
BBBBB
GBBBG
BGGGB
BBBBB
"""

def main():
    wotd = input("Enter the Word of the Day: ").strip().upper()

    if len(wotd) != 5:
        print("The Word of the Day must be exactly 5 letters long.")
        return
    
    word_list = read_word_list()

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
            if letter in occurences.keys():
                if occurences[letter] >= wotd.count(letter):
                    break

            output += "Y"
        else:
            output += "B"
        
        if letter in occurences.keys():
            occurences[letter] += 1
        else:
            occurences[letter] = 1

    return output

if __name__ == "__main__":
    main()