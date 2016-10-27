# tsv
Tab-Separated Value library for Python

TSV file slook like this:

```
# This is an example TSV file
# It lists whether verious genes are good or not.
# Sometimes there are column headers that look like comments; we just ignore those.
# GENE	STATUS	POINTS	DATA
BRCA1	GOOD	37
BRCA2	NOT_GOOD	-100	c=5
HLA-A	VERY_GOOD	3	0,2,3,1,3,2
```

To read a TSV file, use a `TsvReader`:

```
import tsv
reader = tsv.TsvReader(open("file.tsv"))
for parts in reader:
  # Here parts is a list of strings, one per tab-separated column.
	# Make sure you handle not having enough fields, or not being able to
	# parse numbers where you expect them.
  print("Record with {} fields: {}".format(len(parts), parts))
```

To write a TSV file, use a `TsvWriter`:
```
import tsv
writer = tsv.TsvWriter(open("file.tsv", "w"))

writer.comment("This is a comment
writer.line("Column 1", "Column 2", 12345)
writer.list_line(["Column 1", "Column 2"] + list(range(10)))
writer.close()
```

Since TSV makes no provision for escaping tabs or newlines, users must not provide them within field values.
