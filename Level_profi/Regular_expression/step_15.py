import sys, re
html = sys.stdin.read()

pattern = r'<a\s+[^>]*href\s*=\s*"([^"]*)"[^>]*>(.*?)</a>'

matches = re.findall(pattern, html, re.DOTALL | re.IGNORECASE)

for href, content in matches:
    content_clean = re.sub(r'\s+', ' ', content).strip()
    print(f"{href}, {content_clean}")