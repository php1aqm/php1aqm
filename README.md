# 骰子加解密系统

基于骰子方向和位移算法的加解密系统，可以加密中文和英文文本。

![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)
![Python](https://img.shields.io/badge/Python-3.6+-green.svg)
![License](https://img.shields.io/badge/license-MIT-yellow.svg)

## 项目介绍

这个项目实现了一种基于骰子状态变换的加密算法，通过骰子的不同朝向来生成密钥，并使用向量叉乘等数学运算来实现加密和解密过程。系统支持中文汉字（通过拼音转换）和ASCII字符的加解密。骰子的六个面在空间中的不同朝向构成了复杂的密钥空间，使加密过程具有较高的安全性。

## 功能特点

- 支持中文文本加解密（通过拼音转换）
- 支持文件加解密
- 自动生成随机密钥
- 图形用户界面操作
- 支持密钥导入导出
- 独特的基于骰子状态的密钥生成机制
- 双向验证的解密过程

## 快速开始

### 安装

```bash
# 克隆仓库
git clone https://github.com/php1aqm/php1aqm.git
cd php1aqm

# 安装依赖
pip install -r requirements.txt
```

### 运行

```bash
# 启动图形界面
python main.py

# 或使用命令行模式
python main.py -t "要加密的文本" -k "2 3" -e
```

详细使用方法请参考 [使用文档](docs/usage.md)。

## 项目结构

```
.
├── docs/                # 文档目录
│   └── usage.md         # 详细使用说明
├── examples/            # 示例文件目录
│   ├── 1.txt            # 示例输入文件
│   ├── ciphertext.txt   # 加密结果
│   ├── pinyin_text.txt  # 拼音转换结果
│   └── ...              # 其他处理结果
├── images/              # 图片资源
├── src/                 # 源代码
│   ├── f_c.py           # 核心函数库
│   ├── 加解密.py         # 主程序(GUI)
│   ├── jiajiemi.py      # GUI界面定义
│   ├── jiajiemi.ui      # GUI界面设计
│   └── 加解密文件.py      # 文件加解密
├── tests/               # 测试代码
│   ├── test_encryption.py  # 单元测试
│   └── ...              # 其他测试工具
├── .gitignore           # Git忽略文件
├── main.py              # 主入口
├── README.md            # 项目说明
├── README_EN.md         # 英文说明
└── requirements.txt     # 依赖列表
```

## 技术原理

本加密系统使用了以下关键技术：

1. 骰子状态表示：使用三维向量表示骰子的六个面
2. 向量运算：通过叉乘等数学运算实现状态转换
3. 中文处理：使用pypinyin将中文转换为拼音进行处理
4. 字符位移：使用可打印ASCII字符集进行位移加密
5. 状态链：每个字符的加密状态会影响下一个字符的加密密钥

### 算法流程

1. 初始化骰子状态（UP和FRONT面）
2. 将输入文本转换为ASCII或拼音表示
3. 对每个字符：
   - 根据字符生成骰子旋转序列
   - 计算新的骰子状态
   - 使用新状态作为位移密钥进行字符加密
   - 将新状态作为下一个字符的初始状态
4. 生成密文和最终密钥

## 安装指南

### 环境要求
- Python 3.6+
- Windows/Linux/macOS

### 安装依赖

```bash
pip install -r requirements.txt
```

## 使用说明

### 图形界面

启动图形界面：

```bash
python main.py
```

#### 文本加密

1. 在左上文本框输入要加密的文本
2. 点击"生成密钥"按钮获取随机密钥
3. 点击"加密"按钮进行加密
4. 加密后的文本会显示在左下文本框
5. 请务必记录密钥信息，解密时需要使用

#### 文本解密

1. 在右上文本框输入要解密的文本
2. 输入完整的四位密钥（格式为：`初始UP值 初始FRONT值 加密后UP值 加密后FRONT值`）
3. 点击"解密"按钮进行解密
4. 解密后的文本会显示在右下文本框

### 命令行使用

```bash
# 查看帮助
python main.py -h

# 文件加解密
python main.py -f

# 文本加密
python main.py -t "你好，世界" -k "2 3" -e
```

## 开发

### 运行测试

```bash
python -m unittest discover -s tests
```

### 构建文档

```bash
# 如果有更多文档需求，可以考虑使用Sphinx等工具
```

## 贡献指南

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/amazing-feature`)
3. 提交更改 (`git commit -m 'Add some amazing feature'`)
4. 推送到分支 (`git push origin feature/amazing-feature`)
5. 创建 Pull Request

## 许可协议

MIT

## 贡献者

- php1aqm

## 更新日志

### v1.0.0 (2025-04-19)
- 初始版本发布
- 实现基本加解密功能
- 添加GUI界面
