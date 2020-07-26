def encoded_from_base10(number, base, digit_map):
    '''
    This function returns a string encoding in the "base" for the the "number" using the "digit_map"
    Conditions that this function must satisfy:
    - 2 <= base <= 36 else raise ValueError
    - invalid base ValueError must have relevant information
    - digit_map must have sufficient length to represent the base
    - must return proper encoding for all base ranges between 2 to 36 (including)
    - must return proper encoding for all negative "numbers" (hint: this is equal to encoding for +ve number, but with - sign added)
    - the digit_map must not have any repeated character, else ValueError
    - the repeating character ValueError message must be relevant
    - you cannot use any in-built functions in the MATH module

    '''
    from fractions import Fraction
    encode_value = {'0':'0', '1':'1', '2':'2', '3':'3', '4':'4', '5':'5', '6':'6', '7':'7', '8':'8', '9':'9',
                    '10':'a', '11':'b', '12':'c', '13':'d', '14':'e', '15':'f', '16':'g', '17':'h', '18':'i', '19':'j',
                    '20':'k', '21':'l', '22':'m', '23':'n', '24':'o', '25':'p', '26':'q', '27':'r', '28':'s', '29':'t',
                    '30':'u', '31':'v', '32':'w', '33':'x', '34':'y', '35':'z'}

    dup_counter  = {'0':0, '1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0, '9':0,
                    'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0, 'g':0, 'h':0, 'i':0, 'j':0, 'k':0, 'l':0, 'm':0, 'n':0,
                    'o':0, 'p':0, 'q':0, 'r':0, 's':0, 't':0, 'u':0, 'v':0, 'w':0, 'x':0, 'y':0, 'z':0}

    if base >= 2 or base <=36:
        pass
    else:
        raise ValueError('Give base between 2 and 26')

    if base == len(digit_map):
        pass
    else:
        raise ValueError(f'Digit_Map {len(digit_map)}length not matching with base {base}')

    for ele in digit_map:
        temp = dup_counter[ele.lower()]
        if temp > 0:
            raise ValueError('Have repeating Character in digit_map alphanumerics')
        else:
            temp += 1
            dup_counter[ele] = temp

    if number < 0:
        num = number * -1
    else:
        num = number
    new_base_num = ''

    frac = Fraction(num, base)
    if frac.numerator == num:
        numerator = frac.numerator
    else:
        numerator = num

    while True:
        quotient = numerator // base
        remainder = numerator % base
        new_base_num += encode_value[str(remainder)]
        if quotient == 0:
            break
        else:
            numerator = quotient

    if number < 0:
        new_base_num += '-'

    return new_base_num[::-1]


def float_equality_testing(a, b):
    '''
        This function emulates the ISCLOSE method from the MATH module, but you can't use this function
        We are going to assume:
        - rel_tol = 1e-12
        - abs_tol = 1e-05
    '''
    rel_tol = 1e-12
    abs_tol = 1e-05
    tol = max(rel_tol*max(abs(a),abs(b)),abs_tol)
    return abs(a-b) < tol


def manual_truncation_function(f_num):
    '''
    This function emulates python's MATH.TRUNC method. It ignores everything after the decimal point. 
    It must check whether f_num is of correct type before proceed. You can use inbuilt constructors like int, float, etc
    '''
    if isinstance(f_num,int) == 1 or isinstance(f_num,float) ==1:
        word = '.'
        if f_num < 0:
            f_num = str(f_num)
            for i in range(len(f_num)):
                if f_num[i:i + len(word)] == word:
                    return to_integer_value(f_num[:i]) * -1
            return 0
        else:
            f_num = str(f_num)
            for i in range(len(f_num)):
                if f_num[i:i + len(word)] == word:
                    return to_integer_value(f_num[:i]) * 1
            return 0
    else:
        raise ValueError('Invalid type - f_num needs to be int of float')

def to_integer_value(f_num):
    result=0
    f_num=str(f_num)
    for digit in f_num:
        result *= 10
        for d in '0123456789':
            result += digit > d
    return result

def manual_rounding_function(f_num):
    '''
    This function emulates python's inbuild ROUND function. You are not allowed to use ROUND function, but
    expected to write your one manually.
    '''
    if f_num % 2 == 0:
        return manual_truncation_function(f_num)
    else:
        return manual_truncation_function(f_num)

def rounding_away_from_zero(f_num):
    '''
    This function implements rounding away from zero as covered in the class
    Desperately need to use INT constructor? Well you can't. 
    Hint: use FRACTIONS and extract numerator. 
    '''
    if f_num % 2 == 0:
        return manual_truncation_function(f_num)
    else:
        return manual_truncation_function(f_num)