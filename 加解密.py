import sys
from random import randint
from PyQt5.QtWidgets import QMainWindow, QApplication
import f_c
from jiajiemi import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('加解密')
        self.setFixedSize(800, 600)
        self.ui.pushButton_1.clicked.connect(self.Encode)
        self.ui.pushButton_2.clicked.connect(self.Decode)
        self.ui.pushButton_genkey.clicked.connect(self.Genkey)
        self.ui.pushButton_getkey.clicked.connect(self.Getkey)
        self.ui.pushButton_passtext.clicked.connect(self.Passtext)
        self.printable_chars = {index: chr(v) for index, v in enumerate(list(range(33, 127)))}
        self.reversed_printable_chars = {v: k for k, v in self.printable_chars.items()}

    def Passtext(self):
        self.ui.textEdit_enciphertext.setPlainText(self.ui.textEdit_ciphertext.toPlainText())

    def Randomkey(self):
        UP = randint(1, 6)
        FRONT = randint(1, 6)
        while UP + FRONT == 7 or UP == FRONT:
            FRONT = randint(1, 6)
        return UP, FRONT

    def Genkey(self):
        self.UP, self.FRONT = self.Randomkey()
        self.INIT_UP = self.UP
        self.INIT_FRONT = self.FRONT
        self.ui.lineEdit_1.setText(' '.join([str(self.UP), str(self.FRONT)]))

    def Getdir(self, UP, FRONT):
        self.UP_v = f_c.dice_vectors[UP]
        self.FRONT_v = f_c.dice_vectors[FRONT]
        self.RIGHT_v = f_c.cross_product(self.UP_v, self.FRONT_v)
        self.char_to_vector = {
            "U": self.RIGHT_v,
            "F": self.UP_v,
            "R": self.FRONT_v,
            "u": tuple(-x for x in self.RIGHT_v),
            "f": tuple(-x for x in self.UP_v),
            "r": tuple(-x for x in self.FRONT_v)
        }

    def Getkey(self):
        try:
            self.INIT_UP, self.INIT_FRONT = [int(n) for n in self.ui.lineEdit_1.text().split(' ')]
            self.UP, self.FRONT = [int(n) for n in self.ui.label_1.text()[6:].split(' ')]
            self.ui.lineEdit_2.setText(' '.join([str(self.INIT_UP), str(self.INIT_FRONT), str(self.UP), str(self.FRONT)]))
        except:
            pass

    def char_shift(self, char, shift):
        if ord(char) not in range(33, 127):
            return char
        return self.printable_chars[(self.reversed_printable_chars[char] + shift) % len(self.printable_chars)]

    def roll_dice(self, char, encode=1):
        ds1 = '{:08b}'.format(ord(char))[::encode]
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

        V = [self.char_to_vector[d] for d in ds2]
        result_uv = f_c.multiple_cross_product([f_c.dice_vectors[self.UP]] + V)
        result_fv = f_c.multiple_cross_product([f_c.dice_vectors[self.FRONT]] + V)
        RESULT = [f_c.reversed_dice_vectors[result_uv], f_c.reversed_dice_vectors[result_fv]]

        return f_c.get_new_d(self.UP, self.FRONT, RESULT[0], RESULT[1])

    def Encode(self):
        if not self.ui.lineEdit_1.text():
            self.Genkey()
        self.Getdir(self.INIT_UP, self.INIT_FRONT)
        plaintext = self.ui.textEdit_plaintext.toPlainText()
        punctuation_text = f_c.chinese_punctuation_to_ascii(plaintext)
        pinyin_text = f_c.chinese2pinyin(punctuation_text)
        ciphertext = ""
        for char in pinyin_text:
            if ord(char) in range(33, 127):
                self.UP, self.FRONT = self.roll_dice(char)
            ciphertext += self.char_shift(char, self.UP**2)
        self.ui.textEdit_ciphertext.setPlainText(ciphertext)
        self.ui.label_1.setText('加密后秘钥：' + ' '.join([str(self.UP), str(self.FRONT)]))

    def Decode(self):
        try:
            self.INIT_UP, self.INIT_FRONT, self.UP, self.FRONT = [int(n) for n in self.ui.lineEdit_2.text().split(' ')]
        except:
            self.UP, self.FRONT = self.Randomkey()
            self.INIT_UP, self.INIT_FRONT = self.Randomkey()
        finally:
            if not (self.UP in range(1, 7) and self.FRONT in range(1, 7) and
                    self.UP != self.FRONT and self.UP + self.FRONT != 7 and
                    self.INIT_FRONT in range(1, 7) and self.INIT_FRONT in range(1, 7) and
                    self.INIT_FRONT != self.INIT_UP and self.INIT_FRONT + self.INIT_UP != 7):
                self.UP, self.FRONT = self.Randomkey()
                self.INIT_UP, self.INIT_FRONT = self.Randomkey()

        self.Getdir(self.INIT_UP, self.INIT_FRONT)
        self.ui.label_2.setText('解密秘钥：' + ' '.join([str(self.INIT_UP), str(self.INIT_FRONT), str(self.UP), str(self.FRONT)]))
        ciphertext = self.ui.textEdit_enciphertext.toPlainText()
        decrypted_plaintext = ""
        for char in ciphertext[::-1]:
            new_char = self.char_shift(char, -self.UP**2)
            decrypted_plaintext += new_char
            if ord(new_char) in range(33, 127):
                self.UP, self.FRONT = self.roll_dice(new_char, -1)

        decrypted_plaintext = decrypted_plaintext[::-1]
        pinyin_plaintext = f_c.pinyin2chinese(decrypted_plaintext)
        self.ui.textEdit_deplaintext.setPlainText(pinyin_plaintext)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())