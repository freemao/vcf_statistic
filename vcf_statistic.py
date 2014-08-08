#!/usr/lib/python
#-*- coding:utf-8 -*-

def GenoType_statistic(*names):
    '''Through statistic by this function, you will get a file which contain
    each files' total snp, the number of 0/1, 0/0, and 1/1.
    '''
    f0 = open('genotype_results.txt', 'w')
    f0.write('samples\t0/0\t0/1\t1/1\tothers\ttotal\n')
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
str(oneone) + '\t' + str(others) + '\t' + str(total) + '\n')
    f0.close()

def VariantType_fb_statistic(*names):
    from VCF_Parser import FbVcf
    '''This function is designed for freebayes, you will get a file which
    contain each vcf files' total variant type, snp, ins, del, mnp, complex
    ,other types('snp,snp', 'ins,snp', 'ins,ins'...)and these number of
    each sequence of each freebayse vcf file.
    '''
    f0 = open('FB.VariantType.results.txt', 'w')
    f0.write('samples\tSNP\tINS\tDEL\tMNP\tCOMPLEX\tOTHERS\tTOTAL\n')
    for fn in names:
        sm = '.'.join(fn.split('.')[0:-1])
        f1 = open(fn, 'r')
        Ttotal, Tsnp, Tins, Tdeletion, Tmnp, Tcomplex, Tothers = \
0, 0, 0, 0, 0, 0, 0
        Etotal, Esnp, Eins, Edeletion, Emnp, Ecomplex, Eothers = \
0, 0, 0, 0, 0, 0, 0
        chrlist = []
        for i in f1:
            if i.startswith('#'):
                pass
            else:
                Ttotal += 1
                instance1 = FbVcf()
                Chr = instance1.chr(i)
                vartype = instance1.VariantType(i)
                if Chr not in chrlist and len(chrlist)==0:
                    '''if vartype == 'snp':
                        Tsnp += 1
                        Esnp += 1
                    elif vartype == 'ins':
                        Tins += 1
                        Eins += 1
                    elif vartype == 'del':
                        Tdeletion += 1
                        Edeletion += 1
                    elif vartype == 'mnp':
                        Tmnp += 1
                        Emnp += 1
                    elif vartype == 'complex':
                        Tcomplex += 1
                        Ecomplex += 1
                    else :
                        Tothers += 1
                        Eothers += 1
                    Etotal += 1'''
                    chrlist.append(Chr)
                if Chr in chrlist:
                    if vartype == 'snp':
                        Tsnp += 1
                        Esnp += 1
                    elif vartype == 'ins':
                        Tins += 1
                        Eins += 1
                    elif vartype == 'del':
                        Tdeletion += 1
                        Edeletion += 1
                    elif vartype == 'mnp':
                        Tmnp += 1
                        Emnp += 1
                    elif vartype == 'complex':
                        Tcomplex += 1
                        Ecomplex += 1
                    else :
                        Tothers += 1
                        Eothers += 1
                    Etotal += 1
                if Chr not in chrlist and len(chrlist)!=0:
                    f0.write(chrlist[-1] + '\t' + str(Esnp) + '\t' + str(Eins) + '\t' + \
str(Edeletion) + '\t' + str(Emnp)+'\t'+str(Ecomplex)+'\t'+str(Eothers) \
+ '\t' + str(Etotal) + '\n')
                    Esnp, Eins, Edeletion, Emnp, Ecomplex, Eothers, Etotal =\
0, 0, 0, 0, 0, 0, 0
                    if vartype == 'snp':
                        Tsnp += 1
                        Esnp += 1
                    elif vartype == 'ins':
                        Tins += 1
                        Eins += 1
                    elif vartype == 'del':
                        Tdeletion += 1
                        Edeletion += 1
                    elif vartype == 'mnp':
                        Tmnp += 1
                        Emnp += 1
                    elif vartype == 'complex':
                        Tcomplex += 1
                        Ecomplex += 1
                    else :
                        Tothers += 1
                        Eothers += 1
                    Etotal += 1
                    chrlist.append(Chr)

        f1.close()
        f0.write(chrlist[-1] + '\t' + str(Esnp) + '\t' + str(Eins) + '\t' + \
str(Edeletion) + '\t' + str(Emnp)+'\t'+str(Ecomplex)+'\t'+str(Eothers) +\
 '\t' + str(Etotal) + '\n\n')
        f0.write(sm + '\t' + str(Tsnp) + '\t' + str(Tins) + '\t' + \
str(Tdeletion) + '\t' + str(Tmnp)+'\t'+str(Tcomplex)+'\t'+str(Tothers) \
+ '\t' + str(Ttotal) + '\n')
    f0.close()

if __name__ == '__main__':
    import sys
    argslist = sys.argv[1:]
    VariantType_fb_statistic(*sys.argv[1:])
