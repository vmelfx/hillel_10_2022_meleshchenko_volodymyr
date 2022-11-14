import functools


# MODIFY THIS DECORATOR
def reverse_string(func):
    """If output is a string, reverse it. Otherwise, return None."""

    @functools.wraps(func)
    def wrapper():
        output = func()
        if isinstance(output, str):
            return output[::-1]
        return func()

    return wrapper


# TARGET FUNCTIONS
@reverse_string
def get_university_name() -> str:
    return "Western Institute of Technology and Higher Education"


@reverse_string
def get_university_founding_year() -> int:
    return 1957


# TEST OUPUT
print(get_university_name(), get_university_founding_year(), sep="\n")
