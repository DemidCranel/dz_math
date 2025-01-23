import sympy as sp
from sympy.parsing.sympy_parser import parse_expr
from sympy.parsing.sympy_parser import standard_transformations,implicit_multiplication_application
from sympy.plotting import plot

x = sp.symbols('x')

number = 1

mission = {
    (x**2-5*x+6)/(x**2-12*x+20):2,
    (x**3-x**2+2*x)/(x**2+x):0,
    (6+x-x**2)/(x**3-27):3,
    (2*x**2-x-1)/(3*x**2-x-2):1,
    (2*x**2-7*x+4)/(x**2-5*x+6):2,
    (12+x-x**2)/(x**3-27):3,
    (3*x**2+2*x-1)/(27*x**3-1):1/3,
    (x**2-4*x-5)/(x**2-2*x-3):-1,
    (3*x**2+2*x-1)/(-x**2+x+2):-1,
    (3*x**2-11*x+6)/(2*x**2-5*x-3):3,
    (x**3-8)/(x**2+x-6):2,
    (x**2-x-2)/(x**3+1):-1,
    (x**2-16)/(x**2+x-20):4,
    (4*x**2+11*x-3)/(x**2+2*x-3):-3,
    (3*x**2-7*x-6)/(2*x**2-7*x+3):3,
    (4*x**2+7*x-2)/(3*x**2+8*x+4):-2,
    (5*x**2+4*x-1)/(3*x**2+x-2):-1,
    (x**2-4*x-5)/(3*x**2+2*x-2):-1,
    (7*x**2+4*x-3)/(2*x**2+3*x+1):-1,
    (3*x**2-3*x+2)/(x**2-x-12):4,
    (2*x**2-9*x+10)/(x**2+3*x-10):2,
    (4*x**2+x-5)/(x**2-2*x+1):1,
    (-5*x**2+11*x-2)/(3*x**2-x-10):2,
    (x**2-5*x-14)/(2*x**2-9*x-35):7,
    (3*x**2-6*x-45)/(2*x**2-3*x-35):5,
    (4*x**2+3*x+15)/(x**2-6*x-27):-3,
    (x**2-2*x-35)/(2*x**2+11*x+5):-5,
    (2*x**2+15*x-8)/(3*x**2+25*x+8):-8,
    (3*x**2-2*x-40)/(x**2-3*x-4):4,
    (2*x**2+5*x-3)/(3*x**2+10*x+3):-3
}

for key in mission:

    expression = key
    print(f'Задача 1.{number}: {expression}')
    number += 1

    limit_expression = sp.limit(expression, x, mission[key])
    print(f'Ответ: {limit_expression}')
