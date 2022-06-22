def main(a,b,c):
    if a>=b and b>=c or a<=b and b<=c:
        return b
    if b>=a and a>=c or b<=a and a<=c:
        return a
    return c

    """
    Determine the number between large and small.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    # return
print(main(5,5,7))