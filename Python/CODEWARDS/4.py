"""from solution import narcissistic
import codewars_test as test

@test.describe("Examples")
def examples():
    
    @test.it("Narcissistic numbers")
    def narcissistic_tests():
        test.assert_equals(narcissistic(7), True, '7 is narcissistic');
        test.assert_equals(narcissistic(371), True, '371 is narcissistic');

    @test.it("Not narcissistic numbers")
    def not_narcissistic_tests():
        test.assert_equals(narcissistic(122), False, '122 is not narcissistic')
        test.assert_equals(narcissistic(4887), False, '4887 is not narcissistic')"""

def narcissistic( value ):
    suma = 0
    for numero in str(value):
        suma += int(numero)**len(str(value))
        if suma == value:
            return True
    return False

print(narcissistic(371))