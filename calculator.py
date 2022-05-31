from typing import Union

import numexpr as ne


def calculate(input_string: str) -> Union[int, float, str]:
    """
    Solves the equations
    :param input_string: string with equation
    :return: result or error message
    """
    try:
        result = ne.evaluate(input_string)
        return result
    except (KeyError, SyntaxError, TypeError):
        return 'Please enter an equation containing only numbers and ' \
               'operators without letters, emojis, double symbols, brackets, etc.'
