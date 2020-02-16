from .a import A


class B(A):
    def bar(self):
        print('B...bar')
    
    def spam(self):
        return super().spam()