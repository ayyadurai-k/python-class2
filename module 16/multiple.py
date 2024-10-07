
class A :
    def call_a(self):
        print("From A")

class B:
    def call_b(self):
        print("From B")

class C:
    def call_c(self):
        print("From C")

class D(A,B,C):
    def call_d(self):
        print("From D")


d = D()

d.call_a()

d.call_b()

d.call_c()

d.call_d()