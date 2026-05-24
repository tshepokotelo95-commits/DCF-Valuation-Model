import numpy as np

def run_dcf_valuation(
    initial_revenue: float,
    revenue_growth: float,
    ebitda_margin: float,
    tax_rate: float,
    capex_as_pct_rev: float,
    nwc_change_as_pct_rev: float,
    wacc: float,
    perpetual_growth_rate: float
):
    """
    Executes an institutional 5-year explicit projection DCF Model
    to derive Intrinsic Enterprise Value.
    """
    years = np.arange(1, 6)
    projected_revenue = []
    projected_fcff = []
    
    current_rev = initial_revenue
    print("--- 5-Year Corporate Financial Projections ---")
    
    for year in years:
        # 1. Income Statement Projections
        current_rev *= (1 + revenue_growth)
        ebitda = current_rev * ebitda_margin
        
        # Approximating D&A to equal Capex for template baseline stability
        da = current_rev * capex_as_pct_rev
        ebit = ebitda - da
        taxes = ebit * tax_rate
        nopat = ebit - taxes
        
        # 2. Free Cash Flow to Firm (FCFF) Derivation
        # Formula: FCFF = NOPAT + D&A - CapEx - Change in Net Working Capital
        capex = current_rev * capex_as_pct_rev
        nwc_change = current_rev * nwc_change_as_pct_rev
        fcff = nopat + da - capex - nwc_change
        
        projected_revenue.append(current_rev)
        projected_fcff.append(fcff)
        
        print(f"Year {year:d} | Revenue: ${current_rev:,.0f} | FCFF: ${fcff:,.0f}")
        
    # 3. Discounting Calculations
    discount_factors = (1 + wacc) ** years
    pv_of_fcff = np.array(projected_fcff) / discount_factors
    sum_pv_explicit_flows = np.sum(pv_of_fcff)
    
    # 4. Terminal Value Engine (Gordon Growth Method)
    terminal_year_fcff = projected_fcff[-1] * (1 + perpetual_growth_rate)
    terminal_value = terminal_year_fcff / (wacc - perpetual_growth_rate)
    pv_of_terminal_value = terminal_value / ((1 + wacc) ** 5)
    
    # 5. Enterprise Valuation Summary
    enterprise_value = sum_pv_explicit_flows + pv_of_terminal_value
    
    print("\n================ VALUATION SUMMARY ================")
    print(f"PV of Explicit Cash Flows:  ${sum_pv_explicit_flows:,.2f}")
    print(f"PV of Terminal Value:       ${pv_of_terminal_value:,.2f}")
    print(f"INTRINSIC ENTERPRISE VALUE: ${enterprise_value:,.2f}")
    print("===================================================")
    
    return enterprise_value

if __name__ == "__main__":
    print("Initializing Corporate Finance Valuation Engine...")
    # Baseline simulation run: $100M revenue business profile
    run_dcf_valuation(
        initial_revenue=100000000, 
        revenue_growth=0.07,         # 7% YoY growth
        ebitda_margin=0.22,          # 22% Operating Margin
        tax_rate=0.25,               # 25% Corporate tax
        capex_as_pct_rev=0.04,       # 4% Capital reinvestment rate
        nwc_change_as_pct_rev=0.01,  # 1% Working capital drag
        wacc=0.089,                  # 8.9% discount rate from calculator
        perpetual_growth_rate=0.02   # 2% Long-term terminal growth
    )
