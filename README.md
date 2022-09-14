# PDF Intercalate

## Intercalate

Merges scans of front and back pages into one document:

```
$ pipenv run intercalate --front front.pdf --back back.pdf [--reverse] --out output.pdf
```

The optional `--reverse` parameter indicates that the back pages are in reverse
order relative to the front pages.  This allows the tool to accept scans where
the front pages are all scanned in a stack, then flipped as a stack to scan the
back pages (using an automatic document feeder).

## Stitch

Merges scans of pages batches of pages into a contiguous sequence.

```
$ pipenv run stitch first.pdf --flip second.pdf --out output.pdf
```

The optional per file `--flip` parameter indicates that the pages from that file
should be flipped (rotated by 180 degrees) in the output.

## Set-up

This package uses [pipenv](https://pipenv.pypa.io/) to manage dependencies.  To
install it, the package's dependencies, and run the script, do the following:

```
$ python3 -m pip install --user pipenv
$ pipenv install
$ pipenv run intercalate --help
```
