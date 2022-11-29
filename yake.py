
import yake
import json

language = "en"
max_ngram_size = 3
deduplication_threshold = 0.9
deduplication_algo = 'seqm'
windowSize = 1
numOfKeywords = 20


issues = []

with open('issues.json','r', encoding='utf-8') as f:
  issues = json.load(f)

issues_titles = [ issue['issue_data']['title'] for issue in issues ]


custom_kw_extractor = yake.KeywordExtractor(lan=language, n=max_ngram_size, dedupLim=deduplication_threshold, dedupFunc=deduplication_algo, windowsSize=windowSize, top=numOfKeywords, features=None)
keywords = custom_kw_extractor.extract_keywords(issues_titles)

for kw in keywords:
    print(kw)