def is_leap(year):
    if year % 4 == 0:
        return True
        if year % 100 == 0:
            return False
            if year % 400 == 0:
                return True
    #         else:
    #             return False
    #     else:
    #         return True
    # else:
    #     return False
is_leap(2024)