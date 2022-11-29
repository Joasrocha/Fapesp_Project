import nltk 
nltk.download('stopwords')
nltk.download('punkt')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re
from string import digits
from os.path import splitext, basename
from re import search

issue_body = "```\nSep 03, 2015 4:25:30 PM java.util.prefs.WindowsPreferences <init>\nWARNUNG: Could not open/create prefs root node Software\\JavaSoft\\Prefs at root 0x80000002. Windows RegCreateKeyEx(...) returned error code 5.\n```\n\nHaven't evaluated yet what consequences this has...\n"

#conversão em letra minúscula
issue_body = issue_body.lower()

#remoção de links
issue_body = re.sub(r'http\S+', '', issue_body)

#remoção de dígitos
remove_digits = str.maketrans('', '', digits)
issue_body = issue_body.translate(remove_digits)

print (issue_body)

#/////////////////////////////////////////////////////////////////////////////

#//////////////////////////////////////////////////////////////////////  


#remoção de stop_words  
stop_words = set(stopwords.words('english'))
  
word_tokens = word_tokenize(issue_body)
  
filtered_sentence = [w for w in word_tokens if not w.lower() in stop_words]
  
filtered_sentence = []
  
for w in word_tokens:
    if w not in stop_words:
        filtered_sentence.append(w)

#impressão final da string após a filtragem  
print(filtered_sentence)