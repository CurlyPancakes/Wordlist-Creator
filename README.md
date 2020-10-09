# Wordlist-Creator

[![Build Status](https://img.shields.io/github/stars/Zero-Developing/Wordlist-Creator.svg)](https://github.com/Zero-Developing/Wordlist-Creator)
[![Build Status](https://img.shields.io/github/forks/Zero-Developing/Wordlist-Creator)](https://github.com/Zero-Developing/Wordlist-Creator)
[![License: CC](https://img.shields.io/github/license/Zero-Developing/Wordlist-Creator)](https://github.com/Zero-Developing/Wordlist-Creator)

## Information
Wordlist-Creator is an python based script, which is currently under developing. The software is working with multi-threading. There is no extra GUI at the moment. You can find the error documentation in our [documentation](doc.md).

## Getting Started
- [Documentation](doc.md)

### Installation
```bash
git clone https://github.com/Zero-Developing/Wordlist-Creator
pip install pyfiglet
cd Wordlist-Creator
```

### Usage

#### Version 1(Fast way)
```bash
python start.py --min MIN_AMOUNT --max MAX_AMOUNT
```
You can even use only one parameter.
```bash
python start.py --max MAX_AMOUNT
```
#### Version 2(Slow way)
```bash
python start.py
```

### Example
So let's test it out. We will generate a wordlist from [Infos.txt](infos.txt). The output will be stored in the [Wordlist.txt](wordlist.txt).\
**Input->** [Infos.txt](infos.txt)
```bash
python start.py --min 1 --max 3
```
**Output->** [Wordlist.txt](wordlist.txt)


## Bugs
Depending on the console, bugs can occur with the output.

If you have problems with the program. Try executing it in other terminals like Powershell.

## Disclaimer
The software is provided for educational purposes only. See the **[License](LICENSE)** for more information.
