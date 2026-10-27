"""
Day 21 - 2026-10-27
Tool: Loan EMI Calculator
What it does: Works out the fixed monthly payment (EMI) for a loan
from the amount, yearly interest rate and number of years, plus the
total paid and total interest - so a loan offer is easy to judge.
Who it helps: Anyone taking a bank, bike or personal loan who wants
to know the real monthly cost before signing anything.
"""


def monthly_emi(principal, yearly_rate_percent, years):
    """Standard EMI formula. A 0% loan is just split evenly."""
    if principal <= 0 or years <= 0:
        raise ValueError("Principal and years must be positive.")
    months = int(years * 12)
    monthly_rate = yearly_rate_percent / 100 / 12
    if monthly_rate == 0:
        return round(principal / months, 2)
    factor = (1 + monthly_rate) ** months
    return round(principal * monthly_rate * factor / (factor - 1), 2)


def loan_summary(principal, yearly_rate_percent, years):
    months = int(years * 12)
    emi = monthly_emi(principal, yearly_rate_percent, years)
    total = round(emi * months, 2)
    return {"months": months, "emi": emi, "total_paid": total,
            "total_interest": round(total - principal, 2)}


if __name__ == "__main__":
    summary = loan_summary(200000, 9, 3)
    print("Loan: 200000 taka at 9% for 3 years")
    print("Monthly EMI:", summary["emi"], "taka")
    print("Total paid:", summary["total_paid"], "taka")
    print("Total interest:", summary["total_interest"], "taka")
    print("Zero-interest check (12000 taka, 1 year):",
          monthly_emi(12000, 0, 1), "taka/month")
