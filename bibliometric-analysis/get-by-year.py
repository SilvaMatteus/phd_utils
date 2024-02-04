import sys
import bibtexparser


if len(sys.argv) < 2:
    print('Invalid arg')
    sys.exit(1)


library = bibtexparser.parse_file(sys.argv[1])

if len(library.failed_blocks) > 0:
    print("Some blocks failed to parse. Check the entries of `library.failed_blocks`.")
    print(library.failed_blocks)
    exit(1)
else:
    print("All blocks parsed successfully...")

yd = {}
for entry in library.entries:
    if entry.fields_dict['year'].value in yd:
        yd[entry.fields_dict['year'].value] += 1
    else:
        yd[entry.fields_dict['year'].value] = 1

print(yd)

csv_lines = []
csv_lines.append("YEAR, COUNT\n")
for key in sorted(yd.keys()):
    csv_lines.append("{}, {}\n".format(key, yd[key]))

with open('years_count.csv', 'w') as f:
    f.writelines(csv_lines)
