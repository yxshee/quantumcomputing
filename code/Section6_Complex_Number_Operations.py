#!/usr/bin/env python3
"""
Section 6 – Complex Numbers in Python

Demonstrates conversion between Cartesian and polar forms using cmath.
"""
import cmath

def cartesian_to_polar(z):
    r, phi = cmath.polar(z)
    return r, phi

def polar_to_cartesian(r, phi):
    return cmath.rect(r, phi)

def main():
    z_str = input("Enter a complex number (e.g. 3+4j): ")
    z = complex(z_str.strip())

    r, phi = cartesian_to_polar(z)
    print(f"Polar form: r = {r:.4f}, θ = {phi:.4f} rad")

    z_back = polar_to_cartesian(r, phi)
    print(f"Back to Cartesian: {z_back}")

if __name__ == "__main__":
    main()
