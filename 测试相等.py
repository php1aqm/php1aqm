import itertools
from random import randint
import f_c

UP = randint(1, 6)
FRONT = randint(1, 6)
NEW_UP = NEW_FRONT = None
while UP + FRONT == 7 or UP == FRONT:
    FRONT = randint(1, 6)
print(UP, FRONT)
UP = 1
FRONT = 2
UP_v = f_c.dice_vectors[UP]  # 向前翻转
FRONT_v = f_c.dice_vectors[FRONT]  # 向右翻转
RIGHT_v = f_c.cross_product(UP_v, FRONT_v)  # 向上翻转
char_to_vector = {"U": RIGHT_v, "F": UP_v, "R": FRONT_v,
                  "u": tuple(-x for x in RIGHT_v), "f": tuple(-x for x in UP_v), "r": tuple(-x for x in FRONT_v)}

V1 = []
V2 = []

for ds1 in [''.join(a) for a in itertools.product('RUFruf', repeat=4)]:  # 笛卡尔积
    ds2 = f_c.apply_replacements(ds1)
    for dire in 'UFR':
        ds2 = f_c.frontMove(ds2, dire)
        ds2 = f_c.apply_replacements(ds2)
        if len(ds2) < 4:
            break
    print(ds1, ds2)
ds1 = 'UF'
ds2 = 'RU'
for d in ds1:
    V1.append(char_to_vector[d])
for d in ds2:
    V2.append(char_to_vector[d])

multiple_cross_product = f_c.multiple_cross_product
result_uv1 = multiple_cross_product([UP_v] + V1)
result_fv1 = multiple_cross_product([FRONT_v] + V1)
result_uv2 = multiple_cross_product([UP_v] + V2)
result_fv2 = multiple_cross_product([FRONT_v] + V2)

if not (result_uv1 == result_uv2) or not (result_fv1 == result_fv2):
    print(ds1, ds2, '不相等')
else:
    print(ds1, ds2, '相等')


RESULT = [f_c.reversed_dice_vectors[result_uv1], f_c.reversed_dice_vectors[result_fv1]]
NEW_UP, NEW_FRONT = f_c.get_new_d(UP, FRONT, RESULT[0], RESULT[1])
print(NEW_UP, NEW_FRONT)