class TwoDvector:
    def __init__(self, i, j):
        self.i = i
        self.j = j
    
    def show(self):
        print(f" The vector is ({self.i}i + {self.j}j)")


class ThreeDvector(TwoDvector):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.k = k
    
    def show(self):
        print(f" The vector is ({self.i}i + {self.j}j + {self.k}k)")


a = TwoDvector(3, 4)
a.show()
b = ThreeDvector(5, 6, 7)
b.show()


# Explain each line of code above with comments:-

# Define a class named TwoDvector to represent a 2D vector
# The __init__ method initializes the vector with i and j components
# The show method prints the vector in a formatted string
# Define a class named ThreeDvector that inherits from TwoDvector to represent a 3D vector
# The __init__ method initializes the vector with i, j, and k components
# It calls the parent class's __init__ method to set i and j, and sets k
# The show method overrides the parent class's show method to include the k component
# Create an instance of TwoDvector with i=3 and j=4
# Call the show method to display the 2D vector
# Create an instance of ThreeDvector with i=5, j=6, and k=7
# Call the show method to display the 3D vector
# The output will show the components of both vectors in the specified format 