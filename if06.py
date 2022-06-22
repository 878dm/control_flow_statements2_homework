def main(n):
    x=n%10
    n=n//10
    z=n%10
    n=n//10
    y=n%10
    n=n//10
    k=n%10
    n=n//10
    j=n%10
    if x>z and x>y and x>k and x>j :
        return 1
    if z>x and z>y and z>k and z>j :
        return 2
    if y>x and y>z and y>j and y>k :
        return 3
    if j>x and j>y and j>z and j>k :
        return 5
    return 4
    """
    Find the index of the largest digit of the five-digit number.
    Args:
        n: Five-digit number.
    Returns:
        int: return answer.
    """
    # return
print(main(55487))