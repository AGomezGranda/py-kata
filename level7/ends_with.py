# Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).

#ends with solution:
def solution(string, ending):
    return string.endswith(ending)

#complex solution
def complex_solution(text, ending):
    ends = len(ending)
    new_string = text[-ends:]
    return new_string == ending
