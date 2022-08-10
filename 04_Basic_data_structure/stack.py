class Stack:

    def __init__(self):
        self.ls = []

    def isEmpty(self):
        return self.ls == []

    def push(self, var):
        self.ls.append(var)

    def pop(self):
        return self.ls.pop()

    def peek(self):
        return self.ls[len(self.ls) - 1]

    def size(self):
        return len(self.ls)


def rev_string(seq):
    r_stack = Stack()
    out = ""
    for i in list(seq):
        r_stack.push(i)
    for j in range(len(seq)):
        out = out + r_stack.pop()
    return out


def sym_balance(seq):
    res = True
    symb_list = [40, 41, 91, 93, 123, 125]
    b_stack = Stack()
    symb_in = list(seq)
    if len(symb_in) > 1:
        b_stack.push(symb_in[0])
    flag = -1
    for i in symb_in[1:]:
        if b_stack.isEmpty() and i == symb_in[len(symb_in) - 1]:
            res = i
        else:
            if not b_stack.isEmpty():
                x = ord(b_stack.peek())
            for j in range(1, len(symb_list), 2):
                flag = 0
                if ord(i) == symb_list[j] and x == symb_list[j - 1]:
                    b_stack.pop()
                    if b_stack.isEmpty() and i == symb_in[len(symb_in) - 1]:
                        res = True
                    break
                elif ord(i) == symb_list[j - 1] and i != symb_in[len(symb_in) - 1]:
                    flag = 1
                    break
                else:
                    flag = 2
            if flag == 1:
                b_stack.push(i)
            elif flag == 2:
                res = i
                break
    return res

# print(sym_balance("[[()]()([])]"))

def test_stack():
    c = Stack()
    result = sym_balance("[[()]()([])]")
    assert result == True, "wrong answer: %s" % result
    result = sym_balance("[{)}]")
    assert result == ')', "wrong answer: %s" % result
    result = sym_balance("[{}}]")
    assert result == '}', "wrong answer: %s" % result
    result = sym_balance("[({}]")
    assert result == ']', "wrong answer: %s" % result
    result = sym_balance("[")
    assert result == True, "wrong answer: %s" % result
    result = sym_balance("[()))]")
    assert result == ')', "wrong answer: %s" % result
    result = sym_balance("(((())))))))))))")
    assert result == ')', "wrong answer: %s" % result
    result = sym_balance("][")
    assert result == '[', "wrong answer: %s" % result

    print("Well done")

    # assert c.peek() == 123, f"wrong answer: {c.peek()}"
    # c.push(222)
    # c.push(334)
    # x = c.pop()
    # assert x == 334, f"wrong answer:{x}"
    # assert rev_string("Hello!") == "!olleH", "wrong answer: %s}" % rev_string("Hello!")
    # print('Purrrrfect!')

if __name__ == "__main__":
    test_stack()
