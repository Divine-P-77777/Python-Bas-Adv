class Employee:
    a = 1
    
    @classmethod  #👉 The method belongs to the class, not to an object.
                  # It takes cls (the class itself) as the first argument — not self.  

    def show(cls):
        print(f"The class attribute of a is {cls.a}")

e = Employee()
e.a = 45

e.show()


# Use it when you want to change or access class-level data (cls), not instance data (self).
