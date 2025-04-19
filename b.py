from pypinyin import pinyin, Style

text = '打电话好的，这样就难了把撒【'
pinyin_list = pinyin(text, style=Style.TONE, heteronym=False)
pinyin_str = ' '.join([item[0] for item in pinyin_list])
print(pinyin_str)