

class Sample:
    def print_sample(self):
        print("This is a sample class.")

class SampleChild(Sample):
    def print_sample(self):
        print("This is a child class.")


obj = SampleChild()

obj.print_sample()