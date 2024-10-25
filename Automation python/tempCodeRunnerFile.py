import camelot
tables = camelot.read_pdf('foo.pdf', pages='1')
print(tables)