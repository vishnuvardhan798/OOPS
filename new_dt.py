
#Fraction class to represent a fraction with a numerator and denominator
class Fraction:
    #initializing of parameterizing the constructor
    def __init__(self,x,y):
        self.numerator=x
        self.denominator=y


    def __str__(self):
        return '{}/{}'.format(self.numerator,self.denominator)


    def __add__(self,other):
        new_numerator=self.numerator*other.denominator +other.numerator*self.denominator
        new_denominator=self.denominator*other.denominator
        return Fraction(new_numerator,new_denominator)


    def __sub__(self,other):
        new_numerator=self.numerator*other.denominator - other.numerator*self.denominator
        new_denominator=self.denominator*other.denominator

        return Fraction(new_numerator,new_denominator)


    def __mul__(self,other):
        new_numerator=self.numerator*other.numerator
        new_denominator=self.denominator*other.denominator

        return Fraction(new_numerator,new_denominator)



    def __truediv__(self,other):
        new_numerator=self.numerator*other.denominator
        new_denominator=self.denominator*other.numerator

        return Fraction(new_numerator,new_denominator)



    
fraction1=Fraction(2,3)
fraction2=Fraction(7,11)
fraction3=Fraction(4,11)
print(fraction1+fraction2+fraction3)
print(fraction1-fraction2-fraction3)
print(fraction1*fraction2*fraction3)
print(fraction1/fraction2/fraction3)
    

    











































# #this is for 2 fractions

# class Fraction:
#     def __init__(self,x,y):
#         self.numerator=x
#         self.denominator=y
#     def __str__(self):
#         return'{}/{}'.format(self.numerator,self.denominator)

#     def __add__(self,other):
#         new_numerator=self.numerator*other.denominator + other.numerator*self.denominator
#         new_denominator=self.denominator*other.denominator
#         return '{}/{}'.format(new_numerator,new_denominator)


#     def __sub__(self,other):
#             new_numerator=self.numerator*other.denominator - other.numerator*self.denominator
#             new_denominator=self.denominator*other.denominator
#             return '{}/{}'.format(new_numerator,new_denominator)



#     def __mul__(self,other):
#             new_numerator=self.numerator * other.numerator
#             new_denominator=self.denominator*other.denominator
#             return '{}/{}'.format(new_numerator,new_denominator)


#     def __truediv__(self,other):
#             new_numerator=self.numerator*other.denominator 
#             new_denominator=self.denominator*other.numerator
#             return '{}/{}'.format(new_numerator,new_denominator)


# fraction1=Fraction(2,3)
# fraction2=Fraction(7,11)
# print(fraction1+fraction2)
# print(fraction1-fraction2)
# print(fraction1*fraction2)
# print(fraction1/fraction2)