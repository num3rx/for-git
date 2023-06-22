def pd_check(word):
    if word == word[::-1]:
        return True
    else:
        return False
    

word = input()
print(pd_check(word))
