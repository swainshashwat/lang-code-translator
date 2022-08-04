import re
import json

class RegexAdapter:
    def __init__(self):
        self.valid_token_types = ['keyword', 'variable']
        self.valid_languages = ['en', 'hi', 'or']
        
        with open('lang.json', 'r') as f:
            self.lang_lookup = json.load(f)

    def _return_valid_token_types(self):
        return self.valid_token_types
    
    def get_regex(self, lang, token_type):
        if lang not in self.languages:
            raise ValueError("Invalid language code: "+lang)
        if token_type not in self.valid_token_types:
            raise ValueError("Invalid token_type: "+token_type)
        


        regex = {
            "if": re.compile("(\W("")[\( ]{1})"),
            "elif": re.compile("(\W(elif)[\( ]{1})"),
            "else": re.compile("(\W(else)[ ]*[:]{1})")
        }

    