import re
text = open("hindi_file.txt",encoding= 'utf-8').read()
#This converts the encoded text to an internal unicode object, where
# all characters are properly recognized as an entity:
words = re.split(r'\s+', re.sub(r'[,/\-!?.|lI।"\]\[<>br]', ' ', text).strip())
print(words)
text = ' '.join(words)
fh = open("hindi.txt","w", encoding='utf-8').write(text)
