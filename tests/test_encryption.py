#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
骰子加解密系统单元测试

测试加解密算法的正确性和一致性
"""

import sys
import os
import unittest

# 将src目录添加到模块搜索路径
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'src'))

from f_c import chinese2pinyin, pinyin2chinese, chinese_punctuation_to_ascii
from f_c import cross_product, multiple_cross_product

class TestChineseConversion(unittest.TestCase):
    """测试中文转换功能"""
    
    def test_chinese_to_pinyin(self):
        """测试中文转拼音"""
        self.assertEqual(chinese2pinyin("你好"), "ni3 hao3")
        self.assertEqual(chinese2pinyin("世界"), "shi4 jie4")
    
    def test_pinyin_to_chinese(self):
        """测试拼音转中文字符"""
        self.assertEqual(pinyin2chinese("ni3"), "nǐ")
        self.assertEqual(pinyin2chinese("hao3"), "hǎo")
    
    def test_punctuation_conversion(self):
        """测试中文标点转换"""
        self.assertEqual(chinese_punctuation_to_ascii("你好，世界！"), "你好,世界!")
        self.assertEqual(chinese_punctuation_to_ascii("（测试）"), "(测试)")

class TestVectorOperations(unittest.TestCase):
    """测试向量运算"""
    
    def test_cross_product(self):
        """测试叉乘运算"""
        self.assertEqual(cross_product((1,0,0), (0,1,0)), (0,0,1))
        self.assertEqual(cross_product((0,1,0), (0,0,1)), (1,0,0))
    
    def test_multiple_cross_product(self):
        """测试多重叉乘"""
        vectors = [(1,0,0), (0,1,0), (0,0,1)]
        self.assertEqual(multiple_cross_product(vectors[:1]), (1,0,0))
        self.assertEqual(multiple_cross_product(vectors[:2]), (0,0,1))

class TestEncryptionDecryption(unittest.TestCase):
    """测试加密解密过程的一致性"""
    
    def test_encryption_decryption_consistency(self):
        """测试加密后解密是否一致"""
        # 这里需要实现加密解密一致性测试
        # 由于涉及到UI组件，这部分测试可能需要重构加解密.py
        # 将核心加解密逻辑抽离出来才能进行有效测试
        pass

if __name__ == "__main__":
    unittest.main() 