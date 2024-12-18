# Asn1-Decoder-In-ZatoESB
This is an implementation in [ZATO ESB](https://zato.io) of a decoder using PyAsn1 library  for files encoded in DER/BER (ASN1) 

## Python Libraries
The two files located in the folder "PythonModules" should be copied in the "zato_extra_path" as suggested here [zato.io](https://zato.io/docs/admin/guide/enabling-extra-libs.html) 
 - PythonModules/DataStructureSDP.py is the data structure translated in PyAsn1 convention 
 - PythonModules/LcnDecodeur.py is the Python module that decode the BER/DER encoded file

## DecoderZatoService
The actual Zato service that decode the BER/DER encoded file is DecoderZatoService/ZatoAsnDecoder.py . This file should be deployed like any Zato service. 
The service requires two request inputs: 'file' which is the BER/DER encoded file name with its absolute path and 'nom_decodeur' which is any generic name. 
