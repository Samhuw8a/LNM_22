import re
from itertools import chain, product, count as count_from


# Most of this is shamelessly stolen from Peter Norvig.

cat = ''.join
inf = float('inf')
flatten = chain.from_iterable


def mapl(f, iterable)->list:
    return list(map(f, iterable))

def mapt(f, iterable)->tuple:
    return tuple(map(f, iterable))

def filterl(f, iterable)->list:
    return list(filter(f, iterable))

def read_input(filename, datatype=str, sep='\n')->list:
    """Read a txt File by 'sep' (//n)"""
    filename = f"{filename:02d}" if isinstance(filename, int) else filename
    with open(f"{filename}.txt") as f:
        contents = f.read().strip().split(sep)
        return mapl(datatype, contents)

def read_input_line(filename, sep=''):
    """Read a txt File by line 'sep' (//n)"""
    filename = f"{filename:02d}" if isinstance(filename, int) else filename
    with open(f"{filename}.txt") as f:
        contents = f.read().strip()
        return contents if not sep else contents.split(sep)

def digits(line)->list:
    """Convert number-strings to Ints"""
    return mapl(int, line)

def integers(text, negative=True)->tuple:
    return mapt(int, re.findall(r"-?\d+" if negative else r"\d+", text))

def count(iterable, pred=bool)->int:
    """Returns all items returning True on 'pred'"""
    return sum(1 for item in iterable if pred(item))

def first(iterable, default=None):
    """returns the first element of a iterable"""
    return next(iter(iterable), default)

def filter_first(iterable, pred):
    """returns the first element of a iterable which is filterd with 'pred'"""
    return first(el for el in iterable if pred(el))

def manhattan(a, b=(0, 0))->int:
    """returns the manhatan distance of two points a and b"""
    return sum(abs(p - q) for p, q in zip(a, b))

def sign(n)->int:
    """returns the sign of an integer"""
    if n > 0: return 1
    elif n < 0: return -1
    else: return 0

def print_2d(lines)->None:
    """Print 2d matrix"""
    for line in lines:
        print(cat(line))

def maxval(d)->int:
    """Max value of d"""
    return max(d.values())

def transpose(matrix)->list:
    """transpose a matrix"""
    return list(zip(*matrix))

def bin2int(s)->int:
    """binary to int"""
    return int(s, 2)

def neighbours(x, y, amount=4):
    """All neighbours"""
    assert amount in {4, 8, 9}
    for dy, dx in product((-1, 0, 1), repeat=2):
        if ((amount == 4 and abs(dx) != abs(dy)) or
            (amount == 8 and not dx == dy == 0) or
             amount == 9):
            yield (x+dx, y+dy)

def list2grid(lines, pred=None):
    return {(x, y): val
            for y, line in enumerate(lines)
            for x, val in enumerate(line)
            if (pred(val) if pred else True)}

def grid2list(grid, pred=bool):
    max_x, max_y = map(max, zip(*grid))
    lines = [[' ' for _ in range(max_x+1)]
                  for _ in range(max_y+1)]
    for x, y in grid:
        if pred(grid[(x, y)]):
            lines[y][x] = '█'
    return lines


if __name__ == "__main__":
    assert cat(["ab", "cd", "ef"]) == "abcdef"
    assert mapl(int, ["1", "2"]) == [1, 2]
    assert mapt(int, ["1", "2"]) == (1, 2)
    assert filterl(lambda x: x > 3, [1, 5, 2, 4, 3]) == [5, 4]
    assert digits("123") == [1, 2, 3]
    assert integers("23 -42 55") == (23, -42, 55)
    assert integers("23 -42 55", negative=False) == (23, 42, 55)
    assert count([3, -5, 10, -7, 33], lambda x: x > 0) == 3
    assert first([2, 4, 6, 8]) == 2
    assert filter_first([2, 7, 4, 6, 8], lambda x: x > 5) == 7
    assert manhattan((5, -3)) == 8
    assert manhattan((5, -3), (2, 7)) == 13
    assert maxval(dict(a=3, b=99, c=66)) == 99
    assert tuple(neighbours(5, 7)) == ((5, 6),
                               (4, 7),         (6, 7),
                                       (5, 8))
    assert tuple(neighbours(5, 7, amount=8)) == ((4, 6), (5, 6), (6, 6),
                                                 (4, 7),         (6, 7),
                                                 (4, 8), (5, 8), (6, 8))
    assert list2grid([[10, 20], [30, 40]]) == {(0, 0): 10, (1, 0): 20,
                                               (0, 1): 30, (1, 1): 40}
    assert grid2list({(0, 1): 1, (1, 0): 1, (2, 0): 1}) == [[' ', '█', '█'],
                                                            ['█', ' ', ' ']]
    print(tuple(neighbours(5,7)))
