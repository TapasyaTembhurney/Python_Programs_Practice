import sys

def search_word(word, string):
    return string.count(word)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python searchword.py <filename> <word>")
    else:
        filename = sys.argv[1]
        word = sys.argv[2]

        with open(filename) as f:
            string = f.read()
            n = search_word(word, string)
            print(n)