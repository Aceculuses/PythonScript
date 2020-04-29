#!/bin/python3

import sys, getopt

try:
    if sys.argv[1:]!=[]:
        opts,args=getopt.getopt(sys.argv[1:],'ho:x:')
        if len(args) == 1:
            input_file=args[0]
        elif len(args) ==0:
            pass
        else:
            print('Please check with -h to see how to use this programme')
    else:
        print("You have not yet enter any options and input fasta file. Please enter -h to see usage")
        print("Please type in: python3 command_line_options_parsing.py -h")
        sys.exit()

except getopt.GetoptError as err:
    print(err)
    print('Please check your options')
    print("Please type in: python3 command_line_options_parsing.py -h")
    sys.exit(2)

prefix='split_'
X=1

for op,value in opts:
    if op == '-o':
        prefix=value
        print('Got your prefix name: ', prefix)
    elif op == '-x':
        try:
            X=int(value)
            print('Got youur split number: ', X)
        except ValueError:
            print('Please make sure you enter a integer number for -x options')
            print('Help mannual: python3 command_line_options_parsing.py -h')
            sys.exit()
    elif op == '-h':
       print("Usage: split_fasta.py [options] input.fasta")
       print("Options:")
       print('  -o    STR      Output prefix name (default: split_)')
       print('  -x    INT      The number of a file will be splitted into (default: 1)')
       sys.exit()

#Open fasta file
try:
    fa_in_file=open(input_file,'r')
except IOError:
    print('The input fasta file do not exit, please enter correct file name')
    sys.exit()

fa_info=[]
fa_seq=[]
fa_num=-1

#Store seq_id and seq in fa_info and fa_seq lists respectively
for y in fa_in_file.readlines():
    y=y.rstrip()
    if y[0]=='>':
        fa_info.append(y)
        fa_num+=1
        fa_seq.append('')
    else:
        fa_seq[fa_num]+=y

#spli sequences evenly into multiple fasta files
file_num=(fa_num+1)//X +1

for i in range(file_num):
    exec(prefix + str(i + 1) + ' = open("' + prefix + str(i + 1) + '.fasta"' + ', "w")')#create fasta files
    #Generate sequence interval
    start=i*X
    end=(i+1)*X
    if end > fa_num+1:
        end=fa_num+1
    #\n false \\n yes
    for j in range(start, end, 1):
        exec(prefix + str(i + 1) + '.write(fa_info[j]+"\\n")')
        while len(fa_seq[j]) > 60:
            exec(prefix + str(i + 1) + '.write(fa_seq[j][:60]+"\\n")')
            fa_seq[j] = fa_seq[j][60:]
        else:
            exec(prefix + str(i + 1) + '.write(fa_seq[j]+"\\n")')
    exec(prefix + str(i + 1) + '.close()')
fa_in_file.close()
