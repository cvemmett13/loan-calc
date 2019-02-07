'''
Program: Loan Calculator
Author: Charlie Emmett
Purpose: To calculate how long one will have to pay off a loan at a user given amount or how much the payments will be to pay off a loan in a given amount of time
Date Started: 1/23/2019
Date Last Edited: 1/31/2019


TODO

add part for interest
    will need to loop through all ipmt and add them up
'''

import numpy as np
import warnings

# declare constants
period = 12         # number of payments per year

# begin loop

warnings.filterwarnings('error')

while 1 == 1:
    
    # Determine what output the user wants

    output_type = (input('\nDo you want to calculate the time(1) or the payment amount(2)? Please enter the corresponding number.'))

    # verify that the user gave good data
    if (output_type == '1') or  (output_type == '2'):

        pass

    else:
        
        print("I'm sorry that is not an accepted input")

        continue

    # collect the principle amount from the user
    
    principle = float(input('What is the total principle amount of your loan, in dollars?'))

    # collect the interest rate from the user

    rate = float(input('What is the interest rate of your loan, in decimal form?'))

    # convert rate to interest per period

    rate = rate/period
    
    #Begin the if statement

    # if user desires a time output

    if output_type == '1':
        
        pmt = float(input('What are your desired monthly payments, in dollars?'))
        
        # Calculate the time
        try:
            
            time = np.nper(rate, -pmt, principle)

        except RuntimeWarning:

            print("Your inputted payments do not cover your interest. You would never pay off the loan at that rate.")

            continue
        
        
        #print time to the console
        
        print('You have ' + str(format(time, '.2f')) + ' payments to make. \nThat is approximately ' + str(format(time/period, '.2f')) + ' years.')

    # if user desires a payment amount output
    
    elif output_type == '2':
        
        time = float(input('How many months will you be making payments?'))

        #calculate the payments

        pmt = -(np.pmt(rate,time,principle))
        
        #print pmt to the console

        print('Your payments will be $' + str(format(pmt,'.2f')) + ' per month.')

    # ask the user if they want to use the app again

    repeat = input("Do you want to perform another calculation? Please type 'yes' or 'no'.")

    # if statement to break loop

    if repeat == 'no':

        break
