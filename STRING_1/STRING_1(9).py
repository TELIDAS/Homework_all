def combo_string(string_a, string_b):
    if len(string_a)<len(string_b):
        return string_a + string_b + string_a
    else:
        return string_b + string_a + string_b



print(combo_string("HELLO", "HI"))
print(combo_string("HI", "HELLO"))
print(combo_string("aaa", "B"))