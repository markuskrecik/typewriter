

class Typewriter(object):

    def __init__(self):
        super().__init__()
        self.symbol_list = []
        self.symbol = r'{}'
        self.latex = r''
        self.mapping = {
'none': {
'32': r' ',
'39': r"'",
'44': r',',
'45': r'-',
'46': r'.',
'47': r'/',
'48': r'0',
'49': r'1',
'50': r'2',
'51': r'3',
'52': r'4',
'53': r'5',
'54': r'6',
'55': r'7',
'56': r'8',
'57': r'9',
'59': r';',
'61': r'=',
'65': r'a',
'66': r'b',
'67': r'c',
'68': r'd',
'69': r'e',
'70': r'f',
'71': r'g',
'72': r'h',
'73': r'i',
'74': r'j',
'75': r'k',
'76': r'l',
'77': r'm',
'78': r'n',
'79': r'o',
'80': r'p',
'81': r'q',
'82': r'r',
'83': r's',
'84': r't',
'85': r'u',
'86': r'v',
'87': r'w',
'88': r'x',
'89': r'y',
'90': r'z',
'91': r'[',
# '92': r'\\',
'93': r']',
# '96': r'`',
'167': r'§',
'16777217': r'\quad', # tab
'16777219': '', # backspace
'16777220': '', # enter
},
'16777251': {
'32': r' ',
'39': r"'",
'44': r',',
'45': r'-',
'46': r'.',
'47': r'/',
'48': r'0',
'49': r'1',
'50': r'2',
'51': r'3',
'52': r'4',
'53': r'5',
'54': r'6',
'55': r'7',
'56': r'8',
'57': r'9',
'59': r';',
'61': r'=',
'65': r'\alpha ',
'66': r'\beta ',
'67': r'\chi ',
'68': r'\delta ',
'69': r'\epsilon ',
'70': r'\phi ',
'71': r'\gamma ',
'72': r'\eta ',
'73': r'\iota ',
'74': r'j ',
'75': r'\kappa ',
'76': r'\lambda ',
'77': r'\mu ',
'78': r'\nu ',
'79': r'o ',
'80': r'\pi ',
'81': r'\theta ',
'82': r'\rho ',
'83': r'\sigma ',
'84': r'\tau ',
'85': r'\upsilon ',
'86': r'v ',
'87': r'\omega ',
'88': r'\xi ',
'89': r'y ',
'90': r'\zeta ',
'91': r'[',
# '92': r'\\',
'93': r']',
# '96': r'`',
'167': r'§',
'16777217': r'\quad', # tab
'16777219': '', # backspace
'16777220': '', # enter
}
}
# {'modifier': '16777248', # shift
# '16777248': {}},
# {'modifier': '16777249', # cmd
# '16777249': {}},
# {'modifier': '16777250', # ctrl
# '16777250': {}},
# {'modifier': '16777251', # alt
# '16777251': {}},


    # def parse_settings(self, settings):


    def latex_from_qt(self, keys_arr):
        if int(keys_arr[0]) <= 16777220: # no modifier
            self.latex += self.mapping['none'][keys_arr[0]]
        else:
            try:
                self.latex += self.mapping[keys_arr[0]][keys_arr[1]]
            except:
                pass
        return self.latex

    # def
