from mymodule import foo
import mymodule as mm


print(foo("foo"))

print(mm.foo("foo"))

newtext=foo("mars")
print(newtext)