def select_sort(lst):
    """
    选择排序算法: 
    思想：
        1、对于一个列表只要它的前 n-1 个元素有序，那么整个列表就是有序的了

    >>> lst = [3,2,1,4,5,6,-1]
    >>> select_sort(lst)
    >>> lst
    [-1, 1, 2, 3, 4, 5, 6]
    >>> 
    >>> lst = [2,1]
    >>> select_sort(lst)
    >>> lst
    [1, 2]
    >>> 
    >>> lst = [0]
    >>> select_sort(lst)
    >>> lst
    [0]
    """
    # 把前 n - 1 个元素正确的排列了，那么整个列表就是有序的了
    for i in range(0,len(lst) - 1):
        min_item_index = i
        # 找出 i ~ ( n - 1 ) 中最小的元素，并把它填到位置 i
        for j in range(i + 1,len(lst)):
            if lst[j] < lst[min_item_index]:
                min_item_index = j
        # 当 min_item_index != i 时就直接交换
        if min_item_index != i:
            lst[min_item_index],lst[i] = lst[i],lst[min_item_index]


if __name__ == "__main__":
    import doctest
    doctest.testmod()