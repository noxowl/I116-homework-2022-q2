#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Fundamentals of Programming (Nao Hirokawa)
Term 1-2(Q2), 2022
Lecture 4

@Author: RHIE Suyeong(2250008. M.Phil. Student in Transdisciplinary Sciences)
"""

# The data was taken from the following webpage:
#   http://www.data.jma.go.jp/obd/stats/etrn/view/monthly_s3.php?prec_no=44&block_no=47662
tokyo_records = [
    (2000, [7.6, 6.0, 9.4, 14.5, 19.8, 22.5, 27.7, 28.3, 25.6, 18.8, 13.3, 8.8]),
    (2001, [4.9, 6.6, 9.8, 15.7, 19.5, 23.1, 28.5, 26.4, 23.2, 18.7, 13.1, 8.4]),
    (2002, [7.4, 7.9, 12.2, 16.1, 18.4, 21.6, 28.0, 28.0, 23.1, 19.0, 11.6, 7.2]),
    (2003, [5.5, 6.4, 8.7, 15.1, 18.8, 23.2, 22.8, 26.0, 24.2, 17.8, 14.4, 9.2]),
    (2004, [6.3, 8.5, 9.8, 16.4, 19.6, 23.7, 28.5, 27.2, 25.1, 17.5, 15.6, 9.9]),
    (2005, [6.1, 6.2, 9.0, 15.1, 17.7, 23.2, 25.6, 28.1, 24.7, 19.2, 13.3, 6.4]),
    (2006, [5.1, 6.7, 9.8, 13.6, 19.0, 22.5, 25.6, 27.5, 23.5, 19.5, 14.4, 9.5]),
    (2007, [7.6, 8.6, 10.8, 13.7, 19.8, 23.2, 24.4, 29.0, 25.2, 19.0, 13.3, 9.0]),
    (2008, [5.9, 5.5, 10.7, 14.7, 18.5, 21.3, 27.0, 26.8, 24.4, 19.4, 13.1, 9.8]),
    (2009, [6.8, 7.8, 10.0, 15.7, 20.1, 22.5, 26.3, 26.6, 23.0, 19.0, 13.5, 9.0]),
    (2010, [7.0, 6.5, 9.1, 12.4, 19.0, 23.6, 28.0, 29.6, 25.1, 18.9, 13.5, 9.9]),
    (2011, [5.1, 7.0, 8.1, 14.5, 18.5, 22.8, 27.3, 27.5, 25.1, 19.5, 14.9, 7.5]),
    (2012, [4.8, 5.4, 8.8, 14.5, 19.6, 21.4, 26.4, 29.1, 26.2, 19.4, 12.7, 7.3]),
    (2013, [5.5, 6.2, 12.1, 15.2, 19.8, 22.9, 27.3, 29.2, 25.2, 19.8, 13.5, 8.3]),
    (2014, [6.3, 5.9, 10.4, 15.0, 20.3, 23.4, 26.8, 27.7, 23.2, 19.1, 14.2, 6.7]),
    (2015, [5.8, 5.7, 10.3, 14.5, 21.1, 22.1, 26.2, 26.7, 22.6, 18.4, 13.9, 9.3]),
    (2016, [6.1, 7.2, 10.1, 15.4, 20.2, 22.4, 25.4, 27.1, 24.4, 18.7, 11.4, 8.9]),
    (2017, [5.8, 6.9, 8.5, 14.7, 20.0, 22.0, 27.3, 26.4, 22.8, 16.8, 11.9, 6.6])]


class HTMLGenerator:
    def __init__(self):
        self.payload = []

    def _header(self):
        self.payload.append("<!DOCTYPE html>")
        self.payload.append("<head>")
        self._css()
        self.payload.append("</head>")

    def _css(self):
        self.payload.append("<style>")
        self.payload.append("table.temperature_table { border-top: 1px solid; border-bottom: 1px solid;}")
        self.payload.append("table.temperature_table tr>td.cold { background: #aaf;} /* -10 */")
        self.payload.append("table.temperature_table tr>td.cool { background: #ccf;} /* 10-15 */")
        self.payload.append("table.temperature_table tr>td.mild { background: #fef;} /* 15-20 */")
        self.payload.append("table.temperature_table tr>td.warm { background: #fcc;} /* 20-25 */")
        self.payload.append("table.temperature_table tr>td.hot { background: #faa;} /* 25- */")
        self.payload.append("</style>")

    def _body(self):
        self.payload.append("<body>")
        self.payload.append("<h1>Temperatures in Tokyo</h1>")

    def _cell_class(self, temperature):
        result = ''
        if 25 <= temperature < 50:
            result = 'hot'
        elif 20 <= temperature < 25:
            result = 'warm'
        elif 15 <= temperature < 20:
            result = 'mild'
        elif 10 <= temperature < 15:
            result = 'cool'
        elif -50 <= temperature < 10:
            result = 'cold'
        return result

    def _table(self, records: list):
        self.payload.append('<table class="temperature_table">')
        self.payload.append("<tr>")
        self.payload.append("<th>-</th>")
        for i in range(len(records[0][1])):
            self.payload.append(f"<th>{i + 1}</th>")
        self.payload.append("</tr>")
        for r in records:
            self._table_contents(r[0], r[1])
        self.payload.append("</tr>")
        self.payload.append("</table>")

    def _table_contents(self, row_title, items: list):
        self.payload.append("<tr>")
        self.payload.append(f"<td>{row_title}</td>")
        for i in items:
            self.payload.append(f'<td class="temperature_table {self._cell_class(i)}">{i}</td>')

    def _footer(self):
        self.payload.append("</body>")
        self.payload.append("</html>")

    def generate(self, records):
        self._header()
        self._body()
        self._table(records)
        self._footer()
        for p in self.payload:
            print(p)


def table_test():
    """
    HTML Generation

    python l4.py > table.html
    """
    generator = HTMLGenerator()
    generator.generate(tokyo_records)


table_test()
