# FinTech Calculator
A calculator for different types of mortgage loans, created for FinTech classes 2020.
## Usage
To use calculator, type in bash console:
```bash
python calculator.py path/to/input.json
```
### Input format
Calculator accepts input in `json`. Example:
```json
{
  "amount": 500000,
  "term_in_months": 300,
  "interest_rate": 0.037,
  "installment_method": "fixed",
  "commission_method": "not_include"
}
```
There are 6 possible arguments:
* `amount` - float
* `term_in_months` - integer
* `interest_rate` - float
* `installment_method` - `fixed` or `decreasing`
* `commission_method` - `not_include` or `increases_amount` or `decreases_amount`
* `commission_rate` - float

Each argument, if not provided, has default value. Default values are as follows:
```json
{
  "amount": 200000,
  "term_in_months": 240,
  "interest_rate": 0.05,
  "installment_method": "fixed",
  "commission_method": "not_include",
  "commission_rate": 0.015
}
