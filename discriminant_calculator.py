import math

# Calculate the discriminant
def find_root():

    print('ax^2 + bx + c = 0')  # This is an example to show the user as a draft
    a = int(input('a: '))       # Take the coefficient a
    b = int(input('b: '))       # Take the coefficient b
    c = int(input('c: '))       # Take the coefficient c

    # The discriminant formula
    discriminant = b**2 - 4*a * c

    # If discriminant greater than 0
    if discriminant > 0:
        sqrt_discriminant = math.sqrt(discriminant)
        print(f'Discriminant is = {discriminant}')
        print(f'Solution Set = [ {(-b + sqrt_discriminant) / 2*a}, {(-b - sqrt_discriminant) / 2*a} ]')

    # If discriminant equals to 0
    elif discriminant == 0:
        print(f'Discriminant is = {discriminant}')
        print(f'Solution Set = [ x1 = x2 = {-b / 2*a}]')

    # If discriminant is less than 0
    elif discriminant < 0:
        print(f'Discriminant is = {discriminant}')
        print('Solution Set = []\n')



# Run the func
find_root()
