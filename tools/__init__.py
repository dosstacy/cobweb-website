import re

def convert_to_sympy(expression):
    replacements = {
        r'\btg\b': 'tan',
        r'\bctg\b': '1/tan',
        r'\bln\b': 'log',
        r'√': 'sqrt',
        r'\^': '**'
    }

    for pattern, replacement in replacements.items():
        expression = re.sub(pattern, replacement, expression)

    return expression