import re

with open('app/src/main/java/com/example/generator/VideoGenerator.kt', 'r') as f:
    content = f.read()

lines = content.split('\n')
for i in range(1385, 1420):
    if i < len(lines):
        print(f"{i+1}: {lines[i]}")

