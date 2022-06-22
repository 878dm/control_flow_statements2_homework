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
        return x
    if z>x and z>y and z>k and z>j :
        return z
    if y>x and y>z and y>j and y>k :
        return y
    if j>x and j>y and j>z and j>k :
        return j
    return k
    """
    Find the largest digit of the five-digit number.
    Args:
        n: Five-digit number.
    Returns:
        int: return answer.
    """
    # return x,z,y,k,j
print(main(55487))