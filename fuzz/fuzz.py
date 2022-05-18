#!/usr/local/bin/python3
import atheris
import sys
import io

# with atheris.instrument_imports():
from somajo import SoMaJo

de_tokenizer = SoMaJo("de_CMC")
en_tokenizer = SoMaJo("en_PTB")

@atheris.instrument_func
def TestOneInput(data):
    barray = bytearray(data)
    if len(barray) > 0:
        opt = barray[0]
        del barray[0]
        if opt % 8 == 0:
            de_tokenizer.tokenize_text(str(barray).split('.'))
        elif opt % 8 == 1:
            en_tokenizer.tokenize_text(str(barray).split('.'))
        elif opt % 8 == 2:
            f = io.BytesIO(barray)
            de_tokenizer.tokenize_text_file(f,paragraph_separator="single_newlines")
        elif opt % 8 == 3:
            f = io.BytesIO(barray)
            en_tokenizer.tokenize_text_file(f,paragraph_separator="single_newlines")
        elif opt % 8 == 4:
            if len(barray) > 2:
                eos_tags = str(barray[0:len(barray)//2]).split(' ')
                xml = str(barray[len(barray)//2:len(barray)])
                de_tokenizer.tokenize_xml(xml,eos_tags)
        elif opt % 8 == 5:
            if len(barray) > 2:
                eos_tags = str(barray[0:len(barray)//2]).split(' ')
                xml = str(barray[len(barray)//2:len(barray)])
                en_tokenizer.tokenize_xml(xml,eos_tags)
        elif opt % 8 == 6:
            if len(barray) > 2:
                eos_tags = str(barray[0:len(barray)//2]).split(' ')
                xml = str(barray[len(barray)//2:len(barray)])
                de_tokenizer.tokenize_xml_file(io.StringIO(xml),eos_tags)
        elif opt % 8 == 7:
            if len(barray) > 2:
                eos_tags = str(barray[0:len(barray)//2]).split(' ')
                xml = str(barray[len(barray)//2:len(barray)])
                en_tokenizer.tokenize_xml_file(io.StringIO(xml),eos_tags)
    else:
        en_tokenizer.tokenize_text([str(barray)])

atheris.instrument_all()
atheris.Setup(sys.argv, TestOneInput)
atheris.Fuzz()
