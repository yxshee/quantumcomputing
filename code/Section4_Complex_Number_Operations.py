#!/usr/bin/env python3
"""
Section 4 – Complex Number Operations
"""
import cmath

def read_complex():
    z_str = input("Enter complex number (e.g. 3+4j): ")
    return complex(z_str)

def magnitude(z):
    return abs(z)

def main():
    z = read_complex()
    conjugate = z.conjugate()

    print(f"z = {z}")
    print(f"Conjugate = {conjugate}")
    print(f"Addition (z + conjugate) = {z + conjugate}")
    print(f"Subtraction (z - conjugate) = {z - conjugate}")
    print(f"Multiplication (z * conjugate) = {z * conjugate}")
    try:
        print(f"Division (z / conjugate) = {z / conjugate}")
    except ZeroDivisionError:
        print("Division by zero not possible (conjugate is zero).")
    print(f"Interpreting as 2D vector (x, y) = ({z.real}, {z.imag})")
    print(f"Magnitude |z| = {magnitude(z)}")

if __name__ == "__main__":
    main()
