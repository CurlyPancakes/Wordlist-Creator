# Wordlist-Creator

[![Build Status](https://img.shields.io/github/stars/Zero-Developing/Wordlist-Creator.svg)](https://github.com/Zero-Developing/Wordlist-Creator)
[![Build Status](https://img.shields.io/github/forks/Zero-Developing/Wordlist-Creator)](https://github.com/Zero-Developing/Wordlist-Creator)
[![License: CC](https://img.shields.io/github/license/Zero-Developing/Wordlist-Creator)](https://github.com/Zero-Developing/Wordlist-Creator)

## Information
Wordlist-Creator is an python based script, which is currently under developing. There is no extra GUI at the moment.

## Getting Started
- [Documentation](doc.md)

### Installation
```
git clone https://github.com/Zero-Developing/Wordlist-Creator
pip install pyfiglet
```

### Usage
```
cd Wordlist-Creator
```
#### Version 1(Fast way)
```
python create.py --min MIN_LENGTH --max MAX_LENGTH
```
You can even use only one parameter.
```
python create.py --max MAX_LENGTH
```
#### Version 2(Slow way)
```
python create.py
```

### Example
So let's test it out. We will generate a wordlist from [Infos.txt](infos.txt). The output will be stored in the [wordlist.txt](wordlist.txt).\
**Input->** [Infos.txt](infos.txt)
```
python create.py --min 1 --max 3
```
**Output->** [Wordlist.txt](wordlist.txt)


## Bugs
Depending on the console, bugs can occur with the output.

## Disclaimer
The software is provided for educational purposes only. See the **[License](LICENSE)** for more information.
