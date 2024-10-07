
class A :
    def call_a(self):
        print("From A")

class B(A):
    def call_b(self):
        print("From B")

class C(A):
    def call_c(self):
        print("From C")


b = B()
b.call_a()
b.call_b()

c=C()
c.call_a()
c.call_c()