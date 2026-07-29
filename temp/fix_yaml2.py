import re

path = "C:\\Users\\hongk\\.hermes\\config.yaml"

with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Remove blank lines between YAML keys in the model section
# Fix indentation: single space -> 2 spaces
content = re.sub(r'\n\n+', '\n', content)
content = re.sub(r'\n (\w)', r'\n  \1', content)

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

# Verify
with open(path, 'r') as f:
    for i, line in enumerate(f.readlines()[:15]):
        print(f"{i}: {repr(line)}")
