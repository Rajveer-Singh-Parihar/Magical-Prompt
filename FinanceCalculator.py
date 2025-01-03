import tkinter as tk
from tkinter import ttk
import math

class FinanceCalculator:
    def __init__(self, root):
        self.root = root
        root.title("Finance Calculator")
        root.geometry("400x600")
        
        # Style configuration
        style = ttk.Style()
        style.configure('TButton', padding=5)
        style.configure('TLabel', padding=3)
        style.configure('TEntry', padding=3)
        
        # Create notebook for different calculators
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(pady=10, expand=True, fill="both")
        
        # Create tabs
        self.loan_frame = ttk.Frame(self.notebook)
        self.investment_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.loan_frame, text="Loan Calculator")
        self.notebook.add(self.investment_frame, text="Investment Calculator")
        
        self.setup_loan_calculator()
        self.setup_investment_calculator()
    
    def setup_loan_calculator(self):
        # Loan calculator inputs
        ttk.Label(self.loan_frame, text="Loan Amount ($):").pack(pady=5)
        self.loan_amount = ttk.Entry(self.loan_frame)
        self.loan_amount.pack(pady=5)
        
        ttk.Label(self.loan_frame, text="Annual Interest Rate (%):").pack(pady=5)
        self.loan_rate = ttk.Entry(self.loan_frame)
        self.loan_rate.pack(pady=5)
        
        ttk.Label(self.loan_frame, text="Loan Term (years):").pack(pady=5)
        self.loan_term = ttk.Entry(self.loan_frame)
        self.loan_term.pack(pady=5)
        
        ttk.Button(self.loan_frame, text="Calculate Monthly Payment", 
                  command=self.calculate_loan).pack(pady=15)
        
        self.loan_result = ttk.Label(self.loan_frame, text="")
        self.loan_result.pack(pady=10)
    
    def setup_investment_calculator(self):
        # Investment calculator inputs
        ttk.Label(self.investment_frame, text="Initial Investment ($):").pack(pady=5)
        self.investment_principal = ttk.Entry(self.investment_frame)
        self.investment_principal.pack(pady=5)
        
        ttk.Label(self.investment_frame, text="Annual Return Rate (%):").pack(pady=5)
        self.investment_rate = ttk.Entry(self.investment_frame)
        self.investment_rate.pack(pady=5)
        
        ttk.Label(self.investment_frame, text="Time Period (years):").pack(pady=5)
        self.investment_time = ttk.Entry(self.investment_frame)
        self.investment_time.pack(pady=5)
        
        ttk.Label(self.investment_frame, text="Monthly Contribution ($):").pack(pady=5)
        self.monthly_contribution = ttk.Entry(self.investment_frame)
        self.monthly_contribution.pack(pady=5)
        
        ttk.Button(self.investment_frame, text="Calculate Future Value", 
                  command=self.calculate_investment).pack(pady=15)
        
        self.investment_result = ttk.Label(self.investment_frame, text="")
        self.investment_result.pack(pady=10)
    
    def calculate_loan(self):
        try:
            P = float(self.loan_amount.get())
            r = float(self.loan_rate.get()) / 100 / 12  # Monthly interest rate
            n = float(self.loan_term.get()) * 12  # Total number of months
            
            # Monthly payment formula: PMT = P * (r(1+r)^n) / ((1+r)^n - 1)
            monthly_payment = P * (r * (1 + r)**n) / ((1 + r)**n - 1)
            total_payment = monthly_payment * n
            
            result_text = f"Monthly Payment: ${monthly_payment:.2f}\n"
            result_text += f"Total Payment: ${total_payment:.2f}"
            self.loan_result.config(text=result_text)
            
        except ValueError:
            self.loan_result.config(text="Please enter valid numbers")
    
    def calculate_investment(self):
        try:
            P = float(self.investment_principal.get())
            r = float(self.investment_rate.get()) / 100
            t = float(self.investment_time.get())
            PMT = float(self.monthly_contribution.get())
            
            # Future value formula with monthly contributions
            months = t * 12
            monthly_rate = r / 12
            
            future_value = P * (1 + r)**t
            
            # Add future value of monthly contributions
            if PMT > 0:
                future_value += PMT * ((1 + monthly_rate)**(months) - 1) / monthly_rate
            
            total_invested = P + (PMT * 12 * t)
            gains = future_value - total_invested
            
            result_text = f"Future Value: ${future_value:.2f}\n"
            result_text += f"Total Invested: ${total_invested:.2f}\n"
            result_text += f"Total Gains: ${gains:.2f}"
            self.investment_result.config(text=result_text)
            
        except ValueError:
            self.investment_result.config(text="Please enter valid numbers")

if __name__ == "__main__":
    root = tk.Tk()
    app = FinanceCalculator(root)
    root.mainloop()