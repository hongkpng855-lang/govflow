import re

path = "C:\\Users\\hongk\\.hermes\\config.yaml"
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix the broken YAML - replace literal \n with actual newlines
content = content.replace('\\n ', '\n')
content = content.replace('\\n', '\n')
content = content.replace('\\r', '\r')

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed!")
# Show what it looks like now
with open(path, 'r') as f:
    print(f.read()[:500])
