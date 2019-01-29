import logging
from logging import handlers

def insert_sort(lst):
    """
    >>> lst = [1,2,3,6,5,4,0]
    >>> insert_sort(lst)
    >>> lst
    [0, 1, 2, 3, 4, 5, 6]
    >>> lst = [2,1]
    >>> insert_sort(lst)
    >>> lst
    [1, 2]
    >>> lst = [0]
    >>> insert_sort(lst)
    >>> lst
    [0]
    """
    for i in range(1,len(lst)):
        temp = lst[i]
        j = i - 1
        while j >= 0:
            if lst[j] > temp :
                lst[j + 1] = lst[j]
                j = j - 1
            else:
                break
        lst[j + 1] = temp

if __name__ == "__main__":
    import doctest
    doctest.testmod()


            