from __future__ import with_statement
from __future__ import absolute_import
from termcolor import colored
import os
import requests
import sys
import errno
from io import open

try:
    helped = 0
    first = sys.argv[1]
    first = first.replace(" ", "")
    if first == "-h" or first == "--help":
        helped = 1
        print "[] Usage: python dirscovery [url] [wordlist] [extensions]\n    [-h] or [--help] - Display this help menu"
        print "    [url]            - Valid url: http://www.example.com\n    [wordlist]       - Directory to wordlist (txt): /root/example.txt"
        print "    [extensions]     - File extensions to look for (optional): .html,.php,...\n[] Example usage: python dirscovery.py http://www.example.com /root/words.txt .html,.png\n"
        print "[] TIP: Use no extensions to ping directories"
    else:
        allurl = [first]
        if "https://" in allurl[0]:
            allurl[0] = allurl[0][8:]
            allurl.insert(0, "http://")
        elif "http://" in allurl[0]:
            allurl = allurl
        else:
            allurl.insert(0, "http://")
        url = ''.join(allurl)
    path = sys.argv[2]
    path = path.replace(" ", "")
except:
    if helped == 0:
        print "[] Usage: python dirscovery.py [url] [wordlist] [extensions]\n[] Execute \'python dirscovery -h\' for more details"
        exit()
    else:
        exit()
try:
    extensions = sys.argv[3]
    extensions = extensions.split(',')
    for i in extensions:
        if "." not in i:
            extensions.remove(i)
    extensions = list(set(extensions))
except:
    extensions = "none"

print
print colored("  ____  _  ____  ____  ____  ____  _  _  _____ ____ ___  _", "red", attrs=['bold'])
print colored(" /  _ \/ \/  __\/ ___\/   _\/  _ \/ \ |\/  __//  __\\\  \//", "red", attrs=['bold'])
print colored(" | | \|| ||  \/||    \|  /  | / \|| | //|  \  |  \/| \  / ", "red", attrs=['bold'])
print colored(" | |_/|| ||    /\___ ||  \__| \_/|| \// |  /_ |    / / /  ", "red", attrs=['bold'])
print colored(" \____/\_/\_/\_\\\____/\____/\____/\__/  \____\\\_/\_\/_/   ", "red", attrs=['bold'])
print
print colored("[--]", "yellow"), colored("         \'A Simple Directory Discoverer\'        ", "magenta", attrs=['bold']), colored("[--]", "yellow")
print colored("[--]", "yellow") + colored("          Created by:", "blue") + colored(u" Mikicat & Marti157       ", "green") + colored("   ", "blue") + colored("[--]", "yellow")
print colored("                       Version ", "blue") + colored(" 1.2", "green")
print

print "{} Host: " + url
print "{} Wordlist: " + path

if extensions != '':
    print "{} Extensions: " + ''.join(extensions)

print "\n  Starting Dirscovery...\n"

try:
    with open(path, "r") as f:
        matches = 0
        lines = f.readlines()
        r = requests.get(url)
        if (r.status_code) != 200:
            print "  [] Cannot connect to webpage."
            exit()
        else:
            for line in lines:
                line = line.lstrip().rstrip()
                full_url = [url, line]
                if url.endswith('/') or line.startswith('/'):
                    full_url = ''.join(full_url)
                else:
                    full_url = '/'.join(full_url)
                without_ext = full_url
                if extensions == "none":
                    req = requests.get(without_ext)
                    if (req.status_code) == 200:
                        matches = matches + 1
                        print "   [] Match Found: " + without_ext
                else:
                    for i in xrange(0, len(extensions)):
                        full_url = without_ext
                        full_url = full_url + extensions[i]
                        req = requests.get(full_url)
                        if (req.status_code) == 200:
                            matches = matches + 1
                            print "   [] Match Found: " + full_url
                        else:
                            pass
    if matches != 0:
        print "\n   {} Total matches dirscovered: " + str(matches)
    else:
        print "\n   {} No matches dirscovered."
except KeyboardInterrupt:
    print "\nExiting..."
    exit()
except IOError:
    print "  [] Wordlist file not found or unknown url."
    print "  [] Use \"-h\" option for usage example."
    exit()
except:
    print "  [] Unknown error."