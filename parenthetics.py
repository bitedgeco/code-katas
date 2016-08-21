# _*_ coding: utf-8 _*_


def parenthetics(string):
    opens = string.count('(')
    closes = string.count(')')
    if opens > closes:
        return 'open'
    elif closes > opens:
        return 'broken'
    else:
        return 'balanced'


if __name__ == '__main__':
    parenthetics('()')
