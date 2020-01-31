class Node:
    pass


class UnaryOperator(Node):
    def __init__(self, operand):
        self.operand = operand


class BinaryOperatpr(Node):
    def __init__(self, left, right):
        self.left = left
        self.right = right


class Add(BinaryOperatpr):
    pass


class Sub(BinaryOperatpr):
    pass


class Mul(BinaryOperatpr):
    pass


class Div(BinaryOperatpr):
    pass


class Negate(UnaryOperator):
    pass


class Number(Node):
    def __init__(self, value):
        self.value = value


class NodeVistor:
    def visit(self, node):
        methname = 'visit_' + type(node).__name__
        meth = getattr(self, methname, None)
        # print('methname:', methname, ' , meth:', meth)
        if meth is None:
            meth = self.generic_visit
        return meth(node)

    def generic_visit(self, node):
        raise RuntimeError('No {} method'.format('visit_' +
                                                 type(node).__name__))


class Evaluator(NodeVistor):
    def visit_Number(self, node):
        return node.value

    def visit_Add(self, node):
        return self.visit(node.left) + self.visit(node.right)

    def visit_Sub(self, node):
        return self.visit(node.left) - self.visit(node.right)

    def visit_Mul(self, node):
        return self.visit(node.left) * self.visit(node.right)

    def visit_Div(self, node):
        return self.visit(node.left) / self.visit(node.right)

    def visit_Negate(self, node):
        return -node.operand


t1 = Sub(Number(3), Number(4))
t2 = Mul(Number(2), t1)
t3 = Div(Number(5), t2)
t4 = Add(Number(1), t3)

e = Evaluator()
print(e.visit(t1))
print(e.visit(t2))
print(e.visit(t3))
print(e.visit(t4))


class StackCode(NodeVistor):
    def generic_code(self, node):
        self.instructions = []
        self.visit(node)
        return self.instructions

    def visit_Number(self, node):
        self.instructions.append(('PUSH', node.value))

    def binop(self, node, instruction):
        self.visit(node.left)
        self.visit(node.right)
        self.instructions.append((instruction, ))
        print('binop...instructions:', self.instructions)

    def visit_Add(self, node):
        self.binop(node, 'ADD')

    def visit_Sub(self, node):
        self.binop(node, 'SUB')

    def visit_Mul(self, node):
        self.binop(node, 'MUL')

    def visit_Div(self, node):
        self.binop(node, 'DIV')

    def unaryop(self, node, instruction):
        self.visit(node.operand)
        self.instructions.append((instruction, ))

    def visit_Negate(self, node):
        self.unaryop(node, 'NEG')


print('-' * 70)
s = StackCode()
s.generic_code(t4)