def bubble_sort(lst):
    """
    冒泡排序

    >>> lst = [1,2,3,6,5,4,0]
    >>> bubble_sort(lst)
    >>> lst
    [0, 1, 2, 3, 4, 5, 6]
    >>> lst = [2,1]
    >>> bubble_sort(lst)
    >>> lst
    [1, 2]
    >>> lst = [0]
    >>> bubble_sort(lst)
    >>> lst
    [0]
    """
    # 从左到右执行 n - 1 轮
    for i in range(len(lst) - 1):
        swaped = False
        # 每一轮都把最大的数据从左往右推到 n - 1 -i 的位置上
        for j in range(len(lst) - 1 -i ):
            if lst[j] > lst[j + 1]:
                lst[j],lst[j+1] = lst[j+1],lst[j]
                swaped = True
        #如果在一轮冒泡中没有经历交换环节说明整个列表是有序的，停止冒泡过程
        if swaped == False:
            break

if __name__ == "__main__":
    import doctest
    doctest.testmod()