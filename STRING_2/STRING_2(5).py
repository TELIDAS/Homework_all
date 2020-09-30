def end_other(a, b):
    a = a.lower()
    b = b.lower()
    return a[-(len(b)):] == b or a == b[-(len(a)):]
print(end_other("Hiabc", "abc"))
print(end_other("AbC", "HiaBc"))
print(end_other("abc", "abXabc"))
