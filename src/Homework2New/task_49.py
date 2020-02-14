def min(*args, **kwargs):
    """Create minimum function like as build-in function

    :param args: any type witch could be compare
    :param kwargs: key for comparision
    :return: minimum of *args
    """
    key = kwargs.get("key", None)

    def inner_minimum(iter_object, key_inner):
        """Minimum finder inner function

        :param iter_object: object with __iter__ method
        :param key_inner: key for comparision
        :return: minimum from iter_object
        """

        minimum = iter_object[0]
        for arg in iter_object:
            if key_inner and key_inner(arg) < key_inner(minimum):
                minimum = arg
            elif not key and arg < minimum:
                minimum = arg
        return minimum

    if len(args) > 1:
        return inner_minimum(args, key)
    return inner_minimum(list(args[0]), key)


def max(*args, **kwargs):
    """Create maximum function like as build-in function

    :param args: any type witch could be compare
    :param kwargs: key for comparision
    :return: maximum of *args
    """
    key = kwargs.get("key", None)

    def inner_maximum(iter_object, key_inner):
        """Maximum finder inner function

        :param iter_object: object with __iter__ method
        :param key_inner: key for comparision
        :return: maximum from iter_object
        """

        maximum = iter_object[0]
        for arg in iter_object:
            if key_inner and key_inner(arg) > key_inner(maximum):
                maximum = arg
            elif not key and arg > maximum:
                maximum = arg
        return maximum

    if len(args) > 1:
        return inner_maximum(args, key)
    return inner_maximum(list(args[0]), key)


if __name__ == '__main__':

    assert max(3, 2) == 3
    assert min(3, 2) == 2
    assert max([1, 2, 0, 3, 4]) == 4
    assert min("hello") == "e"
    assert max(2.2, 5.6, 5.9, key=int) == 5.6
    assert min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0]
