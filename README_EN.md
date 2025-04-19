# Dice Encryption System

An encryption system based on dice orientation and displacement algorithms, capable of encrypting both Chinese and English text.

![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)
![Python](https://img.shields.io/badge/Python-3.6+-green.svg)
![License](https://img.shields.io/badge/license-MIT-yellow.svg)

## Introduction

This project implements an encryption algorithm based on dice state transitions, using different orientations of dice to generate keys and vector cross products for encryption and decryption processes. The system supports encryption of Chinese characters (through pinyin conversion) and ASCII characters. The six faces of a die in different spatial orientations form a complex key space, making the encryption process highly secure.

## Features

- Support for Chinese text encryption (through pinyin conversion)
- File encryption and decryption
- Automatic random key generation
- Graphical user interface
- Key import and export
- Unique dice state-based key generation mechanism
- Two-way verification for decryption

## Quick Start

### Installation

```bash
# Clone repository
git clone https://github.com/php1aqm/php1aqm.git
cd php1aqm

# Install dependencies
pip install -r requirements.txt
```

### Running

```bash
# Launch the graphical interface
python main.py

# Or use command-line mode
python main.py -t "Text to encrypt" -k "2 3" -e
```

For detailed usage instructions, please refer to the [usage documentation](docs/usage.md).

## Project Structure

```
.
├── docs/                # Documentation
│   └── usage.md         # Detailed usage instructions
├── examples/            # Example files directory
│   ├── 1.txt            # Sample input file
│   ├── ciphertext.txt   # Encryption results
│   ├── pinyin_text.txt  # Pinyin conversion results
│   └── ...              # Other processing results
├── images/              # Image resources
├── src/                 # Source code
│   ├── f_c.py           # Core function library
│   ├── 加解密.py         # Main program (GUI)
│   ├── jiajiemi.py      # GUI definition
│   ├── jiajiemi.ui      # GUI design
│   └── 加解密文件.py      # File encryption/decryption
├── tests/               # Test code
│   ├── test_encryption.py  # Unit tests
│   └── ...              # Other testing tools
├── .gitignore           # Git ignore file
├── main.py              # Main entry point
├── README.md            # Project description (Chinese)
├── README_EN.md         # Project description (English)
└── requirements.txt     # Dependencies
```

## Technical Principles

This encryption system uses the following key technologies:

1. Dice state representation: Using three-dimensional vectors to represent the six faces of a die
2. Vector operations: State transitions through cross products and other mathematical operations
3. Chinese text processing: Using pypinyin to convert Chinese to pinyin
4. Character displacement: Using printable ASCII character sets for displacement encryption
5. State chain: The encryption state of each character affects the encryption key of the next character

### Algorithm Flow

1. Initialize dice state (UP and FRONT faces)
2. Convert input text to ASCII or pinyin representation
3. For each character:
   - Generate dice rotation sequence based on the character
   - Calculate new dice state
   - Use new state as displacement key for character encryption
   - Use new state as initial state for the next character
4. Generate ciphertext and final key

## Installation Guide

### Requirements
- Python 3.6+
- Windows/Linux/macOS

### Installing Dependencies

```bash
pip install -r requirements.txt
```

## Usage Instructions

### Graphical Interface

Launch the graphical interface:

```bash
python main.py
```

#### Text Encryption

1. Enter the text to encrypt in the top-left text box
2. Click the "Generate Key" button to get a random key
3. Click the "Encrypt" button to perform encryption
4. The encrypted text will be displayed in the bottom-left text box
5. Be sure to record the key information, which is needed for decryption

#### Text Decryption

1. Enter the text to decrypt in the top-right text box
2. Enter the complete four-digit key (format: `Initial UP value Initial FRONT value Post-encryption UP value Post-encryption FRONT value`)
3. Click the "Decrypt" button to perform decryption
4. The decrypted text will be displayed in the bottom-right text box

### Command Line Usage

```bash
# View help
python main.py -h

# File encryption/decryption
python main.py -f

# Text encryption
python main.py -t "Hello, World" -k "2 3" -e
```

## Development

### Running Tests

```bash
python -m unittest discover -s tests
```

### Building Documentation

```bash
# If more documentation needs arise, consider using tools like Sphinx
```

## Contribution Guidelines

1. Fork this repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Create a Pull Request

## License

MIT

## Contributors

- php1aqm

## Changelog

### v1.0.0 (2025-04-19)
- Initial release
- Implemented basic encryption and decryption functionality
- Added GUI interface 