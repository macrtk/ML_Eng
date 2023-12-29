## SIMPLE CLASS DESCRIBING A PERSON WITH 2 ATTRIBUTES

class Person(): 
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def greet(self):
        if self.age % 10 in {2,3,4}:
            print(f"Witaj, mam na imie {self.name} i mam {self.age} lata.")
        else:
            print(f"Witaj, mam na imie {self.name} i mam {self.age} lat.")
person1 = Person("Matt",35)
person1
Person.greet(person1)

### SAMPLE CLASS FOR DA

class DataAnalyzer:
    def __init__(self):
        # Initializer for the class
        self.data = []

    def load_data(self, data):
        # Method to load data into the class
        self.data = data

    def calculate_average(self):
        # Method to calculate the average of the data
        if not self.data:
            return "No data loaded"
        return sum(self.data) / len(self.data)

    def data_summary(self):
        # Method to display a summary of the data
        if not self.data:
            return "No data to summarize"
        return f"Data: {self.data}\nAverage: {self.calculate_average()}"

# Create an instance of the DataAnalyzer class
analyzer = DataAnalyzer()

# Load some sample data
sample_data = [10, 20, 30, 40, 50]
analyzer.load_data(sample_data)

# Display the data summary
analyzer.data_summary()
