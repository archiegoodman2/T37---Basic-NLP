import spacy
nlp = spacy.load('en_core_web_sm')

sentence1 = u'The old man the boat.'
sentence2 = u'While Tom was washing the dishes fell on the floor'
sentence3 = u'The horse raced past the barn fell.'
sentence4 = u'The cotton Nike clothing is made of grows in Mississippi.'
sentence5 = u'The sour drink from the Pacific.'

gardenpathSentences = [sentence1, sentence2, sentence3, sentence4, sentence5]

#so let's tokenise our sentences, excluding any whitespace or commas
#methods with an underscore as a suffix return strings, so this is what we want, 
#to make them human readable

nlp_sentence1 = nlp(sentence1)
nlp_sentence2 = nlp(sentence2)
nlp_sentence3 = nlp(sentence3)
nlp_sentence4 = nlp(sentence4)
nlp_sentence5 = nlp(sentence5)
sentences = [nlp_sentence1, nlp_sentence2, nlp_sentence3, nlp_sentence4, nlp_sentence5]

#defining a function to categorize each entity:

def show_ents(doc):
    if doc.ents:    #if it can find any suitable elements in the string to categorise
        for ent in doc.ents :
            print(ent.text+' - ' +str(ent.start_char) +' - '+ str(ent.end_char) +' - '+ent.label_+ ' - '+str(spacy.explain(ent.label_)))  #returns various pieces of info, formatted, about each one
    else:
        print("No named entities found.")

#CITATION + credit: https://towardsdatascience.com/named-entity-recognition-ner-using-spacy-nlp-part-4-28da2ece57c6
#This source is a basic guide on how to create a resuable function that utitlises various packages within spacy to output the category of words.

show_ents(nlp_sentence2)

for i in range(0, len(sentences)) :
    print(f'''
    For sentence {i+1} :''')
    show_ents(sentences[i])


#COMMENTS ON OUTPUTS:
#Spacy is only picking up proper nouns, essentially
#therefore it's not actually returning anything for sentences one and three: for example, if we named that horse it would pick it up
#because the Spacy literature defines an entity as a real world object with a name: mostly proper nouns.

#because of this, the fact that these are garden-path sentences is not actually relevant, as these focus on mistaking nouns for verbs,
#but we cannot distinguish between nouns/verbs with this