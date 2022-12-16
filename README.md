# svg-to-json

Transform SVG files to JSON notation.

## Usage

```bash
python svg-to-json.py [input] [output]
```

## Output

```json
[
  {
    "viewBox": "0 0 24 24",
    "height": "24",
    "width": "24",
    "fill": "none",
    "objects": [
      {
        "d": "M9 11C11.2091 11 13 9.20914 13 7C13 4.79086 11.2091 3 9 3C6.79086 3 5 4.79086 5 7C5 9.20914 6.79086 11 9 11Z",
        "attributes": {
          "stroke": "#1A202C",
          "strokeWidth": "1.5",
          "strokeLinecap": "round",
          "strokeLinejoin": "round"
        }
      },
      {
        "d": "M3 21V19C3 17.9391 3.42143 16.9217 4.17157 16.1716C4.92172 15.4214 5.93913 15 7 15H11C12.0609 15 13.0783 15.4214 13.8284 16.1716C14.5786 16.9217 15 17.9391 15 19V21",
        "attributes": {
          "stroke": "#1A202C",
          "strokeWidth": "1.5",
          "strokeLinecap": "round",
          "strokeLinejoin": "round"
        }
      },
      {
        "d": "M16 3.13C16.8604 3.35031 17.623 3.85071 18.1676 4.55232C18.7122 5.25392 19.0078 6.11683 19.0078 7.005C19.0078 7.89318 18.7122 8.75608 18.1676 9.45769C17.623 10.1593 16.8604 10.6597 16 10.88",
        "attributes": {
          "stroke": "#1A202C",
          "strokeWidth": "1.5",
          "strokeLinecap": "round",
          "strokeLinejoin": "round"
        }
      },
      {
        "d": "M21 21V19C20.9949 18.1172 20.6979 17.2608 20.1553 16.5644C19.6126 15.868 18.8548 15.3707 18 15.15",
        "attributes": {
          "stroke": "#1A202C",
          "strokeWidth": "1.5",
          "strokeLinecap": "round",
          "strokeLinejoin": "round"
        }
      }
    ]
  }
]
```

## License

The MIT License (MIT)

Copyright (c) 2022 Alexander Shelepenok

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
