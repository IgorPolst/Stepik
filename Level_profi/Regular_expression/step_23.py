import re
import sys

code = sys.stdin.read()

code = re.sub(r'^\s*("{3}|\'{3})[^"\'\\]*\1\s*$', '', code, flags=re.MULTILINE)
code = re.sub(r'^\s*#.*$', '', code, flags=re.MULTILINE)
code = re.sub(r'  # .*$', '', code, flags=re.MULTILINE)
lines = [line.rstrip() for line in code.splitlines() if line.strip()]

print('\n'.join(lines))