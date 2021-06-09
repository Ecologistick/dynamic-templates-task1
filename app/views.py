from django.shortcuts import render
from app.settings import INFLATION_CSV

import csv


def inflation_view(request):
    template_name = 'inflation.html'
    data = []
    with open(INFLATION_CSV, newline='', encoding="utf-8") as isfile:
        reader = csv.reader(isfile)
        first_line = next(reader)[0].split(sep=';')
        for row in reader:
            row = row[0].split(sep=';')
            row_new = []
            for r in row:
                if r == row[0]:
                    r = int(r)
                elif r != '':
                    r = float(r)
                row_new.append(r)
            data.append(row_new)

    context = {
        'headers': first_line,
        'inflations': data
    }

    return render(request, template_name,
                  context)
