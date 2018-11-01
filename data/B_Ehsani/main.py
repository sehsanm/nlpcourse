from hazm import Normalizer
from functions import handle_ha, handle_mi, step1_tokenize, sentences
import sys


file_name = sys.argv[1]
f_in = open(file_name,"r",encoding="utf8")
text = f_in.read()
f_in.close()
#preprocessing
# text = re.sub
# text = text.replace("ٔ","‌ی") # حذف کاراکتر همزه 
normalizer = Normalizer()
normalized_text = normalizer.normalize(text)
stuff = [u"هایی", u"هایم",u"هایش",u"هایت",u"هایشان",u"هایتان",u"هایمان"]
for thing in stuff:
    normalized_text = normalized_text.replace(u" " + thing,u"‌" + thing)
token_and_tags = step1_tokenize(normalized_text)
tokenized_text = [item[0] for item in token_and_tags]
fixed_tokenized_text= []
tmp = ""

for token in tokenized_text:
    tmp = handle_ha(tokenized_text,token)
    tmp = handle_mi(tokenized_text,tmp)
    fixed_tokenized_text.append(tmp)
    tmp = ""

for i in range(len(fixed_tokenized_text)):
    if fixed_tokenized_text[i] != tokenized_text[i]:
        token_and_tags[i][0] = fixed_tokenized_text[i]



text_sentences_positions = sentences(token_and_tags)
index = 0
output_file_name = file_name [:-3] + "out"
with open(output_file_name, 'w+') as f1_out:
    for i in range(len(token_and_tags)):
        line = str(index) + "\t" + token_and_tags[i][0] + "\t" + "-" + "\t" + "-" + "\t" + "-" + "\t" + "\n" 
        if i in  text_sentences_positions:
            index = 0
        else:
            index += 1
        f1_out.write(line)
