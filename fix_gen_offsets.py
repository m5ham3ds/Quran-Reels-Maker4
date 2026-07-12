import re

with open('app/src/main/java/com/example/generator/VideoGenerator.kt', 'r') as f:
    content = f.read()

content = content.replace("surahNameY.toFloat() * scaleRatio", "surahNameY.toFloat() * scaleRatio")
# Wait, for surah name, in generator it was 110f. If I changed UI offset from -70f to -40f, UI moved DOWN by 30f.
# If UI moves DOWN by 30f, Generator should move DOWN by 30f.
# Currently Generator Surah Name Y = 110f. Move DOWN by 30f = 140f.
content = content.replace("110f * scaleRatio + scaledSurahNameY", "140f * scaleRatio + scaledSurahNameY")

# Arabic Text
# In UI, it changed from -70f to -160f. Moved UP by 90f.
# In Generator, startY = baseStartY + (scaledArabicTextY - 70f * scaleRatio).
# I should change -70f to -160f to move it UP by 90f.
content = content.replace("scaledArabicTextY - 70f * scaleRatio", "scaledArabicTextY - 160f * scaleRatio")

# Background box in Generator: 
# Currently boxTop = baseStartY - 42f. If Arabic text moved UP by 90f, the box should move UP by 90f?
# Wait! In UI, the box is drawn by Column using padTop = 42f. The Column's top is `baseStartY`.
# In UI, the Arabic text moved UP by 90f RELATIVE TO THE COLUMN.
# But the box in UI did NOT move! The box in UI is still at `- 42f` from the top of the Column.
# So in Generator, `boxTop` should REMAIN AT `baseStartY - 42f`.
# BUT wait! If the text moves UP by 90f, and the box stays in place, the text will be drawn OUTSIDE the box!
# Let's check if the user actually wants the box to stay in place. "نسخ لصق"
# If the UI draws it outside the box, the generator will draw it outside the box.
# If they want the box to wrap the text, then moving the text means the box should move.
# But the UI doesn't move the box! Because the `offset` in UI is applied to the `Box` containing the Text, NOT the `Column` that draws the background!
# Is this correct? "نسخ لصق". Yes, if UI behaves this way, Generator MUST behave this way to match it perfectly.
# Wait, if the Translation text changed from -110f to -230f, it moved UP by 120f.
# So I should change -110f to -230f in Generator.
content = content.replace("scaledTranslationTextY - 110f * scaleRatio", "scaledTranslationTextY - 230f * scaleRatio")

# Icon
# In UI, changed from +50f to +120f. Moved DOWN by 70f.
# In Generator, `scaledIconY + 50f * scaleRatio + 95f * scaleRatio`.
# Change `50f` to `120f`.
content = content.replace("scaledIconY + 50f * scaleRatio + 95f * scaleRatio", "scaledIconY + 120f * scaleRatio + 95f * scaleRatio")

with open('app/src/main/java/com/example/generator/VideoGenerator.kt', 'w') as f:
    f.write(content)
