# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function, unicode_literals

import time, os
from contextlib import closing
from subprocess import call
import pandas as pd
import csv 
from datetime import date
import math 
import glob
import sys
import shutil
from datetime import datetime, timedelta
import configparser
import timeit

import LcnDecodeur

from zato.server.service import Service


class LcnAsnDecodeurFinalService(Service):
    name = "Lcn.AsnDecodeur1.Final.Service"

    # Config
    config = configparser.ConfigParser(converters={'list': lambda x: [i.strip() for i in x.split(',')]})
    config.read('/opt/properties/lcn_config.ini')
    CSV_WORK = config.get('decodeur_asn', 'csv_work')
    ASN_ARCHIVE = config.get('decodeur_asn', 'asn_archive')
    newExtension = config.get('decodeur_asn', 'extension_pendant_decodage')

    class SimpleIO:
        input_required = ('file', 'nom_decodeur')

    # https://zato.io/docs/progguide/hooks/service.html
    # def accept(self):
    #     # Prends le decodeur libre
    #     flagDecodeur, nomDecodeur = self.prendDecodeurLibre(self.listDecodeur, self.nbrDecodeur, self.redisListDecodeurEnMarche)

    #     # Prends le fichier non traite  
    #     flagFichier, fichier = self.prendFichierNonTraite(self.ASN_WORK, self.extension)

    #     return  (not flagFichier and not flagDecodeur and not self.kvdb.conn.exists(self.redisFlagDecodeur1))


    # @staticmethod
    # def before_add_to_store(logger):
    #     # Config
    #     config = configparser.ConfigParser(converters={'list': lambda x: [i.strip() for i in x.split(',')]})
    #     config.read('/opt/properties/lcn_config.ini')
    #     logger.info('Added to store {}'.format(LcnAsnDecodeurService.get_name()))
    #     redisListDecodeurEnMarche = config.get('decodeur_asn', 'redis_list_decodeur_en_marche')
    #     LcnAsnDecodeurService.kvdb.conn.delete(redisListDecodeurEnMarche)
    #     return True
            
    def handle(self):
        now = datetime.now()

        fichier = self.request.input.file
        nomDecodeur = self.request.input.nom_decodeur
        
        absolutePath = fichier.rsplit(os.path.sep, 1)[0]
        nomFichierAvecExtension = fichier.rsplit(os.path.sep, 1)[1]
        nomFichier = fichier.rsplit(os.path.sep, 1)[1].rsplit('.', 1)[0]
            
        self.logger.info("""{} -- {} -- Traitement du fichier '{}' \n""".format(now.strftime("%H:%M:%S:%f"), nomDecodeur, nomFichier))
        log_msg = """{} -- {} -- Traitement du fichier '{}' \n""".format(now.strftime("%H:%M:%S:%f"), nomDecodeur, nomFichier)
        try:
            # Etape 2 
            now00 = datetime.now()
            etape = "Etape 1 -- {}".format(now00.strftime("%H:%M:%S:%f"))
            operation = """Lecture du fichier en mode binaire"""
            fichierEncode = open(fichier, 'rb').read()
            now01 = datetime.now()
            log_msg += """{} -- {}: terminee ({})\n""".format(etape, operation, now01 - now00)    
            # Etape 3
            now00 = datetime.now()
            etape = "Etape 2 -- {}".format(now00.strftime("%H:%M:%S:%f"))
            operation = """Predecodage et decodage"""
            fichierDecode = LcnDecodeur.decoderFichierSDPCallDataRecordLCN(nomFichier, fichierEncode)
            now01 = datetime.now()
            log_msg += """{} -- {}: termine ({})\n""".format(etape, operation, now01 - now00)              
            # Etape 4
            now00 = datetime.now()
            etape = "Etape 3 -- {}".format(now00.strftime("%H:%M:%S:%f"))
            operation = """Export en fichier csv"""
            nomFichierDecode = """{}_{}_{}.csv""".format(nomFichier, nomDecodeur, now.strftime("%H:%M:%S:%f"))
            nomFichierDecode = os.path.join(self.CSV_WORK, nomFichierDecode)
            fichierDecode.to_csv(nomFichierDecode, index=True, sep = str(';') )
            now01 = datetime.now()
            log_msg += """{} -- {}: termine ({})\n""".format(etape, operation, now01 - now00)          
            # Etape 5
            now00 = datetime.now()
            etape = "Etape 4 -- {}".format(now00.strftime("%H:%M:%S:%f"))
            operation = """Copie du fichier '{}' vers ASN_ARCHIVE""".format(nomFichierAvecExtension)
            fichierArchive = os.path.join(self.ASN_ARCHIVE, nomFichierAvecExtension)
            shutil.move(fichier, fichierArchive)
            now01 = datetime.now()
            log_msg += """{} -- {}: terminee ({})\n""".format(etape, operation, now01 - now00)    
            now1 = datetime.now()
            log_msg += """ ================== Termine : {}\n""".format(now1 - now)
            self.logger.info(log_msg) 
        except Exception as es:
            log_warn = log_msg
            log_warn += """ ================== Erreur lors du traitement du fichier '{}': {} \n""".format(nomFichierAvecExtension, es)
            self.logger.warn(log_warn)
            log_msg = """Copie du fichier '{}' vers ASN_ARCHIVE""".format(nomFichierAvecExtension)
            try: 
                fichierArchive = os.path.join(self.ASN_ARCHIVE, nomFichierAvecExtension)
                shutil.move(fichier, fichierArchive)
                log_msg += """ ================== Terminee \n"""
                self.logger.info(log_msg)
            except Exception as es:
                log_warn = log_msg 
                log_warn += """ ================== Erreur: {} \n""".format(es)
                self.logger.warn(log_warn)


