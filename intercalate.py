import argparse

parser = argparse.ArgumentParser(
    description="Merges scans of front and back pages into one document"
)

parser.add_argument(
    '--front', '-F',
    type=str,
    required=True,
    help='PDF containing front pages',
)

parser.add_argument(
    '--back', '-B',
    type=str,
    required=True,
    help='PDF containing back pages (must contain same number of pages as FRONT)',
)

parser.add_argument(
    '--out', '-O',
    type=str,
    required=True,
    help='PDF to output to',
)

parser.add_argument(
    '--reverse', '-R',
    action='store_true',
    help="Whether pages in BACK are reversed relative to FRONT.",
)

if __name__ == "__main__":
    args = parser.parse_args()
    print("Hello, world")
