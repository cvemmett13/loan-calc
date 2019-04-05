import numpy as np
import tkinter as t
import warnings
import tkinter.messagebox

class LoanCalculatorGUI:

    def __init__(self):

        # create the main window
        self.main_window = t.Tk()

        # row 0 widgets
        self.principle_label = t.Label(self.main_window, text = 'Principle')
        self.principle_label.grid(row = 0, column = 0)
        self.principle_entry = t.Entry(self.main_window, width = 10)
        self.principle_entry.grid(row = 0, column = 1)

        # row 1 widgets
        self.calc_time = t.StringVar()

        self.radio_var = t.IntVar()

        self.radio_var.set(0)
        
        self.interest_label = t.Label(self.main_window, text = 'Interest Rate')
        self.interest_label.grid(row = 1, column = 0)

        self.interest_entry = t.Entry(self.main_window, width = 10)
        self.interest_entry.grid(row = 1, column = 1)

        self.time_rb = t.Radiobutton(self.main_window, variable = self.radio_var, value = 0)
        self.time_rb.grid(row = 1, column = 2)

        self.time_label_0 = t.Label(self.main_window, text = 'Calculated Time')
        self.time_label_0.grid(row = 1, column = 3)

        self.time_label_1 = t.Label(self.main_window, textvariable = self.calc_time)
        self.time_label_1.grid(row = 1, column = 4)

        # row 2 widgets
        self.calc_payment = t.StringVar()

        self.time_label = t.Label(self.main_window, text = 'Time')
        self.time_label.grid(row = 2, column = 0)

        self.time_entry = t.Entry(self.main_window, width = 10)
        self.time_entry.grid(row = 2, column = 1)

        self.payment_rb = t.Radiobutton(self.main_window, variable = self.radio_var, value = 1)
        self.payment_rb.grid(row = 2, column = 2)

        self.payment_label_0 = t.Label(self.main_window, text = 'Calculated Payment')
        self.payment_label_0.grid(row = 2, column = 3)

        self.payment_label_1 = t.Label(self.main_window, textvariable = self.calc_payment)
        self.payment_label_1.grid(row = 2, column = 4)

        # row 3 widgets                                                                                   
        self.payment_label = t.Label(self.main_window, text = 'Payments')
        self.payment_label.grid(row = 3, column = 0)

        self.payment_entry = t.Entry(self.main_window, width = 10)
        self.payment_entry.grid(row = 3, column = 1)

        # row 4 widgets
        self.calculate_button = t.Button(self.main_window, text = 'Calculate',
                                         command = self.calculate)
        self.calculate_button.grid(row = 4, column = 0)

        self.clear_button = t.Button(self.main_window, text = 'Clear',
                                     command = self.clear)
        self.clear_button.grid(row = 4, column = 1)

        self.quit_button = t.Button(self.main_window, text = 'Quit',
                                    command = self.main_window.destroy)
        self.quit_button.grid(row = 4, column = 2)

        t.mainloop()

    def calculate(self):

        warnings.filterwarnings('error')

        self.calc_payment.set(0)

        self.calc_time.set(0)

        principle = float(self.principle_entry.get())

        rate = float(self.interest_entry.get())

        rate = rate/12

        if self.radio_var.get() == 0:

            if self.payment_entry.get() == '':
                t.messagebox.showinfo('Error', 'You have not entered the correct information for your desired output.')

            
            else:

                payment = float(self.payment_entry.get())

                try:
                
                    time = np.nper(rate, -payment, principle)

                except RuntimeWarning:

                    self.error()

                    time = 0
                    
                self.calc_time.set(round(float(time),2))
        
        elif self.radio_var.get() == 1:

            if self.time_entry.get() == '':
                t.messagebox.showinfo('Error', 'You have not entered the correct information for your desired output.')

            else:
                time = float(self.time_entry.get())

                payment = -(np.pmt(rate,time,principle))

                self.calc_payment.set(round(float(payment),2))


    # Error message box

    def error(self):

        t.messagebox.showinfo('Error', 'Your inputted payments do not cover your\
                                    interest. The loan would never be paid off.')

    # clear function

    def clear(self):

        self.calc_payment.set(0)

        self.calc_time.set(0)

        self.principle_entry.delete(0, 'end')

        self.interest_entry.delete(0, 'end')

        self.time_entry.delete(0, 'end')

        self.payment_entry.delete(0, 'end')

loan_calc = LoanCalculatorGUI()
