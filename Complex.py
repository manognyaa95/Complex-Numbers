'''
    File name: Complex.py
    Author: Manognya Acharya
    Date created: 15/01/2022
    Date last modified: 15/01/2022
    Python Version: 3.8.8
    Description: Operations on complex numbers
'''

# TODOs:
# 1. Implement operations for more than 2 numbers
# 2. Implement to find the phase of a complex number (eg: phase of (a+ib) = arctan(b/a))
# 3. Exponential powers of complex number (eg: (a+ib)3)
# 4. Simplifying imaginary numbers (eg: sqrt(-9) = 3i)


from math import sqrt

# User defined class for operations on complex numbers
class Complex:
    # Constructor to assign real and imaginary parts
    # of the complex number
    def __init__(self, real, imag):
        self.real = real;
        self.imag = imag;
    
    # Function to find the conjugate of the complex number    
    def complex_conj(self, obj1):
        temp_conj = Complex(0,0);
        # Assigning real and imaginary parts for the conjugate
        temp_conj.real = obj1.real;
        temp_conj.imag = -1 * obj1.imag;
        return temp_conj
        
    # Function to add 2 complex numbers
    def complex_add(self, obj1, obj2):
        temp_add = Complex(0,0);
        # Adding real and imaginary parts
        temp_add.real = obj1.real + obj2.real;
        temp_add.imag = obj1.imag + obj2.imag;
        return temp_add
    
    # Function to subtract 2 complex numbers
    def complex_sub(self, obj1, obj2):
        temp_sub = Complex(0,0);
        # Subtracting real and imaginary parts
        temp_sub.real = obj1.real - obj2.real;
        temp_sub.imag = obj1.imag - obj2.imag;
        return temp_sub
    
    # Function to multiply 2 complex numbers    
    def complex_mul(self, obj1, obj2):
        temp_mul = Complex(0,0);
        # Multiplying real and imagnary parts
        temp_mul.real = obj1.real * obj2.real +  obj1.imag * obj2.imag *-1
        temp_mul.imag = obj1.real * obj2.imag + obj1.imag * obj2.real 
        return temp_mul
        
    # Function to divide 2 complex numbers by simplification   
    def complex_div(self, obj1, obj2):
        temp_div = Complex(0,0);
        # Finding the conjugate of the denominator complex number
        temp_conj = self.complex_conj(obj2);
        # Multiplying the numerator and denominator by the complex conjugate of the denominator
        temp_num = self.complex_mul(obj1,temp_conj);
        temp_den = self.complex_mul(obj2,temp_conj);
        
        # Check if denominator is not zero
        if temp_den.real !=0:
            # Dividing the real and imaginary parts of the numerator by the real part of the denominator
            temp_div.real = temp_num.real/temp_den.real;
            temp_div.imag = temp_num.imag/temp_den.real;
            return temp_div
        # Return ZeroDivisionError if denominator is zero
        else:
            print("ZeroDivisionError: division by zero")
            return (temp_div)
            
    # Function to find the absolute of a complex number
    def complex_abs(self, obj1):
        temp_abs = 0;
        temp_abs = sqrt(obj1.real ** 2 + obj1.imag ** 2);
        return temp_abs
        
        
        
if __name__=='__main__':
    # Assign the first complex number
    Num1 = Complex(8,-2);
    print("The first complex number is", Num1.real , "+j(",Num1.imag,")")
    #Assign the second complex number
    Num2 = Complex(-4,6);
    print("The second complex number is", Num2.real , "+j(",Num2.imag,")")
    
    # Define complex number for perfoming addition, subtraction, multipication and division of two complex numbers
    # Num3 = Complex(0,0);
    # Num3 = Num3.complex_add(Num1) # Num3.real = 4, Num3.imag = 4
    # Num3 = Num3.complex_sub(Num1,Num2) # Num3.real = 12, Num3.imag = -8
    # Num3 = Num3.complex_mul(Num1,Num2) # Num3.real = -20, Num3.imag = 56
    # Num3 = Num3.complex_div(Num1,Num2); # Num3.real = -0.8461538461538461, Num3.imag = -0.7692307692307693
    
    # print("The result complex number is", Num3.real , "+j(",Num3.imag,")")
    
    # Define number to find the absolute of a complex number
    Num3 = 0;
    Num4 = 0;
    Num3 = Num1.complex_abs(Num1);
    Num4 = Num2.complex_abs(Num2);
    print("The absolute of the first complex is", Num3) # Num3 = 8.246211251235321
    print("The absolute of the second complex is", Num4) # Num4 = 7.211102550927978
    
    

