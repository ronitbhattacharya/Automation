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