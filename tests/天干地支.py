def calculate_ganzhi(year):
    # 定义天干和地支
    tiangan = ['甲', '乙', '丙', '丁', '戊', '己', '庚', '辛', '壬', '癸']
    dizhi = ['子', '丑', '寅', '卯', '辰', '巳', '午', '未', '申', '酉', '戌', '亥']

    # 计算天干和地支的索引
    # 减去4是因为天干地支的起点是甲子年，即公元4年
    gan_index = (year - 4) % 10
    zhi_index = (year - 4) % 12

    # 返回计算结果
    return tiangan[gan_index] + dizhi[zhi_index]


year = 244
print(f"{year}年的天干地支是：{calculate_ganzhi(year)}")