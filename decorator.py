def kalimat_palindrome_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result:
            return "Kalimat tersebut merupakan sebuah palindrome."
        else:
            return "Kalimat tersebut bukan sebuah palindrome."
    return wrapper

def is_palindrome(s):
    s = ''.join(filter(str.isalnum, s.lower()))
    return s == s[::-1]

is_palindrome = kalimat_palindrome_decorator(is_palindrome)

kata = "Kasur ini rusak"
hasil = is_palindrome(kata)
print(hasil)