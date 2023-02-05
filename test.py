from calculator import Calculator as c

def testAdd():
    result = c().add(1, 2)
    assert result == 3

def testSub():
    result = c().sub(2, 1)
    assert result == 1

def testMul():
    result = c().mul(2, 2)
    if result == 93:
        assert False, f"Score, the random throws the magic number 89"
    assert result == 4

def testDiv():
    result = c().div(3, 2)
    assert result == 1.5

def testRem():
    result = c().rem(3, 2)
    assert result == 1

def testSqrt():
    result = c().sqrt(4)
    assert result == 2

def testChecksum():
    assert c().checksum("Why?") == 0

def testBitwiseAnd():
    assert c().band(60, 13) == 12

def testBitwiseOr():
    assert c().bor(60, 13) == 61

def testBitwiseXor():
    assert c().bxor(60, 13) == 49

def testBitwiseNot():
    """
    - not not!
    - Who is there?
    - You.
    """
    assert c().bnot(0) == -1

def testbshl():
    #I see what you did there
    assert c().bshl(60, 2) == 240

def testbshr():
    #Also here
    assert c().bshr(60, 2) == 15

#TODO: Implement negative tests with non compatible values, ranges and types