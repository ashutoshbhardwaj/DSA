"""This program is intended to be used to reverse_list
@author: Ashutosh
"""


def reverse_list(li: list[int]) -> list[int]:
    """Reverse the array

    Args:
        list (list): list array
    """
    start_index: int = 0
    end_index: int = len(li) - 1

    while start_index < end_index:
        li[start_index], li[end_index] = li[end_index], li[start_index]
        start_index += 1
        end_index -= 1

    return li


test_reverse_list = """
    >>> reverse_list([1,2,3,4])
    [4, 3, 2, 1]
    """


__test__ = {key: value for key, value in locals().items() if key.startswith("test_")}

if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
