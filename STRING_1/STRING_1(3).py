def make_tags(tag, string):
    return "<" + tag + ">" +string+"</"+tag+">"


print(make_tags("i", "Hello"))
