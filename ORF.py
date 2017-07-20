# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 07:42:58 2017

@author: michael
"""
START = 'ATG'
STOP = ['TGA','TAG']
Read = []
Frames = []

def ORF(Seq):
    Len = len(Seq)
    for frame in range(3):
        Read = []
        for i in range(frame,Len,3):
            Codon =  Seq[i:i+3]
            if Codon == START:
                RNA = Seq[i::]
                Len2 = len(RNA)
                for bp in range(0,Len2,3):
                    Codon2 = RNA[bp:bp+3]
                    if Codon2 not in STOP:
                        Read.append(Codon2)
                    else:
                        pass
        Frames.append(''.join(Read))        
    #reverse
    Seq = Seq[::-1]
    for frame in range(3):
        Read = []
        for i in range(frame,Len,3):
            Codon =  Seq[i:i+3]
            if Codon == START:
                RNA = Seq[i::]
                Len2 = len(RNA)
                for bp in range(0,Len2,3):
                    Codon2 = RNA[bp:bp+3]
                    if Codon2 not in STOP:
                        Read.append(Codon2)
                    else:
                        pass
        Frames.append(''.join(Read)) 
    Open_Read = filter(lambda x: x != '',Frames)
    for i,n in enumerate(Open_Read):
        print (i+1),n
    return Open_Read
    
        
            
    
    """Len2 = len(RNA)
    for bp in range(0,Len2,3):
        Codon2 = RNA[bp:bp+3]
        if Codon2 not in STOP:
            Read.append(Codon2)
        else:
            Frames = ''.join(Read)
            break
    return Frames"""
            
            
        