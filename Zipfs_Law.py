from matplotlib import pyplot as plt
from nltk.corpus import gutenberg
from nltk.tokenize import word_tokenize
import re
from collections import OrderedDict
import itertools
from nltk.stem.porter import *
"""
Total Length ( words )= 12,108,867
Unique words: 2,200,035 / 50,913
--------------------------------------
the 133583
and 95450
of 70085
to 46446
a 32504
in 31959
I 30221
that 28798
he 22198
hi 21402
it 21025
for 19528
wa 18715
not 18189
with 17602
be 17522
you 16398
is 15944
thi 14524
but 13946
all 13725
as 13335
they 13104
him 13012
shall 11682
her 11625
have 10844
had 10317
them 10245
s 9792
my 9580
said 9434
me 9384
she 9078
from 9076
unto 9010
which 8775
lord 8671
at 8642
on 8194
by 8012
their 7865
will 7475
were 6871
are 6856
thou 6759
one 6408
there 6380
so 6338
when 6330
or 5901
what 5793
out 5784
god 5673
man 5644
your 5274
then 5091
ye 5037
up 4957
no 4910
thee 4807
say 4747
an 4730
now 4677
day 4616
upon 4587
do 4579
come 4484
who 4262
we 4213
into 4098
more 4062
would 4046
veri 4020
if 3965
thing 3951
son 3945
like 3861
He 3636
could 3594
king 3574
hand 3539
befor 3450
been 3441
know 3428
ani 3357
go 3340
came 3337
see 3276
time 3189
hous 3163
can 3145
did 3121
good 3076
littl 3069
look 3046
even 2993
other 2967
am 2928
down 2915


"""
file_id = gutenberg.fileids()
total_text = ''
for i in file_id:
    try:
        total_text = total_text + ' '.join(gutenberg.words(i))
    except:
        total_text = gutenberg.words(i)
        total_text = ' '.join(total_text)

total_text = re.sub(r'[^\w\s]', '', total_text)
total_text = ''.join(total_text)
total_text_tok = word_tokenize(total_text)
port = PorterStemmer()
total_text_st = []
for i in total_text_tok:
    total_text_st.append(port.stem(i))
one_dic = {}
for i in total_text_st:
    if word_tokenize(i)[0] in one_dic:
        one_dic[word_tokenize(i)[0]] += 1
    else:
        one_dic[word_tokenize(i)[0]] = 1

total_text_dic = OrderedDict(sorted(one_dic.items(), key=lambda x: -x[1]))
top_total_text_dic = itertools.islice(total_text_dic.items(), 0, 100)
value = list(zip(*top_total_text_dic))
for i in range(100):
    print(value[0][i], value[1][i])
plt.figure(figsize=(25, 13))
plt.plot(value[0], value[1])
plt.savefig(r'C:\Users\Student\Downloads\Top100_Distri_Gutenberg.jpg')
