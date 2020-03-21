from .settings import (
    DEFAULT_AMOUNT,
    DEFAULT_COMMISSION_METHOD,
    DEFAULT_COMMISSION_RATE,
    DEFAULT_INSTALLMENT_METHOD,
    DEFAULT_INTEREST_RATE,
    DEFAULT_TERM_IN_MONTHS,
    SIMULATION_HEADER,
    SIMULATION_OUTPUT_FORMAT,
    SUMMARY_OUTPUT_FORMAT,
)


def simulation_equal(amount, term_in_months, interest_rate):
    installment = amount * interest_rate / (12 * (1 - (12 / (12 + interest_rate)) ** term_in_months))

    for i in range(term_in_months):
        new_amount = amount * (1 + (interest_rate / 12))
        print(SIMULATION_OUTPUT_FORMAT.format((i + 1), amount, new_amount - amount, installment - new_amount + amount, installment))
        new_amount -= installment
        amount = new_amount

    return installment * term_in_months


def simulation_decreasing(amount, term_in_months, interest_rate):
    start_amount = amount
    full_amount = 0.

    for i in range(term_in_months):
        new_amount = amount * (1 + (interest_rate / 12))
        installment = new_amount - amount + (start_amount / term_in_months)
        full_amount += installment
        print(SIMULATION_OUTPUT_FORMAT.format((i + 1), amount, new_amount - amount, installment - new_amount + amount, installment))
        new_amount -= installment
        amount = new_amount

    return full_amount


def parse_input(json_data: dict):
    amount = json_data.get('amount', DEFAULT_AMOUNT)
    term_in_months = json_data.get('term_in_months', DEFAULT_TERM_IN_MONTHS)
    interest_rate = json_data.get('interest_rate', DEFAULT_INTEREST_RATE)
    installment_method = json_data.get('installment_method', DEFAULT_INSTALLMENT_METHOD)
    commission_rate = json_data.get('commission_rate', DEFAULT_COMMISSION_RATE)
    commission_method = json_data.get('commission_method', DEFAULT_COMMISSION_METHOD)

    return amount, term_in_months, interest_rate, installment_method, commission_rate, commission_method


def handle_commission(amount, commission_rate, commission_method):
    amount_to_be_paid = amount
    commission_amount = amount * commission_rate

    if commission_method == 'increases_amount':
        amount += commission_amount
    elif commission_method == 'decreases_amount':
        amount_to_be_paid -= commission_amount
    else:  # not include
        pass

    return amount, amount_to_be_paid


def main_calculator(json_data: dict):
    amount, term_in_months, interest_rate, installment_method, commission_rate, commission_method = parse_input(json_data)
    amount, amount_to_be_paid = handle_commission(amount, commission_method, commission_rate)

    print(SIMULATION_HEADER)

    if installment_method == 'fixed':
        full_amount = simulation_equal(amount, term_in_months, interest_rate)
    else:
        full_amount = simulation_decreasing(amount, term_in_months, interest_rate)

    print(SUMMARY_OUTPUT_FORMAT.format(amount, amount_to_be_paid, full_amount))
