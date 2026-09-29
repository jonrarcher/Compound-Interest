# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 09:06:46 2026

@author: jonsu
"""
# This program calculates compound interest

def main():
    print('Welcome! This program calculates the compound interest of an investment')
    principal = float(input('\nPlease enter your principal. '))
    rate = float(input('Enter your interest rate '))
    time = float(input('Enter the number of years for your investment '))
    Total = (principal*(1+rate)**time)
    interest_earned = Total - principal
    print('\nYour total value will be', round(Total,2))
    print('\nYour interest earned is', round(interest_earned,2))

main()

    
