import sys
import stats as st

def get_book_text(filepath):
    with open(filepath) as f:
        text = f.read()
    return text

def print_result(path, num_of_words, sorted_mass_temp):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("----------- Word Count ----------")
    print(f"Found {num_of_words} total words")
    print("--------- Character Count -------")
    for i in sorted_mass_temp:
        if(i["name"].isalpha()):
            print (f"{i["name"]}: {i["num"]}")
    print("============= END ===============")
    return 0



def main():
    if(len(sys.argv) != 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    # "books/frankenstein.txt"
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = st.count_words(text)
    dic = st.char_count(text)
    # print(st.sort_dic(st.char_count(text)))
    sorted_mass = st.sort_dic(dic)
    print_result(book_path, num_words, sorted_mass)
    return 0

main()
