![Dirscovery](docs/dir-icon.png)

Dirscovery is a simple directory discoverer that uses dictionaries to find folders or files on a website.

Features:
* Find hidden folders in web servers
* Search by extension

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. Follow them carefully. If you have any questions feel free to ask!

## Installing
First, clone or download the repository to your local machine.
Next, make sure you have these dependencies installed (**remember, this is Python 2!**):

```
requests Library
termcolor Library
```
You can install libraries using Pip (again, for Python 2).
## Checking
Now check if you have all dependencies installed and that the script works.
Execute this in your console/terminal:
```
python dirscovery.py
```
Make sure to be in the same folder where the script is.
If you get a "usage" message it means that it is up and working.

# Running
Usage:
```
python dirsovery.py [url] [wordlist] [extensions]
```
Example:
```
python dirscovery.py http://example.com /home/wordlist/words.txt .html,.php
```
You can use the "-h" option for more help.

# Licence
