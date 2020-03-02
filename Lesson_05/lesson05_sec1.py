
empty= {}

# ex 2
def word_count(file):
    with open(file,'r') as myfile:
        for line in myfile:
            line = line.split()
            for i in line:
                word_length = len(i)
                empty[i] = word_length
                # print(i.lower(), word_length)
        print(empty)

word_count('sonnet.txt')