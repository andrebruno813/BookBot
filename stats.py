def word_count(text: str) -> int:
    return len(text.split())

def count_characters(text: str) -> dict[str, int]:
    new_text = text.lower()
    dic = {}
    for c in new_text:
        if c in dic:
            dic[c] += 1
        else:
            dic[c] = 1
    return dic

def sort_on(t: tuple[str, int]) -> int:
    return t[1];

def chars_dict_to_sorted_list(d: dict[str, int]) -> list[tuple[str, int]]:
    new_list = []
    for c in d:
        count = d[c]
        new_list.append((c, count))
    sorted(new_list, key=sort_on, reverse=True)
    return new_list


#print(count_characters("Boot!"))
