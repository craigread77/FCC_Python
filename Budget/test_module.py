class Category:
    def __init__(self, title):
        self.title = title
        self.ledger = []
        self.balance = 0
        self.total_spend = 0
    def __str__(self):
        out_str = ''
        out_str += str('*' * int(((30 - len(self.title)) // 2)) + self.title).ljust(30, '*') + "\n"
        for record in self.ledger:
            out_str += record["description"][:23].ljust(23, ' ') + "{:.2f}".format(record["amount"]).rjust(7, ' ') + "\n"
        out_str += "Total: {:.2f}".format(self.balance)
            
        return out_str

    def deposit(self, amount, description=''):
        amount = round(float(amount), 2)
        self.balance += amount
        self.ledger.append({"amount":amount, "description": description})

    def withdraw(self, amount, description=''):
        amount = round(float(amount), 2)
        if self.check_funds(amount):
            self.balance -= amount
            self.ledger.append({"amount":0 - amount, "description": description})
            self.total_spend += amount
            return True
        else:
            return False
    
    def get_balance(self):
        return self.balance
    
    def transfer(self, amount, target):
        if self.check_funds(amount):
            self.withdraw(amount, "Transfer to {}".format(target.title))
            target.deposit(amount, "Transfer from {}".format(self.title))
            return True
        else:
            return False

    def check_funds(self, amount):
        return self.balance >= round(float(amount), 2)
    



def create_spend_chart(categories):
    header = "Percentage spent by category"
    lines = {}
    out_str = ""

    for i in range(100, -10, -10):
        lines[i] = str(i).rjust(3, ' ') + "| "

    spending_percentages = {}
    grand_total = 0

    for x in categories:
        grand_total += x.total_spend
    
    for y in categories:
        percent = (y.total_spend * 100 / grand_total)
        #rounded = round(percent/10)*10
        spending_percentages[y.title] = percent

    for line in lines:
        for c in categories:
            if spending_percentages[c.title] >= int(line):
                lines[line] += 'o  '
            else:
                lines[line] += '   '

    titles = [c.title for c in categories]
    max_len = max(map(len, titles))
        

    out_str += header + "\n"
    out_str += "\n".join(lines.values()) + "\n"
    out_str += "    " + "-" * ((len(categories) * 3) + 1) + "\n"

    for i in range(0, max_len):
        out_str += "    "
        for title in titles:
            out_str += " "
            if len(title) > i:
                out_str += title[i]
            else:
                out_str += " "
            out_str += " "
        
        out_str += "\n"

    
    return out_str

    
    