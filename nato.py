# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 13:15:08 2019

@author: amtam
"""

def processString(input_str):
    """
    Pre-process the input string so that it can be converted to NATO alphabet. At the bare minimum, needs to change input_str to lowercase.
    Parameters:
        input_str (str): String input by user.
    Returns:
        str_processed (str): Processed string
    """
    input_str = input_str.lower()

    return input_str

def toNATO(string_in, nato):
    """
    Convert lowercase string to its NATO phonetic alphabet equivalent. If it is not a regular letter (e.g. punctuation), don't change it to anything.
    Parameters:
        string_in (str): String to be changed to NATO alphabet. Assumed to be in all lowercase characters.
        nato (dict): Maps each alphabetic letter (lowercase) to its NATO phonetic alphabet equivalent.
    Returns:
        string_out (str): Converted string, in NATO alphabet form.
    Variables:
        output_array (list): Holds the strings of NATO equivalent for each letter in the string_in.
    """
    output_array = []
    for char in string_in:
        try:
            new_char = nato[char]
        except:
            new_char = char
            
        output_array.append(new_char)

    string_out = ' '.join(output_array)
    return string_out


def main():
    input_str = input('Enter a string: ')
    print()

    nato = {'a': 'Alfa',
            'b': 'Bravo',
            'c': 'Charlie',
            'd': 'Delta',
            'e': 'Echo',
            'f': 'Foxtrot',
            'g': 'Golf',
            'h': 'Hotel',
            'i': 'India',
            'j': 'Juliett',
            'k': 'Kilo',
            'l': 'Lima',
            'm': 'Mike',
            'n': 'November',
            'o': 'Oscar',
            'p': 'Papa',
            'q': 'Quebec',
            'r': 'Romeo',
            's': 'Sierra',
            't': 'Tango',
            'u': 'Uniform',
            'v': 'Victor',
            'w': 'Whiskey',
            'x': 'X-ray',
            'y': 'Yankee',
            'z': 'Zulu'
            }
    
    
    input_str_processed = processString(input_str)
    output_str = toNATO(input_str_processed, nato)
    print(output_str)
            
            
    
main()