def foo(myvariable):
    """Foo takes a string as parameter and adds bar to it"""    
    myvariable += "bar"
    return myvariable




if __name__ == '__main__':
    text = "foo"
    print(foo(text))
