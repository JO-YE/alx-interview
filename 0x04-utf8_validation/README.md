# 0x04-utf8_validation
- This repository contains a Python script that implements a method to validate whether a given data set represents a valid UTF-8 encoding. The script checks if a list of integers (representing bytes) follows the UTF-8 encoding rules for characters.

## Method: validUTF8
The validUTF8 method is used to validate the data set. It takes a list of integers as input and returns True if the data is a valid UTF-8 encoding, and False otherwise.

## UTF-8 Encoding Rules
The UTF-8 encoding scheme allows characters to be represented using 1 to 4 bytes. The encoding follows specific rules:

- Single-byte characters (ASCII): Start with 0b0, such as 0b01000001 (65 in decimal) for 'A'.
- Two-byte characters: Start with 0b110, followed by 0b10xxxxxx.
- Three-byte characters: Start with 0b1110, followed by two bytes in the form 0b10xxxxxx.
- Four-byte characters: Start with 0b11110, followed by three bytes in the form 0b10xxxxxx.
***Any continuation byte should start with 0b10xxxxxx***

## Resources
- [UTF-8](https://en.wikipedia.org/wiki/UTF-8)
- [Characters, Symbols, and the Unicode Miracle](https://www.youtube.com/watch?v=MijmeoH9LT4)





