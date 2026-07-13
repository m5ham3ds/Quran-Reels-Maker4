import re

with open('app/src/main/java/com/example/ui/VideoEditorScreen.kt', 'r') as f:
    content = f.read()

content = content.replace("(((arabicTextY - 140f)) * scalePx)", "(((arabicTextY - 70f)) * scalePx)")
content = content.replace("(((translationTextY - 200f)) * scalePx)", "(((translationTextY - 90f)) * scalePx)")
content = content.replace("((surahNameY + 40f) * scalePx)", "((surahNameY + 40f) * scalePx)")
content = content.replace("((iconY + 70f) * scalePx)", "((iconY + 70f) * scalePx)")

with open('app/src/main/java/com/example/ui/VideoEditorScreen.kt', 'w') as f:
    f.write(content)
