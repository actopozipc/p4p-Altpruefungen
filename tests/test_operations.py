import operations as op
a = 2
b = 3
def test_add():
    assert op.add(a, b) == a+b
def test_sub():
    assert op.sub(a, b) == a-b
def test_mult():
    assert op.mult(a, b) == a*b
def test_div():
    assert op.div(a, b) == a/b       