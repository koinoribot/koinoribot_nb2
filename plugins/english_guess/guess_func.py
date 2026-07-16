import os
import random
import re

from ...utils import load_data


check_list = load_data(os.path.join(os.path.dirname(__file__), 'data/check_list.json'))
level_trans = {'四级': 'cet_4', '六级': 'cet_6', '专八': 'level_8', '八级': 'level_8'}
level_trans_jp = {'n5': 'n45', 'n4': 'n45', 'n3': 'n3', 'n2': 'n2', 'n1': 'n1', 'all': 'all', 'n45': 'n45'}



def load_dict(level: str = '四级', word_len: int = 5):
    if level not in ['四级', '六级', '专八', '八级']:
        raise ValueError(f"'level' got an error value: {level}")
    folder = level_trans[level]
    dictionary = load_data(os.path.join(os.path.dirname(__file__), f'data/{folder}/word_{word_len}len.json'))
    return dictionary


def load_jp_dict(level: str = 'all'):
    level = level.lower()
    if level not in ['n45', 'n3', 'n2', 'n1', 'n4', 'n5']:
        level = 'all'
    dictionary = load_data(os.path.join(os.path.dirname(__file__), f'data/japanese/{level}/{level}_list.json'))
    return dictionary


def guess_game(word_len: int, level: str = '四级'):
    """
        猜英语单词的游戏（命令提示符版）
    """
    word = ['_' for _ in range(word_len)]
    dictionary = load_dict(level, word_len)
    rand_word = random.choice(dictionary)
    get_word = rand_word['word']
    get_pos = rand_word['pos']
    get_trans = rand_word['trans']
    low_word = get_word.lower()
    while True:
        user_guess = get_input(word_len)
        print(user_guess)
        correct_pos, is_in_word = _apply_guess(
            user_guess,
            low_word,
            word,
        )
        if len(correct_pos) == word_len:
            print(f'你猜出了这个单词！\n{get_word}\n{get_pos} {get_trans}')
            return
        hint = f"[{'、'.join(is_in_word)}]在正确答案中但位置不对" if is_in_word else ''
        print(f"{format_word(word)}\n{hint}")


def _apply_guess(
    user_guess: str,
    target_word: str,
    revealed_word: list[str],
) -> tuple[list[str], list[str]]:
    correct_pos = []
    in_word = []
    for index, alphabet in enumerate(user_guess):
        if alphabet == target_word[index]:
            correct_pos.append(alphabet)
            revealed_word[index] = alphabet
        elif alphabet in target_word:
            in_word.append(alphabet)
    return correct_pos, in_word


def get_random_word(word_len: int, level: str = '四级'):
    dictionary = load_dict(level, word_len)
    rand_word = random.choice(dictionary)
    return rand_word


def get_random_tango(level: str = 'all'):
    dictionary = load_jp_dict(level)
    rand_tango = random.choice(dictionary)
    return rand_tango


def get_input(word_len: int):
    while True:
        uinput = input('请猜一猜这个单词：').lower()
        if len(uinput) != word_len:
            print(f'长度不对，要猜的单词只有{word_len}个字母')
            continue
        if uinput in check_list:
            return uinput
        print('这个单词是四六级/专八词汇吗')


def kana_yomi_splt(word: str):
    """
        将假名与读音分开
    """
    rematch = re.findall(r'([\u30a1-\u30f6\u3041-\u3093\uFF00-\uFFFF\u4e00-\u9fa5]+)([⓪①②③④⑤⑥⑦⑧⑨⑩]+(或[⓪①②③④⑤⑥⑦⑧⑨⑩]+)?)?', word)
    kana = rematch[0][0]
    yomi = rematch[0][1]
    return kana, yomi


def format_word(word: list):
    string = ''.join(word)
    return string


if __name__ == '__main__':
    guess_game(7)
