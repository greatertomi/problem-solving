# Task Link: https://app.codility.com/programmers/lessons/90-tasks_from_indeed_prime_2015_challenge/longest_password/

def password_validity_checker(password: str):
    count_num = 0
    count_alpha = 0
    for char in password:
        if not char.isalpha() and not char.isdigit():
            return False
        else:
            if char.isalpha():
                count_alpha += 1
            elif char.isdigit():
                count_num += 1

    if count_alpha % 2 == 0 and count_num % 2 == 1:
        return True
    else:
        return False


def longest_password(string: str):
    passwords = string.split()
    maxLen = 0
    for pwd in passwords:
        if password_validity_checker(pwd):
            if len(pwd) > maxLen:
                maxLen = len(pwd)
    return maxLen


value = "te56"
print(longest_password(value))
