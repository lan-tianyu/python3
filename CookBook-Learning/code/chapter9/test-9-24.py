import ast
import inspect


class NameLower(ast.NodeVisitor):
    def __init__(self, lowered_names):
        self.lowered_names = lowered_names
    
    def visit_FunctionDef(self, node):
        code = xzSA


class CodeAnalyzer(ast.NodeVisitor):
    def __init__(self):
        self.loaded = set()
        self.stored = set()
        self.deleted = set()

    def visit_Name(self, node):
        print('node:', node)
        print('node.ctx', node.ctx)
        if isinstance(node.ctx, ast.Load):
            self.loaded.add(node.id)
        elif isinstance(node.ctx, ast.Store):
            self.stored.add(node.id)
        elif isinstance(node.ctx, ast.Del):
            self.deleted.add(node.id)


code = '''
for i in range(10):
    print('i:', i)
'''
top = ast.parse(code, mode='exec')
c = CodeAnalyzer()
c.visit(top)
print('Loaded:', c.loaded)
print('Stored:', c.stored)
print('Deleted:', c.deleted)

exec(compile(top, '<stdin>', 'exec'))
print('-' * 70)

x = 42
print(eval('2 + 3 *4 + x'))

exec('for i in range(10): print(\'i:\', i)')

ex = ast.parse('2 + 3* 4 + x', mode='eval')
print(ex)

print(ast.dump(ex))

top = ast.parse('for i in range(10):print(\'i:\', i)', mode='exec')
print(ast.dump(top))
