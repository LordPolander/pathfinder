from ezodf import opendoc, Sheet
doc = opendoc('xcl.ods')
for sheet in doc.sheets:
   print(sheet.name)
   cell = sheet['A1']
   sheet['A1'].set_value('player name')
   print(cell.value)
   print(cell.value_type)
   doc.saveas('xcl_edited.ods')