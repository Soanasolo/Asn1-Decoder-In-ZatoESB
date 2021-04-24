# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function, unicode_literals

from DataStructureSDP import *

from pyasn1.codec.ber.decoder import decode
import numpy as np
import os
import pandas as pd
import csv
import math
from datetime import datetime


def get_periodicAccountMgmtService(receivedRecord):
    # Retourne une SequenceOf ou liste s'il existe sinon retourne []
    return receivedRecord['periodicAccountMgmt'].getComponentByName('periodicAccountMgmtService', default = [], instantiate=False)



def get_balanceAfter_From_PeriodicAccountMgmtService(periodicAccountMgmntService):
    # balanceAfter                [6] MoneyAmount,  MoneyAmount ::= IA5String (SIZE (1..21))
    # Du type string dans le fichier encode mais float
    return periodicAccountMgmntService.getComponentByName('balanceAfter', default = 0, instantiate=False)



def get_deltaAmount_From_PeriodicAccountMgmtService(periodicAccountMgmntService):
    # deltaAmount                 [7] MoneyAmount OPTIONAL, MoneyAmount ::= IA5String (SIZE (1..21))
    # Du type string dans le fichier encode mais float
    return periodicAccountMgmntService.getComponentByName('deltaAmount', default = 0, instantiate=False)



def get_adjustmentOffers_From_PeriodicAccountMgmtService(periodicAccountMgmntService):
    return periodicAccountMgmntService.getComponentByName('adjustmentOffers', default = [], instantiate=False)



def get_offerID_From_AdjustmentOffer(AdjustmentOffer):
    # offerID                     [0] OfferID, OfferID ::= INTEGER (1..2147483647)
    return AdjustmentOffer.getComponentByName('offerID', default = '', instantiate=False)



def get_offerExpiryDateTimeAfter_From_AdjustmentOffer(AdjustmentOffer):
    return AdjustmentOffer.getComponentByName('offerExpiryDateTimeAfter', default = '', instantiate=False)



def getLigneDecode(receivedRecord):
    ligneDecode =  pd.DataFrame(columns = ['subscriberNumber', 'balanceAfter', 'deltaAmount', 'offerID',
                                         'offerExpiryDateTimeAfter'])

    d1 = {}

    # subscriberNumber             [4] NumberString, NumberString ::= IA5String (SIZE (1..30))
    d1['subscriberNumber'] = str(receivedRecord['periodicAccountMgmt'].getComponentByName('subscriberNumber', default = ''))

    # periodicAccountMgmtService  [16]  SEQUENCE OF PeriodicAccountMgmtService,
    # periodicAccountMgmtService est une liste composée de PeriodicAccountMgmtService
    # Pour une ligne decodée, il n'y a qu'une seule  periodicAccountMgmtService
    # Dans une periodicAccountMgmtService, il y a une ou plusieurs PeriodicAccountMgmtService
    periodicAccountMgmtService = get_periodicAccountMgmtService(receivedRecord)

    for PeriodicAccountMgmtService in periodicAccountMgmtService:

        # balanceAfter                [6] MoneyAmount,  MoneyAmount ::= IA5String (SIZE (1..21))
        d1['balanceAfter'] = float(get_balanceAfter_From_PeriodicAccountMgmtService(PeriodicAccountMgmtService))

        # deltaAmount                 [7] MoneyAmount OPTIONAL, MoneyAmount ::= IA5String (SIZE (1..21))
        d1['deltaAmount'] = abs(float(get_deltaAmount_From_PeriodicAccountMgmtService(PeriodicAccountMgmtService)))

        # Dans une PeriodicAccountMgmtService, il n'y a qu'une seule adjustmentOffers
        # Dans une adjustmentOffers, il peut y avoir une ou plusieurs AdjustmentOffer
        # adjustmentOffers  [20] SEQUENCE OF AdjustmentOffer OPTIONAL
        # adjustmentOffers est une liste composée de AdjustmentOffer
        adjustmentOffers = get_adjustmentOffers_From_PeriodicAccountMgmtService(PeriodicAccountMgmtService)

        for AdjustmentOffer in adjustmentOffers:

            # offerID                     [0] OfferID, OfferID ::= INTEGER (1..2147483647)
            d1['offerID'] = int(get_offerID_From_AdjustmentOffer(AdjustmentOffer))

            # offerExpiryDateTimeAfter    [13] TimeStamp OPTIONAL, TimeStamp ::= IA5String (SIZE (19))
            d1['offerExpiryDateTimeAfter'] = str(get_offerExpiryDateTimeAfter_From_AdjustmentOffer(AdjustmentOffer))

            ligneDecode = ligneDecode.append(d1, ignore_index = True)

    return ligneDecode


def decoderFichierSDPCallDataRecordLCN(nomFichier, fichierEncode):
    # fichierEncode devrait etre de type byte

    # Initialisation du panda dataframe pour enregistrer les infos decodes
    fichierDecode =  pd.DataFrame(columns = ['subscriberNumber', 'balanceAfter', 'deltaAmount', 'offerID',
                              'offerExpiryDateTimeAfter'])

    v = 1
    # Decode le fichier
    while len(fichierEncode) != 0:

        # Decode le premier ligne du fichier encode, et enleve ce meme ligne du fichierEncode
        received_record, fichierEncode = decode(fichierEncode, asn1Spec = SDPCallDataRecord())

        # Ne prends que la ligne du type 'periodicAccountMgmt'
        for field in received_record:
            if field == 'periodicAccountMgmt':
                listLigneDecode = getLigneDecode(received_record)
                fichierDecode = fichierDecode.append(listLigneDecode, ignore_index = True)

        v += 1

    return fichierDecode


if __name__ == '__main__':
    decoderFichierSDPCallDataRecordLCN(sys.argv[1])
