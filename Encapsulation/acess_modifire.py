# ----------------------------------------------------
# PUBLIC:
# Accessible from anywhere, inside or outside the class.
# ----------------------------------------------------
class Main:
    def __init__(self):
        self.name = "hi"

m = Main()
print(m.name)  # Output: hi


# ----------------------------------------------------
# PROTECTED:
# Indicated by a single underscore (_). 
# Technically accessible outside, but warns other 
# developers it should only be used in subclasses.
# ----------------------------------------------------

class Main:
    def __init__(self):
        self._name = "hi"

m = Main()
print(m._name)  # Output: hi


# ----------------------------------------------------
# PRIVATE:
# Indicated by a double underscore (__).
# Triggers name mangling to prevent direct outside access.
# ----------------------------------------------------
class Main:
    def __init__(self):
        self.__name = "hi"

# Note: Running 'print(m.__name)' below this block 
# will raise an AttributeError because it is protected.