import argparse
from pdfrw import PdfReader, PdfWriter

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

    front = PdfReader(args.front).pages
    back = PdfReader(args.back).pages

    assert len(front) == len(back), \
        "FRONT and BACK must contain the same number of pages"

    if args.reverse:
        back = reversed(back)

    out = PdfWriter()
    for pair in zip(front, back):
        out.addpages(pair)
    out.write(args.out)
