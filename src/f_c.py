import copy
import itertools
from pypinyin import pinyin, Style


def chinese2pinyin(text):
    pinyin_list = pinyin(text, style=Style.TONE2, heteronym=False)
    pinyin_str = ' '.join([item[0] for item in pinyin_list])
    return pinyin_str


def pinyin2chinese(text):
    tone_map = {
        'a1': 'ā', 'a2': 'á', 'a3': 'ǎ', 'a4': 'à',
        'e1': 'ē', 'e2': 'é', 'e3': 'ě', 'e4': 'è',
        'i1': 'ī', 'i2': 'í', 'i3': 'ǐ', 'i4': 'ì',
        'o1': 'ō', 'o4': 'ó', 'o3': 'ǒ', 'o2': 'ò',
        'u1': 'ū', 'u2': 'ú', 'u3': 'ǔ', 'u4': 'ù',
        'v1': 'ǖ', 'v2': 'ǘ', 'v3': 'ǚ', 'v4': 'ǜ',
    }
    for tone in tone_map:
        text = text.replace(tone, tone_map[tone])
    return text


def chinese_punctuation_to_ascii(text):
    punctuation_map = {
        '，': ',', '。': '.', '！': '!', '？': '?', '；': ';', '：': ':', '‘': "'", '’': "'", '“': '"', '”': '"', '—': '--',
        '…': '...', '（': '(', '）': ')', '【': '[', '】': ']', '《': '<', '》': '>', '～': '~', '、': ',', '·': '.', '〈': '<',
        '〉': '>', '〔': '[', '〕': ']', '／': '/', '．': '.', '－': '-'
    }
    for chinese, english in punctuation_map.items():
        text = text.replace(chinese, english)
    return text


def cross_product(a, b):
    return (
        a[1] * b[2] - a[2] * b[1],
        a[2] * b[0] - a[0] * b[2],
        a[0] * b[1] - a[1] * b[0]
    )


def multiple_cross_product(vectors):
    result = vectors[0]
    if len(vectors) < 2:
        return result
    for vector in vectors[1:]:
        result = result if cross_product(result, vector) == (0, 0, 0) else cross_product(result, vector)
    return result


def frontMove(t, d):
    while len(t) > 2:
        for i in range(len(t) - 1):
            if t[i].upper() != d:
                if t[i].upper() != t[i + 1].upper():
                    replace_text = replacements2[t[i:i + 2]]
                    for index, char in enumerate(replace_text):
                        if char.upper() == d and index % 2 == 0:
                            t = t[:i] + replace_text[index:index + 2] + t[i + 2:]
                            break
        first_non_d_index = next((i for i, char in enumerate(t.upper()) if char != d), len(t))
        last_d_index = t.upper().rfind(d)
        if t[0].upper() == d and first_non_d_index > last_d_index:
            break
    return t


def apply_replacements(d):
    for old, new in replacements1.items():
        d = d.replace(old, new)
    return d


dice_vectors = {1: (0, 0, 1), 2: (1, 0, 0), 3: (0, 1, 0), 6: (0, 0, -1), 5: (-1, 0, 0), 4: (0, -1, 0)}
reversed_dice_vectors = {v: k for k, v in dice_vectors.items()}

replacements1 = {
    "UUU": "u", "RRR": "r", "FFF": "f", "uuu": "U", "rrr": "R", "fff": "F",
    "Rr": "", "rR": "", "Uu": "", "uU": "", "Ff": "", "fF": ""
}

replacements2 = {}
for i, j in itertools.product('RUFruf', repeat=2):
    if i.upper() != j.upper():
        k = [item for item in 'UFR' if item.upper() not in [i.upper(), j.upper()]][0]
        k = k.lower() if i.islower() else k
        if (i.upper() + j.upper()) in ('UFR' + 'U'):
            replacements2[i + j] = k + i if j.isupper() else k.swapcase() + i
        else:
            replacements2[i + j] = k.swapcase() + i if j.isupper() else k + i
replacements2_clone = copy.deepcopy(replacements2)
for k, v in replacements2_clone.items():
    replacements2[v] += k

right_dic = {}
for i in range(1, 7):
    for j in range(1, 7):
        if i + j != 7 and i != j:
            for k, v in dice_vectors.items():
                if v == cross_product(dice_vectors[i], dice_vectors[j]):
                    right_dic[(i, j)] = k


def get_new_d(UP, FRONT, RESULT1, RESULT2):
    NEW_FRONT = NEW_UP = None
    Flag = 1
    RIGHT = right_dic[(UP, FRONT)]

    if RESULT1 == UP:
        NEW_UP = UP
        Flag = 1
    elif 7 - RESULT1 == UP:
        NEW_UP = 7 - UP
        Flag = 0
    elif RESULT2 == UP:
        NEW_UP = FRONT
        Flag = 1
    elif 7 - RESULT2 == UP:
        NEW_UP = 7 - FRONT
        Flag = 0

    if RESULT1 == FRONT:
        NEW_FRONT = UP
        Flag = 1
    elif 7 - RESULT1 == FRONT:
        NEW_FRONT = 7 - UP
        Flag = 0
    elif RESULT2 == FRONT:
        NEW_FRONT = FRONT
        Flag = 1
    elif 7 - RESULT2 == FRONT:
        NEW_FRONT = 7 - FRONT
        Flag = 0

    if not NEW_UP:
        if RESULT1 == RIGHT:
            NEW_UP = 7 - RIGHT if Flag else RIGHT
        elif 7 - RESULT1 == RIGHT:
            NEW_UP = RIGHT if Flag else 7 - RIGHT
        elif RESULT2 == RIGHT:
            NEW_UP = RIGHT if Flag else 7 - RIGHT
        elif 7 - RESULT2 == RIGHT:
            NEW_UP = 7 - RIGHT if Flag else RIGHT

    if not NEW_FRONT:
        if RESULT1 == RIGHT:
            NEW_FRONT = RIGHT if Flag else 7 - RIGHT
        elif 7 - RESULT1 == RIGHT:
            NEW_FRONT = 7 - RIGHT if Flag else RIGHT
        elif RESULT2 == RIGHT:
            NEW_FRONT = 7 - RIGHT if Flag else RIGHT
        elif 7 - RESULT2 == RIGHT:
            NEW_FRONT = RIGHT if Flag else 7 - RIGHT

    return NEW_UP, NEW_FRONT