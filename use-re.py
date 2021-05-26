import re
req = re.compile("hello")

test = "hello wprld"
print(type(req))
print(req.search(test))
print(req.findall(test))
print(req.match(test))
print(req.sub("python", test))

req = re.compile(r"\s*hello\s*")
test = "hii hello python hello hello!"
print(req.split(test))
print(req.split(test, 2))