#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
骰子加解密系统主入口

这个模块是骰子加解密系统的主入口，根据命令行参数选择不同的功能模式。
"""

import sys
import os
import argparse

# 将src目录添加到模块搜索路径
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

def parse_args():
    """解析命令行参数"""
    parser = argparse.ArgumentParser(description='骰子加解密系统')
    parser.add_argument('-g', '--gui', action='store_true', help='启动GUI界面')
    parser.add_argument('-f', '--file', action='store_true', help='文件加解密模式')
    parser.add_argument('-t', '--text', type=str, help='要加密的文本')
    parser.add_argument('-k', '--key', type=str, help='密钥(格式: "UP FRONT")')
    parser.add_argument('-e', '--encrypt', action='store_true', help='加密模式')
    parser.add_argument('-d', '--decrypt', action='store_true', help='解密模式')
    
    return parser.parse_args()

def main():
    """主函数"""
    args = parse_args()
    
    if args.gui or len(sys.argv) == 1:
        # 导入GUI模块并启动
        from src.加解密 import MainWindow, QApplication
        app = QApplication(sys.argv)
        window = MainWindow()
        window.show()
        sys.exit(app.exec_())
    
    elif args.file:
        # 导入文件加解密模块
        print("启动文件加解密模式...")
        from src.加解密文件 import process_file
        # 这里需要修改加解密文件.py来支持函数调用
        # process_file(args.encrypt, args.decrypt, args.key)
        
        # 临时解决方案
        import subprocess
        subprocess.call(["python", os.path.join("src", "加解密文件.py")])
    
    elif args.text:
        # 文本加解密
        if args.encrypt and args.key:
            from src.f_c import chinese2pinyin, chinese_punctuation_to_ascii
            # 这里需要实现文本加密函数
            text = chinese_punctuation_to_ascii(args.text)
            pinyin_text = chinese2pinyin(text)
            print(f"原文: {args.text}")
            print(f"拼音转换: {pinyin_text}")
            print("请使用GUI界面进行加密操作")
        
        elif args.decrypt and args.key:
            # 这里需要实现文本解密函数
            print("请使用GUI界面进行解密操作")
        
        else:
            print("错误: 请指定加密(-e)或解密(-d)模式，并提供密钥(-k)")
    
    else:
        print("请指定操作模式。使用 -h 或 --help 查看帮助信息。")

if __name__ == "__main__":
    main() 