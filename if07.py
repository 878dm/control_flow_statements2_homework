def main(temp):
    if temp<0 : 
        return "Freezing"
    if  temp<=10 and temp<=1 :
        return "Ver Cold"
    if temp<=20 and temp<=11 :
        return "Cold"
    if temp<=21 and temp<=30 :
        return "Normal"
    if temp<=31 and temp<=40 :
        return "Hot"
    return "Very Hot"
    """
    Display the message according to the following temperature conditions given to you in Celsius:
    Use the elif statments.
    Temp<0: "Freezing"
    Temp 1-10: "Very Cold"
    Temp 11-20: "Cold"
    Temp 21-30: "Normal"
    Temp 31-40: "Hot"
    Temp >40: "Very Hot"
    Args:
        temp: Temperature in Celsius.
    Returns:
        str: return answer.
    """
    # return
print(main(-9))