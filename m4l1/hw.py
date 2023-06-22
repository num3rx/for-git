def pd_check(word):
    if word == word[::-1]:
        return True
    else:
        return False
    

print(pd_check('лепсспел'))
