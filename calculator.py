import json
import sys

from calculator.calc import main_calculator


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python main.py path/to/input.json')
        exit(1)

    json_path = sys.argv[1]

    try:
        with open(json_path) as f:
            data = json.load(f)
            main_calculator(data)
    except IOError:
        print(f'File not accessible: {json_path}')
        exit(1)
