# Asn1-Decoder-In-ZatoESB
This is an implementation in [ZATO ESB](https://zato.io)of a decoder using PyAsn1 library  for files encoded in DER/BER (ASN1) 

## Python Libraries
The two files located in the folder "PythonModules" should be copied in the zato_extra_path as suggested here [zato.io](https://zato.io/docs/admin/guide/enabling-extra-libs.html) 
 - PythonModules/DataStructureSDP.py is the data structure translated in PyAsn1 convention 
 - PythonModules/LcnDecodeur.py is the Python module that decode the BER/DER encoded file
