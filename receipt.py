import datetime

def generate(cart, total, pay_method):
    with open("receipt.txt", "w") as file:
        file.write("="*40 + "\n")
        file.write("       🛒 TAJ MINI MART RECEIPT\n")
        file.write("="*40 + "\n")

        now = datetime.datetime.now()
        file.write(f"Date: {now.strftime('%Y-%m-%d %H:%M:%S')}\n")
        file.write("-"*40 + "\n")
        file.write(f"{'Item':10} {'Qty':>3} {'Rate':>6} {'Total':>7}\n")
        file.write("-
