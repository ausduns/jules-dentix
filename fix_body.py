import sys

with open('index.html', 'r') as f:
    content = f.read()

# Make sure there is smooth scrolling behavior if we ever add ids to sections
content = content.replace('<html lang="en">', '<html lang="en" class="scroll-smooth">')

with open('index.html', 'w') as f:
    f.write(content)
