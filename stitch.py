from os import path
from pdfrw import PdfReader, PdfWriter
import sys
from typing import List, NamedTuple


class Args(NamedTuple):
    out: str
    pdfs: List[str]


def print_usage(prog):
    print(
        (
            f"usage: {prog} [-h] --out OUT [[--flip] PDF ...]\n\n"
            "Stitch together pages from consecutive PDF files.\n\n"
            "opions:\n"
            "  -h, --help            show this help message and exit\n"
            "  -O, --out             PDF to output to\n"
            "  PDF                   Add the pages from this PDF file.\n"
            "  --flip PDF, -F flip   Add the pages from this PDF file, rotated 180 degrees.\n"
        ),
        file=sys.stderr,
    )


def parse_args():
    args = iter(sys.argv)
    prog = path.basename(next(args))

    out  = None
    pdfs = []
    for arg in args:
        if arg in ("-h", "--help"):
            print_usage(prog)
            exit(0)
        elif arg in ("-O", "--out"):
            out = next(args)
        elif arg in ("-F", "--flip"):
            pdfs.append((180, next(args)))
        else:
            pdfs.append((0, arg))

    if out is None:
        print(f"{prog}: error: --out/-O is a required argument.", file=sys.stderr)
        exit(1)

    return Args(out, pdfs)


if __name__ == "__main__":
    args = parse_args()
    out  = PdfWriter()
    for angle, file in args.pdfs:
        pdf = PdfReader(file)
        for page in pdf.pages:
            page.Rotate = (int(page.inheritable.Rotate or 0) + angle) % 360
            out.addpage(page)

    out.write(args.out)
