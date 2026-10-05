def stop_iteration():
    return next(iter([]))


def zero_division():
    return 1 / 0


def assertion_error():
    assert False, "Intentional assertion failure"


def import_error():
    from math import this_name_does_not_exist


def key_error():
    return {}["missing"]


def syntax_error():
    compile("if True print('hello')", "example", "exec")


def indentation_error():
    compile("if True:\nprint('hello')", "example", "exec")


def type_error():
    return 4 + "3"


def main():
    examples = [
        (stop_iteration, StopIteration), (zero_division, ZeroDivisionError),
        (assertion_error, AssertionError), (import_error, ImportError),
        (key_error, KeyError), (syntax_error, SyntaxError),
        (indentation_error, IndentationError), (type_error, TypeError),
    ]
    for function, expected_exception in examples:
        try:
            function()
        except expected_exception as error:
            print(f"{function.__name__}: {type(error).__name__}")
        else:
            raise AssertionError(f"{function.__name__} did not raise the expected exception")


if __name__ == "__main__":
    main()
