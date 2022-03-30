import stanza
# stanza.download("zh")
nlp = stanza.Pipeline("zh", processors="tokenize,pos,ner")
a = nlp("车载用具，请提干净整洁箱子")

print(a)