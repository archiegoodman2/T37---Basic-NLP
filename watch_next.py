
import spacy 

description = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trainer as a gladiator."
#this is for the given example: Planet Hulk 

def up_next(description):
    f = open('movies.txt', 'r')

    contents = ""

    for line in f:
        contents += line   #now we have a string full of our file contents

    #we want to split it into a list of each line:

    lines = contents.split("\n")

    #so the idea is, we want to find the element of this list that returns the greatest similarity value
    #when compared to our input description, which is in this case, the example given.
    nlp = spacy.load('en_core_web_md')
    #start by loading our language model
    nlp_description = nlp(description) #this will help us later.

    list_of_NLPs = []

    for i in range(0, len(lines)): 
        list_of_NLPs.append(nlp(lines[i]))

    #so now we can simply use the similarity method included in the spacy module to compare.

    list_of_similarities = []   #define a list of all of our similarity values
    for i in range(0, len(list_of_NLPs)):
        value = float(list_of_NLPs[i].similarity(nlp_description))    #this spits out our similarity values
        list_of_similarities.append(value)

    most_similiar_index = list_of_similarities.index(max(list_of_similarities))   #this simply gives us the index of the line that best matched our description
    
    #now we have found the index at which our best matched description can be found, we simply print out that line of the contents.

    matched_movie = lines[most_similiar_index]   #this is a string containing the name and description of the best matched movie

    print(f'''The movie that best matched the given movie was {matched_movie} ''')
    f.close()

up_next(description)