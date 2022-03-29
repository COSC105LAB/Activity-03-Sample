import sampleClass as sample

# Return without params
print("Return without params: ", sample.SampleClass.sampleReturnFunction(), end='\n\n')

# Return with set params
print("Return with set params: ", sample.SampleClass.sampleReturnWithParams(2,3,4), end='\n\n')

# Return with input params
# We use the int() method to cast the output from input() as integer
# since the method will always return a string.
a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))
c = int(input("Enter number 3: "))
print("Return with input params: ", sample.SampleClass.sampleReturnWithParams(a,b,c), end='\n\n')

# Direct method call
sample.SampleClass.sampleFunctionWithoutReturn()
