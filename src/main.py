from src.cli import parse_args
from src.models import Budget
import sys


def main():
    args = parse_args()

    try:
        predictor = Budget.from_csv(args.file)
    except FileNotFoundError:
        print("File not found")
        sys.exit(1)

    try:
        if args.mode == "total":
            res = predictor.total
        elif args.mode == "average":
            res = predictor.average
        else:
            res = None
        print(f" Результат {args.mode} {res}")

    except Exception as e:
        print(f"Ошибка {e}")


if __name__ == '__main__':
    main()
