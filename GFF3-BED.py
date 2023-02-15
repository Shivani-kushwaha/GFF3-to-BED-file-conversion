def main_gff3():
 with open("./yeast.gff3", "r") as gff3_yeast, open("hw.bed", "w") as BED_hw:
  for lines in gff3_yeast:
       if lines.startswith('#'):
           continue
       column = lines.strip()
       column = lines.split('\t')
       if len(column) != 9:
           continue
       chromosome = str(column[0])
       start = int(int(column[3]) - 1)
       start = str(start)
       end = str(int(column[4]))
       end = str(end)
       strand = str(column[6])
       score = str(column[7])
       gene_name = column[8].split(';')[0].split('=')[1]
       read = "".join(chromosome + ' ' + start + ' ' + end + ' ' + score + ' ' + strand + ' ' + gene_name + '\n')
       BED_hw.write(read)
main_gff3()






