import yaml

path = "C:\\Users\\hongk\\.hermes\\config.yaml"

with open(path, 'r', encoding='cp950', errors='replace') as f:
    content = f.read()

# Show the broken part
lines = content.split('\n')
for i, line in enumerate(lines[:15]):
    print(f"{i}: {repr(line)}")
