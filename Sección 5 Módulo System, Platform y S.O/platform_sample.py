import locale
import platform
import sys

system = platform.system()
print(system)

version = platform.version()
print(version)
print(platform.python_version())
print(platform.machine())
print(platform.uname())
print(platform.processor())
print(sys.version)
print(locale.getlocale())
print(locale.getencoding())