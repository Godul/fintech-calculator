import json
import sys

def simulation(amount, installment, term_in_months, interest_rate):

    output_format = '{:>4} {:>10.2f} {:>10.2f} {:>10.2f} {:>10.2f}'

    for i in range(term_in_months):
        new_amount = amount * (1 + (interest_rate / 12))
        print(output_format.format((i+1), amount, new_amount - amount, installment - new_amount + amount, installment))
        new_amount -= installment
        amount = new_amount


def main_calculator(json_data):
    amount = json_data.get('amount', 200000)
    term_in_months = json_data.get('term_in_months', 240)
    interest_rate = json_data.get('interest_rate', 0.05)
    installment = amount * interest_rate / (12 * (1 - (12/(12 + interest_rate))**term_in_months))
    print('kwota kredytowana: ', amount)
    print('kwota do wypłaty: ', amount)
    print('suma spłat: ', installment * term_in_months)
    simulation(amount, installment, term_in_months, interest_rate)


if __name__ == '__main__':
    path = sys.argv[1]
    with open(path) as f:
        data = json.load(f)
        main_calculator(data)
