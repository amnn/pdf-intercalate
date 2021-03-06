# PDF Intercalate

Merges scans of front and back pages into one document:

```
$ ./intercalate --front front.pdf --back back.pdf [--reverse] --out output.pdf
```

The optional `--reverse` parameter indicates that the back pages are in reverse
order relative to the front pages.  This allows the tool to accept scans where
the front pages are all scanned in a stack, then flipped as a stack to scan the
back pages (using an automatic document feeder).

## Set-up

This package uses [pipenv](https://pipenv.pypa.io/) to manage dependencies.  To
install it, the package's dependencies, and run the script, do the following:

```
$ python3 -m pip install --user pipenv
$ pipenv install
$ pipenv run intercalate --help
```
