class A:
    def call_a(self):
        print("From A")

class B(A):
    def call_b(self):
        print("From B")

class C(B):
    def call_c(self):
        print("From C")

c = C()

c.call_c()

c.call_b()

c.call_a()