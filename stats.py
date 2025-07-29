def word_count(content: str) -> str:
    return len(content.split())

def count_char(content: str) -> dict:
    char_dict = {}
    content = content.lower()
    for char in content:
        if char in char_dict:
            char_dict[char] += 1
        else :
            char_dict[char] = 1
    return char_dict


def sort_on(dictionary) -> int:
    return dictionary['num']


def sorted_dict(char_dict: dict) -> list[dict]:
    char_list = []
    for char, val in char_dict.items():
        char_list.append({'char': char, 'num': val})
    char_list.sort(reverse=True, key=sort_on)
    return char_list
