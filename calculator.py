
import numexpr as ne


def calculate(input_string: str) -> str:
    """
    Solves the equations
    :param input_string: string with equation
    :return: result or error message
    """
    try:
        result = ne.evaluate(input_string)
        return str(result)
    except (KeyError, SyntaxError, TypeError):
        return 'Please enter an equation containing only numbers and ' \
               'operators without letters, emojis, double symbols, brackets, etc.'
