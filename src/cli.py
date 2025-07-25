import argparse


def parse_args():
    """ python -m src.main --file=data/sample.csv --mode=total """
    parser = argparse.ArgumentParser(description="Budget Calculator")

    parser.add_argument(
        "--file",
        type=str,
        required=True,
        help="Путь к CSV файлу",
    )

    parser.add_argument(
        "--mode",
        type=str,
        required=True,
        choices=["total", "average"],
        help="Тип анализа: total, average",
    )

    return parser.parse_args()


if __name__ == '__main__':
    print("Привет из модуля cli1")
    print("Привет из модуля cli2")

