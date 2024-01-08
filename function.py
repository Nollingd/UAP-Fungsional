#2.2
def is_palindrome(s):
    s = ''.join(filter(str.isalnum, s.lower()))
    return s == s[::-1]

kata = "Kasur ini rusak"
hasil = is_palindrome(kata)
print(f"{hasil}")