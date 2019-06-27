# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 13:15:08 2019

@author: amtam
"""

def main():
    input_str = input('Enter a string: ')
    print()
    output_array = []
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
    
    input_str = input_str.lower()
    
    for char in input_str:
        try:
            new_char = nato[char]
        except:
            new_char = char
            
        output_array.append(new_char)
            
            
    output_str = ' '.join(output_array)
    print(output_str)
            
            
    
main()