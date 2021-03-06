# coding: utf-8
from __future__ import (
    absolute_import, division, print_function, unicode_literals)
from operator import itemgetter

# example to convert:
# csv2ofx -m rabobank -E ISO-8859-1 CSV_O_20200630_014400.csv CSV_O_20200630_014400.ofx

def date_func(trxn):
    tag = trxn['Datum']
    tag = tag.split('-')

    return '{}/{}/{}'.format(tag[1], tag[2], tag[0])

mapping = {
    'has_header': True,
    'currency': itemgetter('Munt'),
    # 'delimiter': ';',
    'bank': 'Rabobank',
    'account': itemgetter('IBAN/BBAN'),
    'id': itemgetter('Volgnr'),
    'date': date_func,
    'amount': lambda r: r['Bedrag'].replace(',', '.'),
    'desc': lambda r: '{0} - {1}'.format(r['Naam tegenpartij'],
                                         ' '.join(r['Omschrijving-{}'.format(n)] for n in range(1, 4))),
    'payee': itemgetter('Naam tegenpartij'),
}
