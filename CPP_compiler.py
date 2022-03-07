import os, re, readline
print("Recommended: Save this file in the same directory where you save all you C++ files (.cpp)\n")
COMMANDS = [x for x, y in zip(os.listdir(),[i.endswith(".cpp") for i in os.listdir()]) if y == True]
RE_SPACE = re.compile('.*\s+$', re.M)

for i in COMMANDS:
    print(i)
print()

class Completer(object):
    def _listdir(self, root):
        "List directory 'root' appending the path separator to subdirs."
        res = []
        for name in os.listdir(root):
            path = os.path.join(root, name)
            if os.path.isdir(path):
                name += os.sep
            res.append(name)
        return res

    def _complete_path(self, path=None):
        "Perform completion of filesystem path."
        if not path:
            return self._listdir('.')
        dirname, rest = os.path.split(path)
        tmp = dirname if dirname else '.'
        res = [os.path.join(dirname, p)
                for p in self._listdir(tmp) if p.startswith(rest)]
        # more than one match, or single match which does not exist (typo)
        if len(res) > 1 or not os.path.exists(path):
            return res
        # resolved to a single directory, so return list of files below it
        if os.path.isdir(path):
            return [os.path.join(path, p) for p in self._listdir(path)]
        # exact file match terminates this completion
        return [path + ' ']

    def complete_extra(self, args):
        "Completions for the 'extra' command."
        if not args:
            return self._complete_path('.')
        # treat the last arg as a path and complete it
        return self._complete_path(args[-1])

    def complete(self, text, state):
        "Generic readline completion entry point."
        buffer = readline.get_line_buffer()
        line = readline.get_line_buffer().split()
        # show all commands
        if not line:
            return [c + ' ' for c in COMMANDS][state]
        # account for last argument ending in a space
        if RE_SPACE.match(buffer):
            line.append('')
        # resolve command to the implementation function
        cmd = line[0].strip()
        if cmd in COMMANDS:
            impl = getattr(self, 'complete_%s' % cmd)
            args = line[1:]
            if args:
                return (impl(args) + [None])[state]
            return [cmd + ' '][state]
        results = [c + ' ' for c in COMMANDS if c.startswith(cmd)] + [None]
        return results[state]

comp = Completer()
# we want to treat '/' as part of a word, so override the delimiters
readline.set_completer_delims(' \t\n;')
readline.parse_and_bind("tab: complete")
readline.set_completer(comp.complete)

##################################################################################################################

filename = input('Enter file: ').strip()
if filename not in COMMANDS:
    print("FileNotFound: Please check the filename and classname (if any) of your file...")
    input("\n\n<< Press ENTER to exit >>\n")
    exit()
from time import sleep
try:
    os.remove("a.exe")
except:
    pass
os.system("cd \"" + os.getcwd() + "\"")
print("Compiling... Please wait")
os.system(f"g++ \"{filename}\"")
sleep(2.5)
print("\nOUTPUT\n>>> ", end = '')
if os.path.isfile("a.exe"):
    os.system('a.exe')
input("\n\n<< Press ENTER to exit >>\n")
