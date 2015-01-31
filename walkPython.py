import sys, ast

cppcode = ""

parents = []

class NodeWalker(ast.NodeVisitor):
    def __init__(self):
        self.indent=''
    def visit_Import(self, node):
        print self.indent, 'Process Import'
        self.visitChildren(node)
    def visit_Str(self, node):
        print self.indent, 'String:', repr(node.s)

    def visitChildren(self, node):
        old_indent = self.indent
        self.indent += '  '
        for kid in ast.iter_child_nodes(node):
            self.visit(kid)
        self.indent = old_indent

    def generic_visit(self, node):
		global cppcode
		if (type(node).__name__ == 'Assign'):
			parents.append("Assign")
			for kid in ast.iter_child_nodes(node):
				self.visit(kid)
		elif (type(node).__name__ == 'Num'):
#			node.operand = ast.Num()
			cppcode += str(node.n) + '\n'
		elif (type(node).__name__ == 'Add'):

		print self.indent, 'Generic visit', node, type(node).__name__
		self.visitChildren(node)

pycode = ast.parse(open(sys.argv[1]).read(), sys.argv[1])
NodeWalker().visit(pycode)

print cppcode
