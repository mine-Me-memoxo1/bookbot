from stats import  word_count, count_char, sorted_dict
import sys

def get_book_text(path: str) -> str:
    with open(path) as f:
        content = f.read()
    return content


def main():
    if len(sys.argv) != 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    path = sys.argv[1]
    content = get_book_text(path)
    num_words = word_count(content)
    print('============ BOOKBOT ============')
    print('Analyzing book found at {}...'.format(path))
    print('----------- Word Count ----------')
    print(f'Found {num_words} total words')
    print('--------- Character Count -------')
    char_dict = count_char(content)
    dict_list = sorted_dict(char_dict)
    for d in dict_list:
        if d['char'].isalpha():
            print('{}: {}'.format(d['char'], d['num']))
    print('============= END ===============')

main()