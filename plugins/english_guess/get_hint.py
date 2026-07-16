import json
import os.path


def get_hint(
    in_word: str,  # 在单词里，但位置不对
    incorrect: str,
    length: int,
    correct: dict = None,  # 位置正确的字母
):
    data_path = os.path.join(os.path.dirname(__file__), "data/check_list.json")
    with open(data_path, encoding="utf-8") as file:
        legal_words = json.load(file)
    target_words = legal_words[length]
    candidates = [
        word
        for word in target_words
        if not any(alphabet in incorrect for alphabet in word)
        and all(alphabet in word for alphabet in in_word)
    ]
    if not correct:
        return candidates
    return [
        list(word)
        for word in candidates
        if all(word[index] == alphabet for alphabet, index in correct.items())
    ]

if __name__ == '__main__':
    a = get_hint(
        'sel',  # 这些字母在单词里
        'banktxporu',  # 这些字母不在单词里
        7)  # 单词长度
    print(a)  # 输出所有可能的单词
