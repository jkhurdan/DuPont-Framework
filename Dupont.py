#This is a file to determine the DuPoint values of a Balance sheet

print(""" This program is designed to help you calculate the Dupont Framework.
    
    Select an option from below:
    1. Return on Equity
    2. Profitability (Profit Margin)
    3. Efficency (Asset Turn Over)
    4. Leverage """ 
    )

MenuOption = int(input("Menu Option: "))

if MenuOption == 1:
    print("""
    Return on Equity shows the return that a business generated during a period
    on the equity invested in the business by the owners of the business. 
    
    Return on equity is calculated by dividing net income by total onwers 
    equity. While this is a useful measure of financial performance of a firm, 
    it can be broken down further to reveal where the returns are being 
    generated (and where you can improve)""")

    Profit_Margin = float(input("Please enter your profit margin: "))
    Efficency = float(input("Please enter your Asset Turn Over: "))
    Leverage = float(input("Please enter your leverage: "))

    print("Return of Equity =" + "{:.2%}".format(Profit_Margin * Efficency * Leverage))
elif MenuOption == 2:
    print("""
    Profitability reveals how much profit is left from each dollar of sales after all
    expenses have been subtracted.""")

    Net_income = float(input("Please enter your net income: "))
    Sales = float(input("Please enter your total sales: "))

    print("\n Profit Margin = " + "{:.2%}".format(Net_income/Sales))
    
    print(""" \n To calculate further profitability ratio's select from the menu below:
        1. Gross Profit Margin
        2. Earnings before interest after taxes (EBIAT) -in progress """)
    Profitability_ratios_menu = int(input("select an option from above: "))
    if Profitability_ratios_menu == 1:
        print(""" Gross Profit Margin tells us what percentage of renvue is left to cover
        other expenses after the costs of goods sold is subtracted """)
        Gross_Profit = float(input("Gross Profit: "))
        print("\n Gross Profit Margin = " + "{:.2%}".format(Gross_Profit / Sales ))
    elif Profitability_ratios_menu == 2:
        print(""" 
        Earnings before interest after tax (EBIAT) is a measure of how much income the business
        has generated while ignoring the effects of financing and captial structure, or
        the proportion of debt that the business has.""")

        #Come back to me 
elif MenuOption == 3:
    print("""Asset Turnover tells us how well a business is using its assets to produce sales """ ) 

    Sales = float(input("Please enter your total sales: "))
    Assets = float(input("Please enter the toal value of your assets: "))

    print("\n Asset Turn Over = " + "{:.2%}".format(Sales/Assets))

elif MenuOption == 4:
    print(""" Leverage ratios is also known as the equity multiplier. This measures the impact of
    all non-equity financing, or debt of all sorts, on the firm's ROE.""")

    Average_Total_Assets = float(input("Enter your Average total assets: "))
    Average_Equity = float(input("Enter your average Equity: "))

    print("\n Leverage = ", Average_Total_Assets / Average_Equity)


