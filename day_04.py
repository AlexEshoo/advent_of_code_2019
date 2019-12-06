from functools import partial


def is_valid_password(pwd, extra_strict=False):
    s = str(pwd)
    is_correct_length = len(s) == 6
    has_repeated_digits = any(len(set(s[i:i + 2])) == 1 for i in range(5))
    digits_strictly_increase = all(int(s[i + 1]) >= int(s[i]) for i in range(5))
    has_no_triple_repeats = not any(len(set(s[i:i + 3])) == 1 for i in range(4))

    if extra_strict:
        # largest_pair = max(len(set(s[i:i + 2])) == 1 for i in range(5))
        return all((is_correct_length, has_repeated_digits, digits_strictly_increase, has_no_triple_repeats))

    return all((is_correct_length, has_repeated_digits, digits_strictly_increase))


# PART I
valid_passwords = list(filter(is_valid_password, range(134792, 675811)))
print(f"There are {len(valid_passwords)} valid passwords in the range provided.")

# PART II
valid_passwords = list(filter(partial(is_valid_password, extra_strict=True), range(134792, 675811)))
print(f"There are {len(valid_passwords)} valid passwords with strict requirements in the range provided.")
