# Python-QR-Dump

A Python script that reads images containing QR codes and outputs the decoded
values as CSV.

## Requirements

* [PIL](https://pypi.python.org/pypi/PIL)
* [ZBar](https://pypi.python.org/pypi/zbar)

## Usage Example

```bash
python qr-dump.py -p images -o output.csv
```

Where "images" is a directory containing image files you intend to read QR code
data from.

