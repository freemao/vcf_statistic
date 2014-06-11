#!/usr/lib/python
#-*- coding:utf-8 -*-

def basic_statistic(*names):
    '''Through statistic by this function, you will get a file which contain
    each files' total snp, the number of 0/1, 0/0, and 1/1.
    '''
    f0 = open('statistic_results.txt', 'w')
    f0.write('samples\t0/0\t0/1\t1/1\ttotal\n')
    for fn in names:
        sm = '.'.join(fn.split('.')[0:-1])
        f1 = open(fn, 'r')
        total = 0
        zerzer = 0
        zerone = 0
        oneone = 0
        others = 0
        for i in f1:
            if i.startswith('#'):
                pass
            else:
                total += 1
                j = i.split()[9].split(':')[0]
                if j == '0/0':
                    zerzer += 1
                elif j == '0/1':
                    zerone += 1
                elif j == '1/1':
                    oneone += 1
                else:
                    others += 1
        f1.close()
        f0.write(sm + '\t' + str(zerzer) + '\t' + str(zerone) + '\t' + \
str(oneone) + '\t' + str(others) + '\n')
    f0.close()

if __name__ == '__main__':
    import sys
    argslist = sys.argv[1:]
    basic_statistic(*sys.argv[1:])



