from dataclasses import replace
import re
import copy
from pathlib import Path
import json

class RegexAdapter:
    def __init__(self):
        self.LANG_PATH = Path(Path(__file__).parent.absolute(), "lang.json")
        self.valid_token_types = ['keywords', 'variables']
        self.valid_languages = ['en', 'hi']
        self.valid_keywords = ["if", "elif", "else", "print"] # words that are have tested regex and support in lang.json

        self._load_lang()
        self._load_regex()
        
        
    def _load_regex(self, lang='en'):
        '''
        Load regex compilers for the given language `lang`.
        '''
        self.regex = {
                "keywords": {
                    "if": re.compile("(?![\"|\'])(?:(?:\W)("+self.lang_lookup["keywords"]["if"][lang]+")[\( ]{1})(?![\"|\'])"),
                    "elif": re.compile("(?![\"|\'])(?:(?:\W)("+self.lang_lookup["keywords"]["elif"][lang]+")[\( ]{1})(?![\"|\'])"),
                    "else": re.compile("(?![\"|\'])(?:(?:\W)("+self.lang_lookup["keywords"]["else"][lang]+")[ ]*[:]{1})(?![\"|\'])"),

                    "print": re.compile("(?<![\" \'])(?:^| |	)*(?:("+self.lang_lookup["keywords"]["print"][lang]+")[\(]{1}[\"\'\w.])")
                },
                "variables": {}
            
        }

    def _load_lang(self):
        with open(self.LANG_PATH, 'r') as f:
            self.lang_lookup = json.load(f)

    def _return_valid_token_types(self):
        return self.valid_token_types
    
    def get_regex(self, lang, token_type):
        if lang not in self.valid_languages:
            raise ValueError("Invalid language code: "+lang)
        if token_type not in self.valid_token_types:
            raise ValueError("Invalid token_type: "+token_type)

        return self.regex[lang][token_type]

    def sub(self, pattern, repl, string):
        
        temp = []

        for line in string.split("\n"):
            regx_res = pattern.search(line)
            if regx_res==None:
                temp.append(line)
                continue
            
            temp.append(line[:regx_res.start()] + \
                 regx_res.group().replace(regx_res.group(1), repl) + \
                     line[regx_res.end():])
        
        return '\n'.join(temp)

    def replace_keyword(self, keyword, string, src_lang='en', target_lang='hi'):
        if keyword not in self.valid_keywords:
            raise ValueError("Invalid keyword code: "+keyword+".\
                 Use one of the following keywords which are valid: "\
                + str(self.valid_keywords))
        self._load_regex(src_lang) # loads self.regex for language `lang`

        return self.sub(self.regex["keywords"][keyword],
                self.lang_lookup["keywords"][keyword][target_lang],\
                string)

    def replace_all_keywords(self, string, src_lang='en', target_lang='hi'):
        for k in self.valid_keywords:
            string = self.replace_keyword(k, string, src_lang, target_lang)
        
        return string

        

    