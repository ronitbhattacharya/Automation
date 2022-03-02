#!/usr/bin/env python
# coding: utf-8

# In[62]:


import PyPDF2
import nltk
 
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')
 
 
# creating a pdf file object
pdfFileObj = open('Ankur sir Interview._transcript.mp3-converted.pdf', 'rb')
 
# creating a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
 
# printing number of pages in pdf file
print(pdfReader.numPages)
 
# creating a page object
pageObj = pdfReader.getPage(0)
 
def extract_names(txt):
    person_names = []
 
    for sent in nltk.sent_tokenize(txt):
        for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent))):
            if hasattr(chunk, 'label') and chunk.label() == 'PERSON':
                person_names.append(
                    ' '.join(chunk_leave[0] for chunk_leave in chunk.leaves())
                )
 
    return person_names
# extracting text from page
print(pageObj.extractText())
txt = pageObj.extractText()
names = extract_names(txt)
print(names)
 
# closing the pdf file object
pdfFileObj.close()


# In[9]:


import json
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 import Features, KeywordsOptions,ConceptsOptions

authenticator = IAMAuthenticator('U4PWE8XMkC9auSlzld_TKKvj6j-S4TUzUsT7Fn9KVk-y')
natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2021-08-01',
    authenticator=authenticator
)

natural_language_understanding.set_service_url('https://api.eu-gb.natural-language-understanding.watson.cloud.ibm.com/instances/ad77242e-066d-49a5-9d5c-641bacf78632')

response = natural_language_understanding.analyze(
    text=txt,
    features=Features(concepts=ConceptsOptions(limit=3))).get_result()

print(json.dumps(response, indent=2))


# In[12]:


get_ipython().system('pip install docx2txt')


# In[14]:


import docx2txt


# In[63]:


txt= docx2txt.process("Ankur sir Interview._transcript.mp3.docx")


# In[58]:


print(txt)


# In[60]:


def extract_names(txt):
    person_names = []
 
    for sent in nltk.sent_tokenize(txt):
        for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent))):
            if hasattr(chunk, 'label') and chunk.label() == 'PERSON':
                person_names.append(
                    ' '.join(chunk_leave[0] for chunk_leave in chunk.leaves())
                )
 
    return person_names


# In[61]:


names = extract_names(txt)
print(names)


# In[71]:


import json
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 import Features, KeywordsOptions,ConceptsOptions,EntitiesOptions

authenticator = IAMAuthenticator('U4PWE8XMkC9auSlzld_TKKvj6j-S4TUzUsT7Fn9KVk-y')
natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2021-08-01',
    authenticator=authenticator
)

natural_language_understanding.set_service_url('https://api.eu-gb.natural-language-understanding.watson.cloud.ibm.com/instances/ad77242e-066d-49a5-9d5c-641bacf78632')

response = natural_language_understanding.analyze(
    text=txt,
    features=Features(entities=EntitiesOptions(sentiment=True,limit=2))).get_result()

print(json.dumps(response, indent=2))


# In[26]:


job_description = docx2txt.process("JD-CS Agent.docx")


# In[27]:


print(job_description)


# In[54]:


text=[cv,job_description]


# In[55]:


from sklearn.feature_extraction.text import CountVectorizer
cv=CountVectorizer()
count_matrix = cv.fit_transform(text)


# In[56]:


from sklearn.metrics.pairwise import cosine_similarity
print("\nSimilarity Scores:")
print(cosine_similarity(count_matrix))

