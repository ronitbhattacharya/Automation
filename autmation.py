import PyPDF2
import nltk
 
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')
nltk.download('stopwords')
nltk.download('universal_tagset')
nltk.download('wordnet')
nltk.download('brown')

import docx

def getText(filename):
    doc = docx.Document(filename)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)
 
def func(name):
    # creating a pdf file object
    file_tup = os.path.splitext(name)
    import textract 
    txt=textract.process(name).decode('UTF-8')
    # print(type(txt))
    # print(txt)
    # if file_tup[1]==".docx" or file_tup[1]=='.doc':
    #     txt = getText(name)
    # elif file_tup[1]==".pdf":
    #     # pdfFileObj = open(name, 'rb')
        
    #     # # creating a pdf reader object
    #     # pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        
    #     # # printing number of pages in pdf file
    #     # print(pdfReader.numPages)
        
    #     # # creating a page object
    #     # pageObj = pdfReader.getPage(0)
    #     # print(pageObj)
        
    #     # # def extract_names(txt):
    #     # #     person_names = []
        
    #     # #     for sent in nltk.sent_tokenize(txt):
    #     # #         for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent))):
    #     # #             if hasattr(chunk, 'label') and chunk.label() == 'PERSON':
    #     # #                 person_names.append(
    #     # #                     ' '.join(chunk_leave[0] for chunk_leave in chunk.leaves())
    #     # #                 )
        
    #     # #     return person_names
    #     # # extracting text from page
    #     # # print(pageObj.extractText())
    #     # txt = pageObj.extractText()
    #     # # names = extract_names(txt)
    #     # # print(names)
    #     # print(txt)
    #     # # closing the pdf file object
    #     # pdfFileObj.close()
    #     import pdfplumber
    #     with pdfplumber.open(name) as pdf:
    #         first_page = pdf.pages[0]
    #         txt = first_page.extract_text()
    # else:
    #     return 0


    # from resume_parser import resumeparse

    # data = resumeparse.read_file(name)
    # print(data)


    import json
    from ibm_watson import NaturalLanguageUnderstandingV1
    from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
    from ibm_watson.natural_language_understanding_v1 import Features, KeywordsOptions,ConceptsOptions, SentimentOptions

    authenticator = IAMAuthenticator('U4PWE8XMkC9auSlzld_TKKvj6j-S4TUzUsT7Fn9KVk-y')
    natural_language_understanding = NaturalLanguageUnderstandingV1(
        version='2021-08-01',
        authenticator=authenticator
    )

    natural_language_understanding.set_service_url('https://api.eu-gb.natural-language-understanding.watson.cloud.ibm.com/instances/ad77242e-066d-49a5-9d5c-641bacf78632')

    response = natural_language_understanding.analyze(
        text=txt,
        features=Features(concepts=ConceptsOptions(limit=5))).get_result()
    # print(type(response))
    count=0
    sum=0
    for t in response['concepts']:
        count+=1
        sum+=t['relevance']
    if count>0: 
        sum/=count
    # print(json.dumps(response, indent=2))
    return sum
    # import OS module
import os

# Get the list of all files and directories
# path = "./HR_Interview"
# dir_list = os.listdir(path)

# for files in dir_list:
#     print(path+'/'+files)
#     print(func(path+'/'+files))
# print("\n\nRejected list\n\n")
path = "./Screen_Reject"
dir_list = os.listdir(path)
for files in dir_list:
    print(path+'/'+files)
    print(func(path+'/'+files))
# prints all files
print(dir_list)
