from random import randint
from tqdm import tqdm
import f_c


def char_shift(char, shift):
    if ord(char) not in range(33, 127):
        return char
    return printable_chars[(reversed_printable_chars[char] + shift) % len(printable_chars)]


def roll_dice(Char, encode=1):
    ds1 = '{:08b}'.format(ord(Char))[::encode]
    ds2 = ds1.replace('1', 'U' if encode == 1 else 'u').replace('0', 'R' if encode == 1 else 'r')
    ds2 = f_c.apply_replacements(ds2)

    while len(ds2) > 3:  # 可以 while循环结合 if break 语句来模拟 do-while 的行为
        ds = [ds2[i:i + 4] for i in range(0, len(ds2), 4)]
        ds2 = ''
        for d in ds:
            for dire in 'UFR':
                d = f_c.apply_replacements(d)
                if len(d) < 4:
                    break
                d = f_c.frontMove(d, dire)
            ds2 += d

    V = [char_to_vector[d] for d in ds2]
    result_uv = f_c.multiple_cross_product([f_c.dice_vectors[UP]] + V)
    result_fv = f_c.multiple_cross_product([f_c.dice_vectors[FRONT]] + V)

    RESULT = [f_c.reversed_dice_vectors[result_uv], f_c.reversed_dice_vectors[result_fv]]

    return f_c.get_new_d(UP, FRONT, RESULT[0], RESULT[1])


printable_chars = {index: chr(v) for index, v in enumerate(list(range(33, 127)))}
reversed_printable_chars = {v: k for k, v in printable_chars.items()}

UP = randint(1, 6)
FRONT = randint(1, 6)
while UP + FRONT == 7 or UP == FRONT:
    FRONT = randint(1, 6)
UP_v = f_c.dice_vectors[UP]
FRONT_v = f_c.dice_vectors[FRONT]
RIGHT_v = f_c.cross_product(UP_v, FRONT_v)
char_to_vector = {
    "U": RIGHT_v, "F": UP_v, "R": FRONT_v,
    "u": tuple(-x for x in RIGHT_v), "f": tuple(-x for x in UP_v), "r": tuple(-x for x in FRONT_v)
}

with open("1.txt", 'r', encoding='utf-8') as f:
    plaintext = f.read()

punctuation_text = f_c.chinese_punctuation_to_ascii(plaintext)
pinyin_text = f_c.chinese2pinyin(punctuation_text)
with open("pinyin_text.txt", 'w', encoding='utf-8') as f:
    f.write(pinyin_text)

ciphertext = ""
pbar = tqdm(total=len(pinyin_text), desc="Processing")

for char in pinyin_text:
    pbar.update(1)
    if ord(char) in range(33, 127):
        UP, FRONT = roll_dice(char)
    ciphertext += char_shift(char, UP)

with open("ciphertext.txt", 'w', encoding='utf-8') as f:
    f.write(f'{UP}, {FRONT}\n')
    f.write(ciphertext)

UP = 1
FRONT = 2
decrypted_plaintext = ""
for char in ciphertext[::-1]:
    new_char = char_shift(char, -UP)
    decrypted_plaintext += new_char
    if ord(new_char) in range(33, 127):
        UP, FRONT = roll_dice(new_char, -1)

decrypted_plaintext = decrypted_plaintext[::-1]
with open("decrypted_plaintext.txt", 'w', encoding='utf-8') as f:
    f.write(decrypted_plaintext)

pinyin_plaintext = f_c.pinyin2chinese(decrypted_plaintext)
with open("pinyin_plaintext.txt", 'w', encoding='utf-8') as f:
    f.write(pinyin_plaintext)
