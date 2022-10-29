def delete(list_, index=None):
    if index is None:
        one = list_[:-2]
        two = list_[-1:]
        spisok_ = one + two
        return spisok_
    else:
        one = list_[:index]
        two = list_[index + 1:]
        spisok_ = one + two
        return spisok_

print(delete([0, 0, 1, 2], index=0))  # [0, 1]
print(delete([0, 1, 1, 2, 3], index=1))  # [0, 1, 2]
print(delete([0, 1, 2, 3, 4, 4]))  # [0, 1, 2, 3]
