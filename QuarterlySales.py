def main():
    quarter_sales = []
    GetSales(quarter_sales)

def GetSales(quarter_sales):
    quarter1 = float(input("Enter sales for Q1: "))
    quarter_sales.append(quarter1)
    quarter2 = float(input("Enter sales for Q2: "))
    quarter_sales.append(quarter2)
    quarter3 = float(input("Enter sales for Q3: "))
    quarter_sales.append(quarter3)
    quarter4 = float(input("Enter sales for Q4: "))
    quarter_sales.append(quarter4)
    print(quarter_sales)
main()