import numpy as np

def calculate_wacc(
    risk_free_rate: float,
    equity_beta: float,
    market_premium: float,
    cost_of_debt: float,
    market_equity: float,
    total_debt: float,
    tax_rate: float
) -> float:
    """
    Computes the Weighted Average Cost of Capital (WACC) using CAPM
    for discounting corporate Free Cash Flows.
    """
    total_capital = market_equity + total_debt
    
    # 1. Cost of Equity via Capital Asset Pricing Model (CAPM)
    cost_of_equity = risk_free_rate + (equity_beta * market_premium)
    
    # 2. After-Tax Cost of Debt (Tax Shield Effect)
    after_tax_cost_of_debt = cost_of_debt * (1 - tax_rate)
    
    # 3. Capital Structure Weights
    weight_of_equity = market_equity / total_capital
    weight_of_debt = total_debt / total_capital
    
    # 4. Blended WACC Formula
    wacc = (weight_of_equity * cost_of_equity) + (weight_of_debt * after_tax_cost_of_debt)
    
    print("---------------- WACC ENGINE OUTPUT ----------------")
    print(f"Cost of Equity (CAPM):     {cost_of_equity * 100:.2f}%")
    print(f"After-Tax Cost of Debt:    {after_tax_cost_of_debt * 100:.2f}%")
    print(f"Blended Corporate WACC:    {wacc * 100:.2f}%")
    print("----------------------------------------------------")
    
    return wacc

if __name__ == "__main__":
    # Example Baseline inputs for an institutional corporate profile
    print("Executing standalone WACC verification module...")
    calculate_wacc(
        risk_free_rate=0.045,  # 4.5% Risk-free rate
        equity_beta=1.20,      # Market beta
        market_premium=0.055,  # 5.5% Equity Risk Premium
        cost_of_debt=0.065,    # 6.5% Pre-tax Corporate Bond Yield
        market_equity=800000,  # Equity Value ($k)
        total_debt=200000,     # Debt Value ($k)
        tax_rate=0.25          # 25% Corporate Tax Rate
    )
