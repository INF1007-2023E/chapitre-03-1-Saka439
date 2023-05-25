#!/usr/bin/env python
# -*- coding: utf-8 -*-


import math

def square_root(a: float) -> float:
   b = squrt(a)

def square(a: float) -> float:
  c = power(a,2)
return b, c


def average(a: float, b: float, c: float) -> float:
    somme = a + b + c
    moy = somme/3
    return moy


def to_radians(angle_degs: float, angle_mins: float, angle_secs: float) -> float:
    
    return 



def to_degrees(angle_rads: float) -> tuple:
    
    return 


def to_celsius(temperature: float) -> float:
  temp_in_celsius = (temperature - 32)/1.8
return temp_in_celsius


def to_farenheit(temperature: float) -> float:
   temp_in_farenheit = temperature*1.8 + 32
return temp_in_farenheit


def main() -> None:
    print(f"La racine carré de 144 est : {square_root(144)}")

    print(f"Le carré de 12 est : {square(12)}")

    print(f"Moyenne des nombres 2, 4, 6: {average(2, 4, 6)}")

    print(f"Conversion de 100 degres, 2 minutes et 45 secondes en radians: {to_radians(180, 2, 45)}")
    
    degrees, minutes, seconds = to_degrees(1.0)
    print(f"Conversion de 1 radian en degres: {degrees} degres, {minutes} minutes et {seconds} secondes")

    print(f"Conversion de 100 Celsius en Farenheit: {to_farenheit(100.0)}")
    print(f"Conversion de 451 Farenheit en Celsius: {to_celsius(451.0)}")


if __name__ == '__main__':
    main()
