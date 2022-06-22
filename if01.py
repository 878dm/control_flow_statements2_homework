def main(a,b,c):
    if a>=b and a>=c :
        return a
    if b>=a and b>=c :
        return b
    return c

    """
    Find the largest of the numbers.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    # return
print(main(7,8,9))