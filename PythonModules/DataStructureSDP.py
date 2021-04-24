# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function, unicode_literals

from pyasn1.type import univ, char, namedtype, namedval, tag, constraint, useful 


class AccountFlags(char.IA5String): 
    pass  


AccountFlags.subtypeSpec = constraint.ValueSizeConstraint(8, 8) 


class AccountGroupID(univ.Integer): 
    pass  


AccountGroupID.subtypeSpec = constraint.ValueRangeConstraint(0, 2147483647) 


class AccountHomeRegion(univ.Integer): 
    pass  


AccountHomeRegion.subtypeSpec = constraint.ValueRangeConstraint(0, 999) 


class AccountUnitType(univ.Enumerated): 
    pass  

AccountUnitType.namedValues = namedval.NamedValues( 
    ('time', 0),
    ('money', 1),
    ('totalOctets', 2),
    ('inputOctets', 3),
    ('outputOctets', 4),
    ('serviceSpecificUnits', 5),
    ('volume', 6)
 ) 


class AccumulatorID(univ.Integer): 
    pass  


AccumulatorID.subtypeSpec = constraint.ValueRangeConstraint(1, 2147483647) 


class AccumulatorValue(univ.Integer): 
    pass  


AccumulatorValue.subtypeSpec = constraint.ValueRangeConstraint(-2147483648, 2147483647) 


class AdjustmentAction(univ.Enumerated): 
    pass  

AdjustmentAction.namedValues = namedval.NamedValues( 
    ('set', 0),
    ('add', 1),
    ('subtract', 2),
    ('reset', 3),
    ('remove', 4),
    ('create', 5),
    ('modify', 6),
    ('crop', 8)
 ) 


class AdjustmentRecordType(univ.Enumerated): 
    pass  

AdjustmentRecordType.namedValues = namedval.NamedValues( 
    ('refillCDR', 1),
    ('notDefined', 2),
    ('linkageOfSubordinateSubscriber', 3),
    ('removalOfSubordinateSubscriber', 4),
    ('chargedEnquiry', 5),
    ('chargedServiceClassChange', 6),
    ('notUsed', 7),
    ('changedFamilyAndFriendsList', 8),
    ('clearedDedicatedAccount', 9),
    ('premiumRefill', 10),
    ('provisioningUaDa', 11),
    ('chargedCommunicationIdChange', 12),
    ('markForReratingChange', 13)
 ) 


class AdjustmentTransactionType(univ.Enumerated): 
    pass  

AdjustmentTransactionType.namedValues = namedval.NamedValues( 
    ('refill', 1),
    ('adjustment', 2),
    ('offlinePromotion', 3)
 ) 


class AttributeInfo(univ.Sequence): 
    componentType = namedtype.NamedTypes( 
        namedtype.NamedType('attributeName', char.UTF8String().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))),
        namedtype.OptionalNamedType('attributeValueString', char.UTF8String().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))))

class BonusAccumulator(univ.Sequence): 
    componentType = namedtype.NamedTypes( 
        namedtype.NamedType('accumulatorID', AccumulatorID().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))),
        namedtype.NamedType('accumulatorValueBefore', AccumulatorValue().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))),
        namedtype.NamedType('accumulatorValueAfter', AccumulatorValue().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2))),
        namedtype.NamedType('accumulatorDelta', AccumulatorValue().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 3))))

class CampaignIdentifier(univ.Integer): 
    pass  


CampaignIdentifier.subtypeSpec = constraint.ValueRangeConstraint(1, 99999999) 


class ChargingSuccessCode(univ.Enumerated): 
    pass  

ChargingSuccessCode.namedValues = namedval.NamedValues( 
    ('chargingSucceeded', 0),
    ('chargingPerformedAtDifferentCost', 1),
    ('chargingPerformedPresentedCostLost', 2),
    ('chargingPerformedPartialDeduction', 3),
    ('chargingFailed', 4)
 ) 


class ClearedAccumulator(univ.Sequence): 
    componentType = namedtype.NamedTypes( 
        namedtype.NamedType('accumulatorID', AccumulatorID().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))),
        namedtype.NamedType('clearedAccumulatorValue', AccumulatorValue().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))))

class CommunityID(univ.Integer): 
    pass  


CommunityID.subtypeSpec = constraint.ValueRangeConstraint(0, 9999999) 


class CounterDelta(univ.Integer): 
    pass  


CounterDelta.subtypeSpec = constraint.ValueRangeConstraint(-127, 127) 


class CounterValue(univ.Integer): 
    pass  


CounterValue.subtypeSpec = constraint.ValueRangeConstraint(0, 127) 


class CurrencyType(univ.Integer): 
    pass  



class Date(char.IA5String): 
    pass  


Date.subtypeSpec = constraint.ValueSizeConstraint(8, 8) 


class DateSpecial(univ.Enumerated): 
    pass  

DateSpecial.namedValues = namedval.NamedValues( 
    ('beginningOfTime', 1),
    ('endOfTime', 2)
 ) 


class DateRange(univ.Sequence): 
    componentType = namedtype.NamedTypes( 
        namedtype.NamedType('startDate', Date().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))),
        namedtype.NamedType('endDate', Date().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))))

class DayOfMonth(univ.Integer): 
    pass  


DayOfMonth.subtypeSpec = constraint.ValueRangeConstraint(-1, 31) 


class DayOfWeek(univ.Enumerated): 
    pass  

DayOfWeek.namedValues = namedval.NamedValues( 
    ('monday', 1),
    ('tuesday', 2),
    ('wednesday', 3),
    ('thursday', 4),
    ('friday', 5),
    ('saturday', 6),
    ('sunday', 7)
 ) 


class DedicatedAccountID(univ.Integer): 
    pass  


DedicatedAccountID.subtypeSpec = constraint.ValueRangeConstraint(1, 2147483647) 


class DisconnectionCode(univ.Integer): 
    pass  


DisconnectionCode.subtypeSpec = constraint.ValueRangeConstraint(0, 255) 


class EocnSelectionId(univ.Integer): 
    pass  


EocnSelectionId.subtypeSpec = constraint.ValueRangeConstraint(0, 255) 


class ExternalParameterName(char.IA5String): 
    pass  


ExternalParameterName.subtypeSpec = constraint.ValueSizeConstraint(1, 128) 


class ExternalParameterValue(char.IA5String): 
    pass  


ExternalParameterValue.subtypeSpec = constraint.ValueSizeConstraint(1, 128) 


class ExternalProductID(char.IA5String): 
    pass  


ExternalProductID.subtypeSpec = constraint.ValueSizeConstraint(1, 55) 


class FamilyAndFriendsAction(univ.Enumerated): 
    pass  

FamilyAndFriendsAction.namedValues = namedval.NamedValues( 
    ('set', 0),
    ('add', 1),
    ('delete', 2)
 ) 


class FamilyAndFriendsIndicator(univ.Integer): 
    pass  


FamilyAndFriendsIndicator.subtypeSpec = constraint.ValueRangeConstraint(1, 65535) 


class FileName(char.IA5String): 
    pass  



class GlobalParameterName(char.UTF8String): 
    pass  



class GlobalParameterString(char.UTF8String): 
    pass  



class Hour(univ.Integer): 
    pass  


Hour.subtypeSpec = constraint.ValueRangeConstraint(0, 23) 


class IDString(char.IA5String): 
    pass  



class Integer32(univ.Integer): 
    pass  


Integer32.subtypeSpec = constraint.ValueRangeConstraint(-2147483648, 2147483647) 


class Integer64(univ.Integer): 
    pass  


Integer64.subtypeSpec = constraint.ValueRangeConstraint(-9223372036854775808, 9223372036854775807) 


class Language(univ.Integer): 
    pass  


Language.subtypeSpec = constraint.ValueRangeConstraint(1, 4) 


class MidCycleReratingState(univ.Enumerated): 
    pass  

MidCycleReratingState.namedValues = namedval.NamedValues( 
    ('marked', 0),
    ('unmarked', 1)
 ) 


class MidCycleReratingStateChangeReason(univ.Enumerated): 
    pass  

MidCycleReratingStateChangeReason.namedValues = namedval.NamedValues( 
    ('noStateChange', 0),
    ('externalMarkRequest', 1),
    ('externalUnmarkAndLoadRequest', 2),
    ('externalUnmarkAndNoLoadRequest', 3),
    ('internalReratingTimeOut', 4),
    ('internalBillCycleInstanceSwitch', 5),
    ('internalPamEvaluation', 6)
 ) 


class Minute(univ.Integer): 
    pass  


Minute.subtypeSpec = constraint.ValueRangeConstraint(0, 59) 


class MoneyAmount(char.IA5String): 
    pass  


MoneyAmount.subtypeSpec = constraint.ValueSizeConstraint(1, 21) 


class Month(univ.Integer): 
    pass  


Month.subtypeSpec = constraint.ValueRangeConstraint(1, 12) 


class MultiUnits(Integer64): 
    pass 


class NodeID(char.IA5String): 
    pass  


NodeID.subtypeSpec = constraint.ValueSizeConstraint(1, 20) 


class NodeType(char.IA5String): 
    pass  


NodeType.subtypeSpec = constraint.ValueSizeConstraint(1, 8) 


class NumberString(char.IA5String): 
    pass  


NumberString.subtypeSpec = constraint.ValueSizeConstraint(1, 30) 


class OfferID(univ.Integer): 
    pass  


OfferID.subtypeSpec = constraint.ValueRangeConstraint(1, 2147483647) 


class OfferType(univ.Enumerated): 
    pass  

OfferType.namedValues = namedval.NamedValues( 
    ('account', 0),
    ('multiUserIdentification', 1),
    ('timer', 2),
    ('providerAccount', 3),
    ('sharedAccount', 4)
 ) 


class Owner(univ.Enumerated): 
    pass  

Owner.namedValues = namedval.NamedValues( 
    ('subscriber', 1),
    ('account', 2)
 ) 


class PamClassID(univ.Integer): 
    pass  


PamClassID.subtypeSpec = constraint.ValueRangeConstraint(0, 9999) 


class PamEventType(univ.Enumerated): 
    pass  

PamEventType.namedValues = namedval.NamedValues( 
    ('userInitiatedEval', 1),
    ('pamInitiation', 2),
    ('pamChange', 3),
    ('pamDelete', 4),
    ('scheduled', 5)
 ) 


class PamIndicator(univ.Integer): 
    pass  


PamIndicator.subtypeSpec = constraint.ValueRangeConstraint(0, 65535) 


class PamPeriod(char.IA5String): 
    pass  


PamPeriod.subtypeSpec = constraint.ValueSizeConstraint(1, 30) 


class PamServiceID(univ.Integer): 
    pass  


PamServiceID.subtypeSpec = constraint.ValueRangeConstraint(0, 99) 


class PamServicePriority(univ.Integer): 
    pass  


PamServicePriority.subtypeSpec = constraint.ValueRangeConstraint(0, 65535) 


class Percent(char.IA5String): 
    pass  


Percent.subtypeSpec = constraint.ValueSizeConstraint(1, 10) 


class Period(univ.Integer): 
    pass  


Period.subtypeSpec = constraint.ValueRangeConstraint(0, 1023) 


class PeriodicResetID(univ.Integer): 
    pass  


PeriodicResetID.subtypeSpec = constraint.ValueRangeConstraint(0, 255) 


class PeriodType(univ.Integer): 
    pass  



class PreActReasonCode(univ.Enumerated): 
    pass  

PreActReasonCode.namedValues = namedval.NamedValues( 
    ('origInsideHPLMN', 0),
    ('origOutsideHPLMNwithCAPv1', 1),
    ('origOutsideHPLMNwithCAPv2', 2),
    ('uSSDCallBack', 3),
    ('origOutsideHPLMNwithCAPv3', 4),
    ('firstIVRcall', 5),
    ('firstUSSDaccess', 6),
    ('firstExpiryDateSet', 7),
    ('terminating', 8)
 ) 


class ProductFeeDedicatedAccount(univ.Sequence): 
    componentType = namedtype.NamedTypes( 
        namedtype.NamedType('dedicatedAccountID', DedicatedAccountID().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))),
        namedtype.NamedType('accountValueAfter', MoneyAmount().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))),
        namedtype.NamedType('accountValueChange', MoneyAmount().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2))),
        namedtype.OptionalNamedType('campaignIdentifier', CampaignIdentifier().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 3))))

class ProductFeeMainAccount(univ.Sequence): 
    componentType = namedtype.NamedTypes( 
        namedtype.NamedType('balanceAfter', MoneyAmount().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))),
        namedtype.NamedType('balanceChange', MoneyAmount().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))))

class ProductID(univ.Integer): 
    pass  


ProductID.subtypeSpec = constraint.ValueRangeConstraint(1, 2147483647) 


class ProductOfferingName(char.IA5String): 
    pass  


ProductOfferingName.subtypeSpec = constraint.ValueSizeConstraint(1, 128) 


class PromotionPlan(char.IA5String): 
    pass  


PromotionPlan.subtypeSpec = constraint.ValueSizeConstraint(1, 4) 


class Qualifier(univ.Integer): 
    pass  


Qualifier.subtypeSpec = constraint.ValueRangeConstraint(0, 4294967295) 


class Reason(univ.Enumerated): 
    pass  

Reason.namedValues = namedval.NamedValues( 
    ('serviceClassChange', 1),
    ('subscriberDeleted', 2),
    ('creditClearancePeriodExpired', 3),
    ('dedicatedAccountExpired', 4),
    ('other', 5),
    ('subDedicatedAccountExpired', 6),
    ('offerExpired', 7),
    ('fafExpired', 8),
    ('userInitiatedRequest', 9),
    ('depleted', 10),
    ('tbaRetryDurationExpired', 11)
 ) 


class RecordSequenceNumberString(char.IA5String): 
    pass  


RecordSequenceNumberString.subtypeSpec = constraint.ValueSizeConstraint(1, 20) 


class RemovedFaF(univ.Sequence): 
    componentType = namedtype.NamedTypes( 
        namedtype.NamedType('familyAndFriendsNumber', NumberString().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))),
        namedtype.NamedType('familyAndFriendsIndicator', FamilyAndFriendsIndicator().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))),
        namedtype.OptionalNamedType('fafExpiryDate', Date().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2))),
        namedtype.OptionalNamedType('fafStartDate', Date().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 3))),
        namedtype.OptionalNamedType('offerID', OfferID().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 4))),
        namedtype.OptionalNamedType('reason', Reason().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 5))),
        namedtype.OptionalNamedType('owner', Owner().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 6))))

class ReplenishmentID(univ.Integer): 
    pass  


ReplenishmentID.subtypeSpec = constraint.ValueRangeConstraint(0, 255) 


class ScheduledFrequency(univ.Enumerated): 
    pass  

ScheduledFrequency.namedValues = namedval.NamedValues( 
    ('yearly', 1),
    ('monthly', 2),
    ('weekly', 3),
    ('daily', 4),
    ('hourly', 5),
    ('minutely', 6),
    ('secondly', 7)
 ) 


class ScheduleID(univ.Integer): 
    pass  


ScheduleID.subtypeSpec = constraint.ValueRangeConstraint(0, 9999) 


class ScheduledInterval(univ.Integer): 
    pass  


ScheduledInterval.subtypeSpec = constraint.ValueRangeConstraint(1, 99999) 


class Second(univ.Integer): 
    pass  


Second.subtypeSpec = constraint.ValueRangeConstraint(0, 59) 


class SelectionTreeQualifiers(univ.SequenceOf): 
    componentType = Qualifier 


class SelectionTreeType(univ.Enumerated): 
    pass  

SelectionTreeType.namedValues = namedval.NamedValues( 
    ('rating', 0),
    ('bonus', 1),
    ('selection', 2),
    ('dedicatedAccount', 3),
    ('communityCharging', 4),
    ('numberNormalization', 5),
    ('ussdTextMessage', 6),
    ('accountManagement', 7),
    ('preAnalysis', 8),
    ('periodicAccountManagement', 9)
 ) 


class ServFeeDeductSuccessCode(univ.Enumerated): 
    pass  

ServFeeDeductSuccessCode.namedValues = namedval.NamedValues( 
    ('ok', 1),
    ('okServiceExpired', 2),
    ('okServiceClassChange', 3),
    ('okNoAction', 4),
    ('nokServiceClassChange', 5),
    ('okFirstDeductionSuppressed', 6),
    ('okServiceDeactivated', 7),
    ('serviceFeeTypeDisconnectedDebtCleared', 8),
    ('partialDeductionWhenAccumulatedDeduction', 9),
    ('okOfferExpired', 10),
    ('okConditionalDebtAccumulated', 11)
 ) 


class ServiceClass(univ.Integer): 
    pass  


ServiceClass.subtypeSpec = constraint.ValueRangeConstraint(0, 9999) 


class ServiceFeeType(char.IA5String): 
    pass  


ServiceFeeType.subtypeSpec = constraint.ValueSizeConstraint(1, 10) 


class ServiceOfferings(univ.Integer): 
    pass  


ServiceOfferings.subtypeSpec = constraint.ValueRangeConstraint(0, 2147483647) 


class ServiceProvider(univ.Enumerated): 
    pass  

ServiceProvider.namedValues = namedval.NamedValues( 
    ('ratingTemplate', 1),
    ('policyRuleDeterminationTemplate', 2),
    ('productNotificationTemplate', 3),
    ('productFeeTemplate', 4),
    ('productProvisionTemplate', 5),
    ('quotaDeterminationTemplate', 6)
 ) 


class SfeeFromDAReturnCode(univ.Enumerated): 
    pass  

SfeeFromDAReturnCode.namedValues = namedval.NamedValues( 
    ('nokUDA', 1),
    ('nokXDA', 2),
    ('okEMnDA', 3),
    ('okXMnDA', 4),
    ('okDA', 5),
    ('okMnDA', 6)
 ) 


class SubDedicatedAccountInfo(univ.Sequence): 
    componentType = namedtype.NamedTypes( 
        namedtype.NamedType('dedicatedAccountID', DedicatedAccountID().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))),
        namedtype.OptionalNamedType('accountValue', MoneyAmount().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))),
        namedtype.OptionalNamedType('accountExpiryDate', Date().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2))),
        namedtype.OptionalNamedType('accountStartDate', Date().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 3))),
        namedtype.OptionalNamedType('accountUnit', MultiUnits().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 4))))

class Time(char.IA5String): 
    pass  


Time.subtypeSpec = constraint.ValueSizeConstraint(8, 8) 


class TimeBasedActionType(univ.Enumerated): 
    pass  

TimeBasedActionType.namedValues = namedval.NamedValues( 
    ('activate', 1)
 ) 


class TimeStamp(char.IA5String): 
    pass  


TimeStamp.subtypeSpec = constraint.ValueSizeConstraint(19, 19) 


class TimeZone(char.IA5String): 
    pass  


TimeZone.subtypeSpec = constraint.ValueSizeConstraint(1, 256) 


class TransactionCode(char.IA5String): 
    pass  


TransactionCode.subtypeSpec = constraint.ValueSizeConstraint(1, 30) 


class TransactionID(char.IA5String): 
    pass  


TransactionID.subtypeSpec = constraint.ValueSizeConstraint(1, 20) 


class TransactionType(char.IA5String): 
    pass  


TransactionType.subtypeSpec = constraint.ValueSizeConstraint(1, 30) 


class TransferRecordType(univ.Enumerated): 
    pass  

TransferRecordType.namedValues = namedval.NamedValues( 
    ('subscriberReceived', 1),
    ('subscriberTransferred', 2),
    ('subscriberWakeUp', 3),
    ('cancelRedirect', 4)
 ) 


class TreeParameterName(char.UTF8String): 
    pass  



class TreeParameterString(char.UTF8String): 
    pass  



class Unsigned32(univ.Integer): 
    pass  


Unsigned32.subtypeSpec = constraint.ValueRangeConstraint(0, 4294967295) 


class Unsigned63(univ.Integer): 
    pass  


Unsigned63.subtypeSpec = constraint.ValueRangeConstraint(0, 9223372036854775807) 


class Unsigned64(univ.Integer): 
    pass  


Unsigned64.subtypeSpec = constraint.ValueRangeConstraint(0, 1844674407370955161) 


class UsageCounterID(univ.Integer): 
    pass  


UsageCounterID.subtypeSpec = constraint.ValueRangeConstraint(1, 2147483647) 


class UsageThresholdID(univ.Integer): 
    pass  


UsageThresholdID.subtypeSpec = constraint.ValueRangeConstraint(1, 2147483647) 


class NegativeBalanceBarred(univ.Sequence): 
    componentType = namedtype.NamedTypes( 
        namedtype.NamedType('sdpID', NodeID().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))),
        namedtype.NamedType('cdrID', RecordSequenceNumberString().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2))),
        namedtype.NamedType('accountNumber', NumberString().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 3))),
        namedtype.NamedType('timeStamp', TimeStamp().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 4))),
        namedtype.NamedType('accountBalance', MoneyAmount().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 5))),
        namedtype.NamedType('currencyType', CurrencyType().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 6))),
        namedtype.OptionalNamedType('lastRecord', univ.Boolean().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 7))),
        namedtype.OptionalNamedType('subscriberConvergent', univ.Boolean().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 8))),
        namedtype.OptionalNamedType('aggregatedBalance', MoneyAmount().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 9))))

class PeriodicAdjustment(univ.Sequence): 
    componentType = namedtype.NamedTypes( 
        namedtype.NamedType('sdpID', NodeID().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))),
        namedtype.NamedType('cdrID', RecordSequenceNumberString().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2))),
        namedtype.NamedType('timeStamp', TimeStamp().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 3))),
        namedtype.NamedType('accountNumber', NumberString().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 4))),
        namedtype.NamedType('dedicatedAccountID', DedicatedAccountID().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 5))),
        namedtype.NamedType('currencyType', CurrencyType().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 6))),
        namedtype.OptionalNamedType('lastRecord', univ.Boolean().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 7))),
        namedtype.NamedType('replenishmentID', ReplenishmentID().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 8))),
        namedtype.OptionalNamedType('rolloverNewPeriod', MoneyAmount().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 9))),
        namedtype.OptionalNamedType('rolloverOldPeriod', MoneyAmount().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 10))),
        namedtype.OptionalNamedType('replenishmentDate', Date().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 11))),
        namedtype.OptionalNamedType('replenishmentAmount', MoneyAmount().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 12))),
        namedtype.OptionalNamedType('oldReplenishmentAmount', MoneyAmount().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 13))),
        namedtype.OptionalNamedType('balanceBeforeAdjustment', MoneyAmount().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 14))),
        namedtype.OptionalNamedType('unusedRollover', MoneyAmount().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 15))),
        namedtype.OptionalNamedType('oldServiceClass', ServiceClass().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 16))),
        namedtype.NamedType('serviceClassId', ServiceClass().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 17))),
        namedtype.OptionalNamedType('dedicatedAccountAdjustment', MoneyAmount().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 18))),
        namedtype.OptionalNamedType('dedicatedAccountClearance', MoneyAmount().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 19))),
        namedtype.OptionalNamedType('rolloverCalculationApplied', univ.Boolean().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 20))),
        namedtype.OptionalNamedType('periodOffset', univ.Integer().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 21))),
        namedtype.OptionalNamedType('startDate', Date().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 22))),
        namedtype.OptionalNamedType('periodLength', univ.Integer().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 23))),
        namedtype.OptionalNamedType('typeOfPeriod', PeriodType().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 24))),
        namedtype.OptionalNamedType('aggrBalBeforeAdjustment', MoneyAmount().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 25))),
        namedtype.OptionalNamedType('dedicatedAccountRealMoney', univ.Boolean().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 26))),
        namedtype.OptionalNamedType('offerID', OfferID().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 27))),
        namedtype.OptionalNamedType('accountUnitType', AccountUnitType().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 28))),
        namedtype.OptionalNamedType('dedicatedAccountAdjustmentUnit', MultiUnits().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 29))),
        namedtype.OptionalNamedType('dedicatedAccountClearanceUnit', MultiUnits().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 30))),
        namedtype.OptionalNamedType('unitBalanceBeforeAdjustment', MultiUnits().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 31))),
        namedtype.OptionalNamedType('dedicatedAccountBalance', MoneyAmount().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 32))),
        namedtype.OptionalNamedType('unitDedicatedAccountBalance', MultiUnits().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 33))))

class PeriodicReset(univ.Sequence): 
    componentType = namedtype.NamedTypes( 
        namedtype.NamedType('sdpID', NodeID().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))),
        namedtype.NamedType('cdrID', RecordSequenceNumberString().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2))),
        namedtype.NamedType('timeStamp', TimeStamp().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 3))),
        namedtype.NamedType('accountNumber', NumberString().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 4))),
        namedtype.NamedType('currencyType', CurrencyType().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 5))),
        namedtype.OptionalNamedType('lastRecord', univ.Boolean().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 6))),
        namedtype.NamedType('periodicResetID', PeriodicResetID().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 7))),
        namedtype.OptionalNamedType('periodicResetDate', Date().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 8))),
        namedtype.OptionalNamedType('balanceAtStartOfNewPeriod', MoneyAmount().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 9))),
        namedtype.OptionalNamedType('balanceBeforeAdjustment', MoneyAmount().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 10))),
        namedtype.OptionalNamedType('oldServiceClass', ServiceClass().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 11))),
        namedtype.NamedType('serviceClassId', ServiceClass().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 12))),
        namedtype.OptionalNamedType('periodOffset', univ.Integer().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 13))),
        namedtype.OptionalNamedType('startDate', Date().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 14))),
        namedtype.OptionalNamedType('periodLength', univ.Integer().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 15))),
        namedtype.OptionalNamedType('typeOfPeriod', PeriodType().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 16))),
        namedtype.OptionalNamedType('aggrBalAtStartOfNewPeriod', MoneyAmount().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 17))),
        namedtype.OptionalNamedType('aggrBalBeforeAdjustment', MoneyAmount().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 18))))

class TemporaryBlock(univ.Sequence): 
    componentType = namedtype.NamedTypes( 
        namedtype.NamedType('sdpID', NodeID().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))),
        namedtype.NamedType('cdrID', RecordSequenceNumberString().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2))),
        namedtype.NamedType('accountNumber', NumberString().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 3))),
        namedtype.NamedType('subscriberNumber', NumberString().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 4))),
        namedtype.NamedType('adjustmentTimeStamp', TimeStamp().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 5))),
        namedtype.OptionalNamedType('originNodeType', NodeType().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 6))),
        namedtype.OptionalNamedType('originNodeID', IDString().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 7))),
        namedtype.OptionalNamedType('origTransactionID', TransactionID().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 8))),
        namedtype.OptionalNamedType('origTransactionTimeStamp', TimeStamp().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 9))),
        namedtype.OptionalNamedType('transactionType', TransactionType().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 10))),
        namedtype.OptionalNamedType('transactionCode', TransactionCode().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 11))),
        namedtype.OptionalNamedType('originOperatorId', IDString().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 12))),
        namedtype.OptionalNamedType('temporaryBlockedStatusBefore', univ.Boolean().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 13))),
        namedtype.OptionalNamedType('temporaryBlockedStatusAfter', univ.Boolean().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 14))))

class CDRFileControlBlock(univ.Sequence): 
    componentType = namedtype.NamedTypes( 
        namedtype.NamedType('cdrFileSequenceNumber', Unsigned64().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))),
        namedtype.NamedType('sdpID', NodeID().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2))),
        namedtype.NamedType('cdrFileTimeStamp', TimeStamp().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 3))),
        namedtype.NamedType('cdrFileName', FileName().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 4))),
        namedtype.OptionalNamedType('cdrRecordCount', Unsigned32().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 5))))

class SubscriberTransfer(univ.Sequence): 
    componentType = namedtype.NamedTypes( 
        namedtype.NamedType('transferRecordType', TransferRecordType().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))),
        namedtype.OptionalNamedType('sdpID', NodeID().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2))),
        namedtype.OptionalNamedType('destinationSdpIPAddress', NodeID().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 3))),
        namedtype.NamedType('cdrID', RecordSequenceNumberString().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 4))),
        namedtype.NamedType('accountNumber', NumberString().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 5))),
        namedtype.NamedType('timeStamp', TimeStamp().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 6))),
        namedtype.OptionalNamedType('origTransactionID', TransactionID().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 7))),
        namedtype.OptionalNamedType('originNodeType', NodeType().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 8))),
        namedtype.OptionalNamedType('originNodeID', IDString().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 9))),
        namedtype.OptionalNamedType('origTransactionTimeStamp', TimeStamp().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 10))),
        namedtype.OptionalNamedType('dataTransferChecksum', char.IA5String().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 11))))

class AccumulatorInfo(univ.Sequence): 
    componentType = namedtype.NamedTypes( 
        namedtype.NamedType('accumulatorID', AccumulatorID().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))),
        namedtype.OptionalNamedType('accumulatorValue', AccumulatorValue().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))),
        namedtype.OptionalNamedType('accumulatorClearDate', Date().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2))))

class AdjustmentAccumulator(univ.Sequence): 
    componentType = namedtype.NamedTypes( 
        namedtype.NamedType('accumulatorID', AccumulatorID().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))),
        namedtype.OptionalNamedType('accumulatorValueBefore', AccumulatorValue().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))),
        namedtype.OptionalNamedType('accumulatorValueAfter', AccumulatorValue().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2))),
        namedtype.OptionalNamedType('accumulatorAdjustment', AccumulatorValue().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 3))),
        namedtype.NamedType('action', AdjustmentAction().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 4))),
        namedtype.OptionalNamedType('clearedAccumulatorValue', AccumulatorValue().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 5))),
        namedtype.OptionalNamedType('accumulatorClearDateBefore', Date().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 6))),
        namedtype.OptionalNamedType('accumulatorClearDateAfter', Date().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 7))),
        namedtype.OptionalNamedType('accumulatorValueInitial', AccumulatorValue().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 8))),
        namedtype.OptionalNamedType('accumulatorClearDateInitial', Date().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 9))),
        namedtype.OptionalNamedType('reason', Reason().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 10))))

class AdjustmentFaF(univ.Sequence): 
    componentType = namedtype.NamedTypes( 
        namedtype.NamedType('familyAndFriendsNumber', NumberString().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))),
        namedtype.NamedType('action', AdjustmentAction().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))),
        namedtype.NamedType('familyAndFriendsIndicator', FamilyAndFriendsIndicator().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2))),
        namedtype.OptionalNamedType('fafExpiryDateBefore', Date().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 3))),
        namedtype.OptionalNamedType('fafExpiryDateAfter', Date().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 4))),
        namedtype.OptionalNamedType('fafStartDateBefore', Date().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 5))),
        namedtype.OptionalNamedType('fafStartDateAfter', Date().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 6))),
        namedtype.OptionalNamedType('offerID', OfferID().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 7))),
        namedtype.OptionalNamedType('reason', Reason().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 8))),
        namedtype.OptionalNamedType('owner', Owner().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 9))))

class AdjustmentPeriodicAccountMgmt(univ.Sequence): 
    componentType = namedtype.NamedTypes( 
        namedtype.NamedType('pamServiceID', PamServiceID().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))),
        namedtype.OptionalNamedType('pamClassIDBefore', PamClassID().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))),
        namedtype.OptionalNamedType('pamClassIDAfter', PamClassID().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2))),
        namedtype.OptionalNamedType('scheduleIDBefore', ScheduleID().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 3))),
        namedtype.OptionalNamedType('scheduleIDAfter', ScheduleID().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 4))),
        namedtype.OptionalNamedType('pamPeriodBefore', PamPeriod().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 5))),
        namedtype.OptionalNamedType('pamPeriodAfter', PamPeriod().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 6))),
        namedtype.OptionalNamedType('deferredToDateBefore', Date().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 7))),
        namedtype.OptionalNamedType('deferredToDateAfter', Date().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 8))),
        namedtype.OptionalNamedType('pamServicePriorityBefore', PamServicePriority().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 9))),
        namedtype.OptionalNamedType('pamServicePriorityAfter', PamServicePriority().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 10))))

class AdjustmentSubDedicatedAccount(univ.Sequence): 
    componentType = namedtype.NamedTypes( 
        namedtype.NamedType('dedicatedAccountID', DedicatedAccountID().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))),
        namedtype.OptionalNamedType('accountValueBefore', MoneyAmount().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))),
        namedtype.OptionalNamedType('accountValueAfter', MoneyAmount().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2))),
        namedtype.OptionalNamedType('adjustmentAmount', MoneyAmount().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 3))),
        namedtype.OptionalNamedType('accountExpiryDateBefore', Date().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 4))),
        namedtype.OptionalNamedType('accountExpiryDateAfter', Date().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 5))),
        namedtype.OptionalNamedType('originalAdjustmentAmount', MoneyAmount().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 6))),
        namedtype.OptionalNamedType('clearedAccountValue', MoneyAmount().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 7))),
        namedtype.OptionalNamedType('accountValueInitial', MoneyAmount().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 8))),
        namedtype.OptionalNamedType('accountExpiryDateInitial', Date().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 9))),
        namedtype.OptionalNamedType('accountStartDateBefore', Date().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 10))),
        namedtype.OptionalNamedType('accountStartDateAfter', Date().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 11))),
        namedtype.OptionalNamedType('accountStartDateInitial', Date().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 12))),
        namedtype.OptionalNamedType('mergedIntoDedicatedAccountID', DedicatedAccountID().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 13))),
        namedtype.OptionalNamedType('accountStartDate', Date().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 14))),
        namedtype.OptionalNamedType('accountExpiryDate', Date().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 15))),
        namedtype.OptionalNamedType('movedToOtherSubDedicatedAccount', univ.Boolean().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 16))),
        namedtype.OptionalNamedType('accountUnitBefore', MultiUnits().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 17))),
        namedtype.OptionalNamedType('accountUnitAfter', MultiUnits().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 18))),
        namedtype.OptionalNamedType('adjustmentUnit', MultiUnits().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 19))),
        namedtype.OptionalNamedType('clearedAccountUnit', MultiUnits().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 20))),
        namedtype.OptionalNamedType('accountUnitInitial', MultiUnits().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 21))))

class AggregatedBalanceSubDedicatedAccount(univ.Sequence): 
    componentType = namedtype.NamedTypes( 
        namedtype.NamedType('dedicatedAccountID', DedicatedAccountID().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))),
        namedtype.NamedType('accountValueBefore', MoneyAmount().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))),
        namedtype.NamedType('accountValueAfter', MoneyAmount().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2))),
        namedtype.OptionalNamedType('accountDeductedAmount', MoneyAmount().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 3))))

class BonusDedicatedAccount(univ.Sequence): 
    componentType = namedtype.NamedTypes( 
        namedtype.NamedType('dedicatedAccountID', DedicatedAccountID().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))),
        namedtype.OptionalNamedType('campaignIdentifier', CampaignIdentifier().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))),
        namedtype.NamedType('accountValueBefore', MoneyAmount().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2))),
        namedtype.NamedType('accountValueAfter', MoneyAmount().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 3))),
        namedtype.NamedType('bonusAmount', MoneyAmount().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 4))),
        namedtype.OptionalNamedType('accountExpiryDateBefore', Date().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 5))),
        namedtype.OptionalNamedType('accountExpiryDateAfter', Date().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 6))),
        namedtype.OptionalNamedType('accountStartDateBefore', Date().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 7))),
        namedtype.OptionalNamedType('accountStartDateAfter', Date().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 8))))

class CdrOutputData(univ.Sequence): 
    componentType = namedtype.NamedTypes( 
        namedtype.NamedType('externalParameterName', ExternalParameterName().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))),
        namedtype.NamedType('externalParameterValue', ExternalParameterValue().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))))

class ChangedPam(univ.Sequence): 
    componentType = namedtype.NamedTypes( 
        namedtype.OptionalNamedType('pamClassIDBefore', PamClassID().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))),
        namedtype.NamedType('pamClassIDAfter', PamClassID().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))),
        namedtype.OptionalNamedType('scheduleIDBefore', ScheduleID().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2))),
        namedtype.NamedType('scheduleIDAfter', ScheduleID().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 3))),
        namedtype.OptionalNamedType('pamPeriodBefore', PamPeriod().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 4))),
        namedtype.NamedType('pamPeriodUsed', PamPeriod().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 5))),
        namedtype.NamedType('pamPeriodAfter', PamPeriod().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 6))),
        namedtype.OptionalNamedType('deferredToDateBefore', Date().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 7))),
        namedtype.OptionalNamedType('deferredToDateAfter', Date().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 8))),
        namedtype.OptionalNamedType('pamServicePriorityBefore', PamServicePriority().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 9))),
        namedtype.OptionalNamedType('pamServicePriorityAfter', PamServicePriority().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 10))))

class ClearedSubDedicatedAccount(univ.Sequence): 
    componentType = namedtype.NamedTypes( 
        namedtype.NamedType('dedicatedAccountID', DedicatedAccountID().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))),
        namedtype.OptionalNamedType('clearedAccountValue', MoneyAmount().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))),
        namedtype.OptionalNamedType('accountCreditClearedReason', Reason().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2))),
        namedtype.OptionalNamedType('accountExpiryDate', Date().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 3))),
        namedtype.OptionalNamedType('accountStartDate', Date().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 4))),
        namedtype.OptionalNamedType('clearedAccountUnit', MultiUnits().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 5))))

class DedicatedAccountInfo(univ.Sequence): 
    componentType = namedtype.NamedTypes( 
        namedtype.NamedType('dedicatedAccountID', DedicatedAccountID().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))),
        namedtype.OptionalNamedType('campaignIdentifier', CampaignIdentifier().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))),
        namedtype.OptionalNamedType('accountValue', MoneyAmount().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2))),
        namedtype.OptionalNamedType('accountExpiryDate', Date().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 3))),
        namedtype.OptionalNamedType('accountStartDate', Date().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 4))),
        namedtype.OptionalNamedType('realMoney', univ.Boolean().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 5))),
        namedtype.OptionalNamedType('offerID', OfferID().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 6))),
        namedtype.OptionalNamedType('accountUnitType', AccountUnitType().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 7))),
        namedtype.OptionalNamedType('subDedicatedAccountsInfo', univ.SequenceOf(componentType=SubDedicatedAccountInfo()).subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 8))),
        namedtype.OptionalNamedType('accountUnit', MultiUnits().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 9))),
        namedtype.OptionalNamedType('pamServiceID', PamServiceID().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 10))),
        namedtype.OptionalNamedType('productID', ProductID().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 11))),
        namedtype.OptionalNamedType('externalProductID', ExternalProductID().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 12))))

class EvaluatedPam(univ.Sequence): 
    componentType = namedtype.NamedTypes( 
        namedtype.NamedType('pamClassID', PamClassID().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))),
        namedtype.NamedType('scheduleID', ScheduleID().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))),
        namedtype.NamedType('pamPeriodUsed', PamPeriod().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2))),
        namedtype.OptionalNamedType('pamPeriodAfter', PamPeriod().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 3))),
        namedtype.OptionalNamedType('deferredToDateBefore', Date().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 4))),
        namedtype.OptionalNamedType('deferredToDateAfter', Date().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 5))),
        namedtype.OptionalNamedType('pamServicePriority', PamServicePriority().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 6))))

class FloatingDecimal(univ.Sequence): 
    componentType = namedtype.NamedTypes( 
        namedtype.NamedType('digits', Integer64().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))),
        namedtype.NamedType('decimals', Integer32().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))))

class GlobalParameter(univ.Sequence): 
    componentType = namedtype.NamedTypes( 
        namedtype.NamedType('globalParameterName', GlobalParameterName().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))),
        namedtype.NamedType('globalParameterAction', AdjustmentAction().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))),
        namedtype.OptionalNamedType('globalParameterDecimalValueOld', FloatingDecimal().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 2))),
        namedtype.OptionalNamedType('globalParameterDecimalValueNew', FloatingDecimal().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 3))),
        namedtype.OptionalNamedType('globalParameterIntegerValueOld', Integer64().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 4))),
        namedtype.OptionalNamedType('globalParameterIntegerValueNew', Integer64().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 5))),
        namedtype.OptionalNamedType('globalParameterDateValue', Date().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 6))),
        namedtype.OptionalNamedType('globalParameterStringValue', GlobalParameterString().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 7))))

class LifeCycleInformation(univ.Sequence): 
    componentType = namedtype.NamedTypes( 
        namedtype.OptionalNamedType('supervisionExpDateBefore', Date().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))),
        namedtype.OptionalNamedType('supervisionExpDateAfter', Date().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))),
        namedtype.OptionalNamedType('creditClearancePeriodBefore', Period().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2))),
        namedtype.OptionalNamedType('creditClearancePeriodAfter', Period().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 3))),
        namedtype.OptionalNamedType('servFeeExpDateBefore', Date().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 4))),
        namedtype.OptionalNamedType('servFeeExpDateAfter', Date().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 5))),
        namedtype.OptionalNamedType('serviceRemovalPeriodBefore', Period().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 6))),
        namedtype.OptionalNamedType('serviceRemovalPeriodAfter', Period().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 7))),
        namedtype.OptionalNamedType('accountFlagsBefore', AccountFlags().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 8))),
        namedtype.OptionalNamedType('accountFlagsAfter', AccountFlags().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 9))))

class MidCycleReratingData(univ.Sequence): 
    componentType = namedtype.NamedTypes( 
        namedtype.NamedType('midCycleReratingState', MidCycleReratingState().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))),
        namedtype.NamedType('midCycleReratingStateChangeReason', MidCycleReratingStateChangeReason().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))),
        namedtype.NamedType('jobId', Unsigned32().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2))),
        namedtype.NamedType('subsetId', Unsigned32().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 3))),
        namedtype.NamedType('run', Unsigned32().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 4))),
        namedtype.NamedType('sessionId', Unsigned32().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 5))))

class MonetaryUnits(univ.Sequence): 
    componentType = namedtype.NamedTypes( 
        namedtype.NamedType('amount', Integer64().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))),
        namedtype.NamedType('decimals', Integer32().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))),
        namedtype.NamedType('currency', Unsigned32().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2))))

class OfferAttributeInfo(univ.Sequence): 
    componentType = namedtype.NamedTypes( 
        namedtype.NamedType('offerID', OfferID().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))),
        namedtype.OptionalNamedType('productID', ProductID().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))),
        namedtype.OptionalNamedType('attributes', univ.SequenceOf(componentType=AttributeInfo()).subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 2))),
        namedtype.OptionalNamedType('productOfferingName', ProductOfferingName().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 3))))

class OfferInfo(univ.Sequence): 
    componentType = namedtype.NamedTypes( 
        namedtype.NamedType('offerID', OfferID().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))),
        namedtype.OptionalNamedType('offerStartDate', Date().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))),
        namedtype.OptionalNamedType('offerExpiryDate', Date().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2))),
        namedtype.OptionalNamedType('pamServiceID', PamServiceID().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 3))),
        namedtype.OptionalNamedType('productID', ProductID().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 4))),
        namedtype.OptionalNamedType('offerStartDateTime', TimeStamp().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 5))),
        namedtype.OptionalNamedType('offerExpiryDateTime', TimeStamp().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 6))),
        namedtype.OptionalNamedType('externalProductID', ExternalProductID().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 7))),
        namedtype.OptionalNamedType('productOfferingName', ProductOfferingName().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 8))))

class PamEventData(univ.Choice): 
    componentType = namedtype.NamedTypes( 
        namedtype.NamedType('evaluatedPam', EvaluatedPam().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 0))),
        namedtype.NamedType('changedPam', ChangedPam().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1))))


class PeriodicAccountMgmtData(univ.Sequence): 
    componentType = namedtype.NamedTypes( 
        namedtype.NamedType('pamServiceID', PamServiceID().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))),
        namedtype.NamedType('pamClassID', PamClassID().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))),
        namedtype.NamedType('scheduleID', ScheduleID().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2))),
        namedtype.NamedType('currentPamPeriod', PamPeriod().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 3))),
        namedtype.OptionalNamedType('pamServicePriority', PamServicePriority().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 4))))

class PeriodicAccountMgmtDataLCY(univ.Sequence): 
    componentType = namedtype.NamedTypes( 
        namedtype.NamedType('periodicAccountMgmtData', PeriodicAccountMgmtData().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 0))),
        namedtype.OptionalNamedType('deferredToDate', Date().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))),
        namedtype.OptionalNamedType('lastEvaluationDate', Date().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2))))

class RemovedGlobalParameter(univ.Sequence): 
    componentType = namedtype.NamedTypes( 
        namedtype.NamedType('globalParameterName', GlobalParameterName().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))),
        namedtype.OptionalNamedType('globalParameterDecimalValue', FloatingDecimal().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1))),
        namedtype.OptionalNamedType('globalParameterIntegerValue', Integer64().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2))),
        namedtype.OptionalNamedType('globalParameterDateValue', Date().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 3))),
        namedtype.OptionalNamedType('globalParameterStringValue', GlobalParameterString().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 4))))

class Schedule(univ.Sequence): 
    componentType = namedtype.NamedTypes( 
        namedtype.NamedType('scheduledFrequency', ScheduledFrequency().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))),
        namedtype.OptionalNamedType('scheduledInterval', ScheduledInterval().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))),
        namedtype.OptionalNamedType('scheduledMonth', univ.SequenceOf(componentType=Month()).subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 2))),
        namedtype.OptionalNamedType('scheduledDayOfMonth', univ.SequenceOf(componentType=DayOfMonth()).subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 3))),
        namedtype.OptionalNamedType('scheduledDayOfWeek', univ.SequenceOf(componentType=DayOfWeek()).subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 4))),
        namedtype.OptionalNamedType('scheduledHour', Hour().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 5))),
        namedtype.OptionalNamedType('scheduledMinute', Minute().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 6))),
        namedtype.OptionalNamedType('scheduledSecond', Second().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 7))))

class SelectionTreeParameter(univ.Sequence): 
    componentType = namedtype.NamedTypes( 
        namedtype.NamedType('selectionTreeID', char.UTF8String().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))),
        namedtype.NamedType('selectionTreeVersion', char.UTF8String().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))),
        namedtype.NamedType('selectionTreeType', SelectionTreeType().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2))))

class TreeParameter(univ.Sequence): 
    componentType = namedtype.NamedTypes( 
        namedtype.NamedType('treeParameterName', TreeParameterName().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))),
        namedtype.NamedType('treeParameterAction', AdjustmentAction().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))),
        namedtype.OptionalNamedType('treeParameterDecimalValueOld', FloatingDecimal().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 2))),
        namedtype.OptionalNamedType('treeParameterDecimalValueNew', FloatingDecimal().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 3))),
        namedtype.OptionalNamedType('treeParameterIntegerValueOld', Integer64().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 4))),
        namedtype.OptionalNamedType('treeParameterIntegerValueNew', Integer64().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 5))),
        namedtype.OptionalNamedType('treeParameterDateValue', Date().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 6))),
        namedtype.OptionalNamedType('treeParameterStringValue', TreeParameterString().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 7))),
        namedtype.OptionalNamedType('associatedPartyID', NumberString().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 8))),
        namedtype.OptionalNamedType('forAllSubscribersOnAccount', univ.Boolean().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 9))),
        namedtype.OptionalNamedType('treeParameterScheduleValueOld', Schedule().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 10))),
        namedtype.OptionalNamedType('treeParameterScheduleValueNew', Schedule().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 11))),
        namedtype.OptionalNamedType('treeParameterDayOfWeekValueOld', DayOfWeek().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 12))),
        namedtype.OptionalNamedType('treeParameterDayOfWeekValueNew', DayOfWeek().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 13))),
        namedtype.OptionalNamedType('treeParameterDateRangeValue', DateRange().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 14))),
        namedtype.OptionalNamedType('treeParameterTimeValueOld', Time().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 15))),
        namedtype.OptionalNamedType('treeParameterTimeValueNew', Time().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 16))))

class TreeDefinedFieldType(univ.Choice): 
    componentType = namedtype.NamedTypes( 
        namedtype.NamedType('boolean', univ.Boolean().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))),
        namedtype.NamedType('integer64', Integer64().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2))),
        namedtype.NamedType('date', Date().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 6))),
        namedtype.NamedType('string', char.UTF8String().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 7))),
        namedtype.NamedType('floatingDecimalTDF', FloatingDecimal().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 8))),
        namedtype.NamedType('amountTDF', MonetaryUnits().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 9))),
        namedtype.NamedType('dateSpecial', DateSpecial().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 10))))


class UsageCounterType(univ.Choice): 
    componentType = namedtype.NamedTypes( 
        namedtype.NamedType('usageCounterUnit', Integer64().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))),
        namedtype.NamedType('usageCounterMoney', FloatingDecimal().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1))))


class UsageThreshold(univ.Sequence): 
    componentType = namedtype.NamedTypes( 
        namedtype.NamedType('usageThresholdID', UsageThresholdID().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))),
        namedtype.OptionalNamedType('action', AdjustmentAction().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))),
        namedtype.OptionalNamedType('usageThresholdValueBefore', UsageCounterType().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 2))),
        namedtype.OptionalNamedType('usageThresholdValueAfter', UsageCounterType().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 3))),
        namedtype.OptionalNamedType('associatedPartyID', NumberString().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 4))),
        namedtype.OptionalNamedType('forAllSubscribersOnAccount', univ.Boolean().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 5))))

class BonusAdjustment(univ.Sequence): 
    componentType = namedtype.NamedTypes( 
        namedtype.NamedType('sdpID', NodeID().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))),
        namedtype.NamedType('cdrID', RecordSequenceNumberString().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2))),
        namedtype.NamedType('accountNumber', NumberString().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 3))),
        namedtype.NamedType('subscriberNumber', NumberString().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 4))),
        namedtype.NamedType('bonusTimeStamp', TimeStamp().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 5))),
        namedtype.NamedType('currencyType', CurrencyType().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 6))),
        namedtype.NamedType('serviceClassId', ServiceClass().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 7))),
        namedtype.OptionalNamedType('accountBalanceBeforeBonus', MoneyAmount().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 8))),
        namedtype.OptionalNamedType('accountBalanceAfterBonus', MoneyAmount().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 9))),
        namedtype.OptionalNamedType('bonusAmount', MoneyAmount().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 10))),
        namedtype.OptionalNamedType('subscriberConvergent', univ.Boolean().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 11))),
        namedtype.OptionalNamedType('accountGroupID', AccountGroupID().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 12))),
        namedtype.OptionalNamedType('serviceOfferings', ServiceOfferings().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 13))),
        namedtype.OptionalNamedType('bonusDedicatedAccounts', univ.SequenceOf(componentType=BonusDedicatedAccount()).subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 14))),
        namedtype.OptionalNamedType('bonusAccumulators', univ.SequenceOf(componentType=BonusAccumulator()).subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 15))),
        namedtype.OptionalNamedType('lifeCycleInformation', LifeCycleInformation().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 16))))

class AdjustmentDedicatedAccount(univ.Sequence): 
    componentType = namedtype.NamedTypes( 
        namedtype.NamedType('dedicatedAccountID', DedicatedAccountID().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))),
        namedtype.OptionalNamedType('campaignIdentifier', CampaignIdentifier().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))),
        namedtype.OptionalNamedType('accountValueBefore', MoneyAmount().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2))),
        namedtype.OptionalNamedType('accountValueAfter', MoneyAmount().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 3))),
        namedtype.OptionalNamedType('adjustmentAmount', MoneyAmount().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 4))),
        namedtype.NamedType('action', AdjustmentAction().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 5))),
        namedtype.OptionalNamedType('accountExpiryDateBefore', Date().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 6))),
        namedtype.OptionalNamedType('accountExpiryDateAfter', Date().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 7))),
        namedtype.OptionalNamedType('originalAdjustmentAmount', MoneyAmount().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 8))),
        namedtype.OptionalNamedType('clearedAccountValue', MoneyAmount().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 9))),
        namedtype.OptionalNamedType('accountValueInitial', MoneyAmount().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 10))),
        namedtype.OptionalNamedType('accountExpiryDateInitial', Date().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 11))),
        namedtype.OptionalNamedType('accountCreditClearedReason', Reason().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 12))),
        namedtype.OptionalNamedType('accountStartDateBefore', Date().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 13))),
        namedtype.OptionalNamedType('accountStartDateAfter', Date().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 14))),
        namedtype.OptionalNamedType('accountStartDateInitial', Date().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 15))),
        namedtype.OptionalNamedType('realMoney', univ.Boolean().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 16))),
        namedtype.OptionalNamedType('offerID', OfferID().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 17))),
        namedtype.OptionalNamedType('accountUnitType', AccountUnitType().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 18))),
        namedtype.OptionalNamedType('adjustmentSubDedicatedAccounts', univ.SequenceOf(componentType=AdjustmentSubDedicatedAccount()).subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 19))),
        namedtype.OptionalNamedType('accountUnitBefore', MultiUnits().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 20))),
        namedtype.OptionalNamedType('accountUnitAfter', MultiUnits().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 21))),
        namedtype.OptionalNamedType('adjustmentUnit', MultiUnits().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 22))),
        namedtype.OptionalNamedType('clearedAccountUnit', MultiUnits().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 23))),
        namedtype.OptionalNamedType('accountUnitInitial', MultiUnits().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 24))),
        namedtype.OptionalNamedType('pamServiceID', PamServiceID().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 25))),
        namedtype.OptionalNamedType('productID', ProductID().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 26))),
        namedtype.OptionalNamedType('offerExpiryDate', Date().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 27))),
        namedtype.OptionalNamedType('offerStartDate', Date().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 28))),
        namedtype.OptionalNamedType('externalProductID', ExternalProductID().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 29))),
        namedtype.OptionalNamedType('connectedOfferAttributes', univ.SequenceOf(componentType=OfferAttributeInfo()).subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 30))),
        namedtype.OptionalNamedType('accountValueFullPeriod', MoneyAmount().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 31))),
        namedtype.OptionalNamedType('accountUnitFullPeriod', MultiUnits().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 32))))

class AggregatedBalanceDedicatedAccount(univ.Sequence): 
    componentType = namedtype.NamedTypes( 
        namedtype.NamedType('dedicatedAccountID', DedicatedAccountID().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))),
        namedtype.OptionalNamedType('campaignIdentifier', CampaignIdentifier().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))),
        namedtype.NamedType('accountValueBefore', MoneyAmount().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2))),
        namedtype.NamedType('accountValueAfter', MoneyAmount().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 3))),
        namedtype.OptionalNamedType('accountDeductedAmount', MoneyAmount().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 4))),
        namedtype.OptionalNamedType('offerID', OfferID().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 5))),
        namedtype.OptionalNamedType('aggregatedBalanceSubDedicatedAccounts', univ.SequenceOf(componentType=AggregatedBalanceSubDedicatedAccount()).subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 6))),
        namedtype.OptionalNamedType('offerExpiryDate', Date().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 7))),
        namedtype.OptionalNamedType('offerStartDate', Date().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 8))))

class AttributeChange(univ.Sequence): 
    componentType = namedtype.NamedTypes( 
        namedtype.NamedType('attributeName', char.UTF8String().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))),
        namedtype.NamedType('attributeAction', AdjustmentAction().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))),
        namedtype.OptionalNamedType('attributeValueString', char.UTF8String().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2))),
        namedtype.OptionalNamedType('attributeValueDate', Date().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 3))),
        namedtype.OptionalNamedType('attributeValueDecimal', FloatingDecimal().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 4))),
        namedtype.OptionalNamedType('attributeValueDecimalOld', FloatingDecimal().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 5))),
        namedtype.OptionalNamedType('attributeValueStringOld', char.UTF8String().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 6))),
        namedtype.OptionalNamedType('attributeValueInteger', Integer32().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 7))),
        namedtype.OptionalNamedType('attributeValueIntegerOld', Integer32().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 8))))

class ClearedDedicatedAccount(univ.Sequence): 
    componentType = namedtype.NamedTypes( 
        namedtype.NamedType('dedicatedAccountID', DedicatedAccountID().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))),
        namedtype.OptionalNamedType('campaignIdentifier', CampaignIdentifier().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))),
        namedtype.OptionalNamedType('clearedAccountValue', MoneyAmount().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2))),
        namedtype.OptionalNamedType('accountCreditClearedReason', Reason().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 3))),
        namedtype.OptionalNamedType('accountExpiryDate', Date().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 4))),
        namedtype.OptionalNamedType('accountStartDate', Date().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 5))),
        namedtype.OptionalNamedType('realMoney', univ.Boolean().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 6))),
        namedtype.OptionalNamedType('offerID', OfferID().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 7))),
        namedtype.OptionalNamedType('accountUnitType', AccountUnitType().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 8))),
        namedtype.OptionalNamedType('clearedSubDedicatedAccounts', univ.SequenceOf(componentType=ClearedSubDedicatedAccount()).subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 9))),
        namedtype.OptionalNamedType('clearedAccountUnit', MultiUnits().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 10))),
        namedtype.OptionalNamedType('pamServiceID', PamServiceID().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 11))),
        namedtype.OptionalNamedType('productID', ProductID().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 12))),
        namedtype.OptionalNamedType('offerExpiryDate', Date().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 13))),
        namedtype.OptionalNamedType('offerStartDate', Date().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 14))),
        namedtype.OptionalNamedType('externalProductID', ExternalProductID().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 15))))

class ProductFeeUsageCounter(univ.Sequence): 
    componentType = namedtype.NamedTypes( 
        namedtype.NamedType('usageCounterID', UsageCounterID().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))),
        namedtype.NamedType('usageCounterValueAfter', UsageCounterType().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1))),
        namedtype.NamedType('usageCounterChange', UsageCounterType().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 2))))

class RemovedUsageCounter(univ.Sequence): 
    componentType = namedtype.NamedTypes( 
        namedtype.NamedType('usageCounterID', UsageCounterID().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))),
        namedtype.OptionalNamedType('usageCounterValue', UsageCounterType().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1))),
        namedtype.OptionalNamedType('associatedPartyID', NumberString().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2))),
        namedtype.OptionalNamedType('productID', ProductID().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 3))),
        namedtype.OptionalNamedType('externalProductID', ExternalProductID().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 4))))

class Tree(univ.Sequence): 
    componentType = namedtype.NamedTypes( 
        namedtype.NamedType('serviceProvider', ServiceProvider().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))),
        namedtype.OptionalNamedType('treeParameters', univ.SequenceOf(componentType=TreeParameter()).subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1))))

class TreeDefinedField(univ.Sequence): 
    componentType = namedtype.NamedTypes( 
        namedtype.NamedType('parameterID', char.UTF8String().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))),
        namedtype.NamedType('parameterValue', TreeDefinedFieldType().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1))))

class UnchangedUsageCounter(univ.Sequence): 
    componentType = namedtype.NamedTypes( 
        namedtype.NamedType('usageCounterID', UsageCounterID().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))),
        namedtype.OptionalNamedType('usageCounterValue', UsageCounterType().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1))),
        namedtype.OptionalNamedType('associatedPartyID', NumberString().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2))),
        namedtype.OptionalNamedType('productID', ProductID().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 3))),
        namedtype.OptionalNamedType('externalProductID', ExternalProductID().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 4))))

class UsageCounter(univ.Sequence): 
    componentType = namedtype.NamedTypes( 
        namedtype.NamedType('usageCounterID', UsageCounterID().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))),
        namedtype.OptionalNamedType('action', AdjustmentAction().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))),
        namedtype.OptionalNamedType('usageCounterValueBefore', UsageCounterType().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 2))),
        namedtype.OptionalNamedType('usageCounterValueAfter', UsageCounterType().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 3))),
        namedtype.OptionalNamedType('usageCounterChange', UsageCounterType().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 4))),
        namedtype.OptionalNamedType('associatedPartyID', NumberString().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 5))),
        namedtype.OptionalNamedType('productID', ProductID().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 6))),
        namedtype.OptionalNamedType('externalProductID', ExternalProductID().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 7))),
        namedtype.OptionalNamedType('connectedOfferAttributes', univ.SequenceOf(componentType=OfferAttributeInfo()).subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 8))),
        namedtype.OptionalNamedType('forAllSubscribersOnAccount', univ.Boolean().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 9))))

class NegativeBalance(univ.Sequence): 
    componentType = namedtype.NamedTypes( 
        namedtype.NamedType('accountNumber', NumberString().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))),
        namedtype.NamedType('accountBalanceBefore', MoneyAmount().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2))),
        namedtype.NamedType('accountBalanceAfter', MoneyAmount().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 3))),
        namedtype.NamedType('timeStamp', TimeStamp().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 4))),
        namedtype.OptionalNamedType('sdpID', NodeID().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 5))),
        namedtype.OptionalNamedType('cdrID', RecordSequenceNumberString().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 6))),
        namedtype.OptionalNamedType('subscriberConvergent', univ.Boolean().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 7))),
        namedtype.OptionalNamedType('aggregatedBalanceBefore', MoneyAmount().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 8))),
        namedtype.OptionalNamedType('aggregatedBalanceAfter', MoneyAmount().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 9))),
        namedtype.OptionalNamedType('aggregatedBalanceDedicatedAccounts', univ.SequenceOf(componentType=AggregatedBalanceDedicatedAccount()).subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 10))))

class AdjustmentOffer(univ.Sequence): 
    componentType = namedtype.NamedTypes( 
        namedtype.NamedType('offerID', OfferID().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))),
        namedtype.NamedType('action', AdjustmentAction().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))),
        namedtype.OptionalNamedType('offerExpiryDateBefore', Date().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2))),
        namedtype.OptionalNamedType('offerExpiryDateAfter', Date().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 3))),
        namedtype.OptionalNamedType('offerExpiryDateInitial', Date().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 4))),
        namedtype.OptionalNamedType('offerStartDateBefore', Date().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 5))),
        namedtype.OptionalNamedType('offerStartDateAfter', Date().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 6))),
        namedtype.OptionalNamedType('offerStartDateInitial', Date().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 7))),
        namedtype.OptionalNamedType('reason', Reason().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 8))),
        namedtype.OptionalNamedType('offerType', OfferType().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 9))),
        namedtype.OptionalNamedType('offerDisabledBefore', univ.Boolean().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 10))),
        namedtype.OptionalNamedType('offerDisabledAfter', univ.Boolean().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 11))),
        namedtype.OptionalNamedType('offerExpiryDateTimeBefore', TimeStamp().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 12))),
        namedtype.OptionalNamedType('offerExpiryDateTimeAfter', TimeStamp().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 13))),
        namedtype.OptionalNamedType('offerExpiryDateTimeInitial', TimeStamp().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 14))),
        namedtype.OptionalNamedType('offerStartDateTimeBefore', TimeStamp().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 15))),
        namedtype.OptionalNamedType('offerStartDateTimeAfter', TimeStamp().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 16))),
        namedtype.OptionalNamedType('offerStartDateTimeInitial', TimeStamp().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 17))),
        namedtype.OptionalNamedType('pamServiceID', PamServiceID().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 18))),
        namedtype.OptionalNamedType('offerProviderIDBefore', NumberString().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 19))),
        namedtype.OptionalNamedType('offerProviderIDAfter', NumberString().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 20))),
        namedtype.OptionalNamedType('productID', ProductID().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 21))),
        namedtype.OptionalNamedType('offerAttributeChanges', univ.SequenceOf(componentType=AttributeChange()).subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 22))),
        namedtype.OptionalNamedType('offerAttributeInfo', univ.SequenceOf(componentType=AttributeInfo()).subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 23))),
        namedtype.OptionalNamedType('externalProductID', ExternalProductID().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 24))),
        namedtype.OptionalNamedType('productOfferingName', ProductOfferingName().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 25))),
        namedtype.OptionalNamedType('trees', univ.SequenceOf(componentType=Tree()).subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 26))),
        namedtype.OptionalNamedType('offerPeriodStartDate', Date().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 27))),
        namedtype.OptionalNamedType('offerPeriodStartDateTime', TimeStamp().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 28))))

class AdjustmentPredefinedOfferValue(univ.Sequence): 
    componentType = namedtype.NamedTypes( 
        namedtype.NamedType('offerID', OfferID().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))),
        namedtype.OptionalNamedType('productOfferingName', ProductOfferingName().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))),
        namedtype.OptionalNamedType('offerAttributeChanges', univ.SequenceOf(componentType=AttributeChange()).subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 2))),
        namedtype.OptionalNamedType('trees', univ.SequenceOf(componentType=Tree()).subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 3))))

class PeriodicAccountMgmtService(univ.Sequence): 
    componentType = namedtype.NamedTypes( 
        namedtype.NamedType('pamServiceID', PamServiceID().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))),
        namedtype.NamedType('pamEventData', PamEventData().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1))),
        namedtype.OptionalNamedType('lastEvaluationDate', Date().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2))),
        namedtype.OptionalNamedType('pamIndicator', PamIndicator().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 3))),
        namedtype.NamedType('selectionTreeInfo', univ.SequenceOf(componentType=SelectionTreeParameter()).subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 4))),
        namedtype.OptionalNamedType('balanceBefore', MoneyAmount().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 5))),
        namedtype.NamedType('balanceAfter', MoneyAmount().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 6))),
        namedtype.OptionalNamedType('deltaAmount', MoneyAmount().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 7))),
        namedtype.OptionalNamedType('oldAccountGroupID', AccountGroupID().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 8))),
        namedtype.OptionalNamedType('newAccountGroupID', AccountGroupID().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 9))),
        namedtype.OptionalNamedType('oldServiceOfferings', ServiceOfferings().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 10))),
        namedtype.OptionalNamedType('newServiceOfferings', ServiceOfferings().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 11))),
        namedtype.OptionalNamedType('adjustmentDedicatedAccounts', univ.SequenceOf(componentType=AdjustmentDedicatedAccount()).subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 12))),
        namedtype.OptionalNamedType('adjustmentAccumulators', univ.SequenceOf(componentType=AdjustmentAccumulator()).subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 13))),
        namedtype.OptionalNamedType('treeDefinedFields', univ.SequenceOf(componentType=TreeDefinedField()).subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 14))),
        namedtype.OptionalNamedType('lifeCycleInformation', LifeCycleInformation().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 15))),
        namedtype.OptionalNamedType('aggregatedBalanceBefore', MoneyAmount().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 16))),
        namedtype.OptionalNamedType('aggregatedBalanceAfter', MoneyAmount().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 17))),
        namedtype.OptionalNamedType('forAllSubscribersOnAccount', univ.Boolean().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 18))),
        namedtype.OptionalNamedType('adjustmentUsageCounters', univ.SequenceOf(componentType=UsageCounter()).subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 19))),
        namedtype.OptionalNamedType('adjustmentOffers', univ.SequenceOf(componentType=AdjustmentOffer()).subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 20))),
        namedtype.OptionalNamedType('oldCommunityID1', CommunityID().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 21))),
        namedtype.OptionalNamedType('oldCommunityID2', CommunityID().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 22))),
        namedtype.OptionalNamedType('oldCommunityID3', CommunityID().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 23))),
        namedtype.OptionalNamedType('newCommunityID1', CommunityID().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 24))),
        namedtype.OptionalNamedType('newCommunityID2', CommunityID().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 25))),
        namedtype.OptionalNamedType('newCommunityID3', CommunityID().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 26))),
        namedtype.OptionalNamedType('oldServiceClass', ServiceClass().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 27))),
        namedtype.OptionalNamedType('newServiceClass', ServiceClass().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 28))),
        namedtype.OptionalNamedType('adjustmentUsageThresholds', univ.SequenceOf(componentType=UsageThreshold()).subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 29))))

class ProductFee(univ.Sequence): 
    componentType = namedtype.NamedTypes( 
        namedtype.NamedType('offerID', OfferID().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))),
        namedtype.NamedType('productID', ProductID().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))),
        namedtype.NamedType('fee', MoneyAmount().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2))),
        namedtype.OptionalNamedType('productFeeMainAccount', ProductFeeMainAccount().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 3))),
        namedtype.OptionalNamedType('productFeeDedicatedAccounts', univ.SequenceOf(componentType=ProductFeeDedicatedAccount()).subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 4))),
        namedtype.OptionalNamedType('productFeeUsageCounters', univ.SequenceOf(componentType=ProductFeeUsageCounter()).subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 5))),
        namedtype.OptionalNamedType('fullPeriodFee', MoneyAmount().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 6))),
        namedtype.OptionalNamedType('productFeeDiscountFactor', Percent().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 7))))

class RemovedOffer(univ.Sequence): 
    componentType = namedtype.NamedTypes( 
        namedtype.NamedType('offerID', OfferID().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))),
        namedtype.OptionalNamedType('offerExpiryDate', Date().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))),
        namedtype.OptionalNamedType('offerStartDate', Date().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2))),
        namedtype.OptionalNamedType('reason', Reason().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 3))),
        namedtype.OptionalNamedType('offerType', OfferType().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 4))),
        namedtype.OptionalNamedType('offerDisabled', univ.Boolean().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 5))),
        namedtype.OptionalNamedType('offerExpiryDateTime', TimeStamp().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 6))),
        namedtype.OptionalNamedType('offerStartDateTime', TimeStamp().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 7))),
        namedtype.OptionalNamedType('pamServiceID', PamServiceID().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 8))),
        namedtype.OptionalNamedType('offerProviderID', NumberString().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 9))),
        namedtype.OptionalNamedType('productID', ProductID().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 10))),
        namedtype.OptionalNamedType('offerAttributeChanges', univ.SequenceOf(componentType=AttributeChange()).subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 11))),
        namedtype.OptionalNamedType('offerAttributeInfo', univ.SequenceOf(componentType=AttributeInfo()).subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 12))),
        namedtype.OptionalNamedType('externalProductID', ExternalProductID().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 13))),
        namedtype.OptionalNamedType('productOfferingName', ProductOfferingName().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 14))),
        namedtype.OptionalNamedType('trees', univ.SequenceOf(componentType=Tree()).subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 15))))

class RemovedPredefinedOfferValue(univ.Sequence): 
    componentType = namedtype.NamedTypes( 
        namedtype.NamedType('offerID', OfferID().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))),
        namedtype.OptionalNamedType('productOfferingName', ProductOfferingName().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))),
        namedtype.OptionalNamedType('offerAttributeChanges', univ.SequenceOf(componentType=AttributeChange()).subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 2))),
        namedtype.OptionalNamedType('trees', univ.SequenceOf(componentType=Tree()).subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 3))))

class TimeBasedAction(univ.Sequence): 
    componentType = namedtype.NamedTypes( 
        namedtype.NamedType('offerID', OfferID().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))),
        namedtype.OptionalNamedType('productID', ProductID().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2))),
        namedtype.NamedType('timeBasedActionType', TimeBasedActionType().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 3))),
        namedtype.NamedType('timeBasedActionTimeStamp', TimeStamp().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 4))),
        namedtype.OptionalNamedType('productOfferingName', ProductOfferingName().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 5))),
        namedtype.OptionalNamedType('attributes', univ.SequenceOf(componentType=AttributeInfo()).subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 6))),
        namedtype.OptionalNamedType('adjustmentOffers', univ.SequenceOf(componentType=AdjustmentOffer()).subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 7))),
        namedtype.OptionalNamedType('adjustmentDedicatedAccounts', univ.SequenceOf(componentType=AdjustmentDedicatedAccount()).subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 8))),
        namedtype.OptionalNamedType('adjustmentUsageCounters', univ.SequenceOf(componentType=UsageCounter()).subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 9))),
        namedtype.OptionalNamedType('productFees', univ.SequenceOf(componentType=ProductFee()).subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 10))))

class AccountAdjustment(univ.Sequence): 
    componentType = namedtype.NamedTypes( 
        namedtype.NamedType('adjustmentRecordType', AdjustmentRecordType().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))),
        namedtype.NamedType('sdpID', NodeID().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2))),
        namedtype.NamedType('cdrID', RecordSequenceNumberString().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 3))),
        namedtype.NamedType('accountNumber', NumberString().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 4))),
        namedtype.NamedType('subscriberNumber', NumberString().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 5))),
        namedtype.NamedType('adjustmentTimeStamp', TimeStamp().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 6))),
        namedtype.OptionalNamedType('adjustmentAction', AdjustmentAction().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 7))),
        namedtype.OptionalNamedType('balanceBefore', MoneyAmount().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 8))),
        namedtype.OptionalNamedType('balanceAfter', MoneyAmount().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 9))),
        namedtype.OptionalNamedType('adjustmentAmount', MoneyAmount().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 10))),
        namedtype.NamedType('serviceClassId', ServiceClass().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 11))),
        namedtype.NamedType('currencyType', CurrencyType().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 12))),
        namedtype.OptionalNamedType('originalAdjustmentAmount', MoneyAmount().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 13))),
        namedtype.OptionalNamedType('originalCurrencyType', CurrencyType().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 14))),
        namedtype.OptionalNamedType('originNodeType', NodeType().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 15))),
        namedtype.OptionalNamedType('originNodeId', IDString().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 16))),
        namedtype.OptionalNamedType('origTransactionID', TransactionID().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 17))),
        namedtype.OptionalNamedType('origTransactionTimeStamp', TimeStamp().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 18))),
        namedtype.OptionalNamedType('transactionType', TransactionType().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 19))),
        namedtype.OptionalNamedType('transactionCode', TransactionCode().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 20))),
        namedtype.OptionalNamedType('originOperatorId', IDString().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 21))),
        namedtype.OptionalNamedType('supervisionExpDateBefore', Date().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 22))),
        namedtype.OptionalNamedType('supervisionExpDateAfter', Date().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 23))),
        namedtype.OptionalNamedType('creditClearancePeriodBefore', Period().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 24))),
        namedtype.OptionalNamedType('creditClearancePeriodAfter', Period().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 25))),
        namedtype.OptionalNamedType('servFeeExpDateBefore', Date().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 26))),
        namedtype.OptionalNamedType('servFeeExpDateAfter', Date().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 27))),
        namedtype.OptionalNamedType('serviceRemovalPeriodBefore', Period().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 28))),
        namedtype.OptionalNamedType('serviceRemovalPeriodAfter', Period().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 29))),
        namedtype.OptionalNamedType('accountFlagsBefore', AccountFlags().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 30))),
        namedtype.OptionalNamedType('accountFlagsAfter', AccountFlags().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 31))),
        namedtype.OptionalNamedType('newServiceClass', ServiceClass().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 32))),
        namedtype.OptionalNamedType('valueVoucherExpDateBefore', Date().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 33))),
        namedtype.OptionalNamedType('valueVoucherExpDateAfter', Date().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 34))),
        namedtype.OptionalNamedType('temporaryServiceClassBefore', ServiceClass().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 35))),
        namedtype.OptionalNamedType('temporaryServiceClassAfter', ServiceClass().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 36))),
        namedtype.OptionalNamedType('activationDate', Date().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 37))),
        namedtype.OptionalNamedType('refillUnbarTimeStamp', TimeStamp().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 38))),
        namedtype.OptionalNamedType('oldLanguage', Language().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 39))),
        namedtype.OptionalNamedType('newLanguage', Language().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 40))),
        namedtype.OptionalNamedType('promotionPlanIDBefore', PromotionPlan().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 41))),
        namedtype.OptionalNamedType('promotionPlanIDAfter', PromotionPlan().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 42))),
        namedtype.OptionalNamedType('negativeBalanceBarringDate', Date().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 43))),
        namedtype.OptionalNamedType('oldAccountGroupID', AccountGroupID().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 44))),
        namedtype.OptionalNamedType('oldServiceOfferings', ServiceOfferings().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 45))),
        namedtype.OptionalNamedType('oldCommunityID1', CommunityID().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 46))),
        namedtype.OptionalNamedType('oldCommunityID2', CommunityID().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 47))),
        namedtype.OptionalNamedType('oldCommunityID3', CommunityID().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 48))),
        namedtype.OptionalNamedType('newAccountGroupID', AccountGroupID().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 49))),
        namedtype.OptionalNamedType('newServiceOfferings', ServiceOfferings().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 50))),
        namedtype.OptionalNamedType('subscriberConvergent', univ.Boolean().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 51))),
        namedtype.OptionalNamedType('newCommunityID1', CommunityID().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 52))),
        namedtype.OptionalNamedType('newCommunityID2', CommunityID().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 53))),
        namedtype.OptionalNamedType('newCommunityID3', CommunityID().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 54))),
        namedtype.OptionalNamedType('counterTypeID', univ.Integer().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 55))),
        namedtype.OptionalNamedType('totalCounterStartValue', CounterValue().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 56))),
        namedtype.OptionalNamedType('totalCounterDeltaValue', CounterDelta().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 57))),
        namedtype.OptionalNamedType('periodCounterStartValue', CounterValue().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 58))),
        namedtype.OptionalNamedType('periodCounterDeltaValue', CounterDelta().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 59))),
        namedtype.OptionalNamedType('deductedAmount', MoneyAmount().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 60))),
        namedtype.OptionalNamedType('cost', MoneyAmount().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 61))),
        namedtype.OptionalNamedType('costService', MoneyAmount().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 62))),
        namedtype.OptionalNamedType('presentedCost', MoneyAmount().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 63))),
        namedtype.OptionalNamedType('chargingSuccessCode', ChargingSuccessCode().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 64))),
        namedtype.OptionalNamedType('chargingIndicator', univ.Integer().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 65))),
        namedtype.OptionalNamedType('familyAndFriendsAction', FamilyAndFriendsAction().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 66))),
        namedtype.OptionalNamedType('familyAndFriendsNumber', NumberString().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 67))),
        namedtype.OptionalNamedType('familyAndFriendsIndicator', FamilyAndFriendsIndicator().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 68))),
        namedtype.OptionalNamedType('owner', Owner().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 69))),
        namedtype.OptionalNamedType('accountHomeRegion', AccountHomeRegion().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 70))),
        namedtype.OptionalNamedType('changedPIN', univ.Boolean().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 71))),
        namedtype.OptionalNamedType('accountUnbarSuppressed', univ.Boolean().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 72))),
        namedtype.OptionalNamedType('adjustmentDedicatedAccounts', univ.SequenceOf(componentType=AdjustmentDedicatedAccount()).subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 73))),
        namedtype.OptionalNamedType('adjustmentAccumulators', univ.SequenceOf(componentType=AdjustmentAccumulator()).subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 74))),
        namedtype.OptionalNamedType('origServiceClassBefore', ServiceClass().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 75))),
        namedtype.OptionalNamedType('origServiceClassAfter', ServiceClass().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 76))),
        namedtype.OptionalNamedType('serviceSessionID', char.UTF8String().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 77))),
        namedtype.OptionalNamedType('duplicatingCDRNode', NodeType().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 78))),
        namedtype.OptionalNamedType('aggregatedBalanceBefore', MoneyAmount().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 79))),
        namedtype.OptionalNamedType('aggregatedBalanceAfter', MoneyAmount().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 80))),
        namedtype.OptionalNamedType('adjustmentFaFs', univ.SequenceOf(componentType=AdjustmentFaF()).subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 81))),
        namedtype.OptionalNamedType('adjustmentOffers', univ.SequenceOf(componentType=AdjustmentOffer()).subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 82))),
        namedtype.OptionalNamedType('lastRecord', univ.Boolean().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 83))),
        namedtype.OptionalNamedType('adjustmentPeriodicAccountMgmt', univ.SequenceOf(componentType=AdjustmentPeriodicAccountMgmt()).subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 84))),
        namedtype.OptionalNamedType('forAllSubscribersOnAccount', univ.Boolean().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 85))),
        namedtype.OptionalNamedType('adjustmentUsageCounters', univ.SequenceOf(componentType=UsageCounter()).subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 86))),
        namedtype.OptionalNamedType('adjustmentUsageThresholds', univ.SequenceOf(componentType=UsageThreshold()).subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 87))),
        namedtype.OptionalNamedType('modifiedSubscriberNumber', NumberString().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 88))),
        namedtype.OptionalNamedType('modifiedSubscriberNumberExpiryDate', Date().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 89))),
        namedtype.OptionalNamedType('suppressedCost', MoneyAmount().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 90))),
        namedtype.OptionalNamedType('adjustmentTransactionType', AdjustmentTransactionType().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 91))),
        namedtype.OptionalNamedType('eocnSelectionIdBefore', EocnSelectionId().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 92))),
        namedtype.OptionalNamedType('eocnSelectionIdAfter', EocnSelectionId().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 93))),
        namedtype.OptionalNamedType('accountPrepaidEmptyLimitBefore', MoneyAmount().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 94))),
        namedtype.OptionalNamedType('accountPrepaidEmptyLimitAfter', MoneyAmount().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 95))),
        namedtype.OptionalNamedType('accountHomeTimeZoneBefore', TimeZone().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 96))),
        namedtype.OptionalNamedType('accountHomeTimeZoneAfter', TimeZone().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 97))),
        namedtype.OptionalNamedType('periodicAccountMgmtBillCycleData', PeriodicAccountMgmtData().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 98))),
        namedtype.OptionalNamedType('accountStateSequenceNumber', Unsigned63().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 99))),
        namedtype.OptionalNamedType('requestData', univ.OctetString().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 100))),
        namedtype.OptionalNamedType('midCycleReratingData', MidCycleReratingData().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 101))),
        namedtype.OptionalNamedType('backdateTimeStamp', TimeStamp().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 102))),
        namedtype.OptionalNamedType('backdateBillCyclePeriod', PamPeriod().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 103))),
        namedtype.OptionalNamedType('providerNumber', NumberString().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 104))),
        namedtype.OptionalNamedType('oldProviderNumber', NumberString().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 105))),
        namedtype.OptionalNamedType('newProviderNumber', NumberString().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 106))),
        namedtype.OptionalNamedType('periodicAccountMgmtRerateCycleData', PeriodicAccountMgmtData().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 107))),
        namedtype.OptionalNamedType('adjustmentPredefinedOfferValues', univ.SequenceOf(componentType=AdjustmentPredefinedOfferValue()).subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 108))),
        namedtype.OptionalNamedType('adjustmentGlobalParameterValues', univ.SequenceOf(componentType=GlobalParameter()).subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 109))),
        namedtype.OptionalNamedType('cdrOutputData', univ.SequenceOf(componentType=CdrOutputData()).subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 110))))

class ServiceFeeDeduction(univ.Sequence): 
    componentType = namedtype.NamedTypes( 
        namedtype.NamedType('sdpID', NodeID().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))),
        namedtype.NamedType('cdrID', RecordSequenceNumberString().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2))),
        namedtype.NamedType('originNodeType', NodeType().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 3))),
        namedtype.NamedType('timeStamp', TimeStamp().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 4))),
        namedtype.NamedType('accountNumber', NumberString().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 5))),
        namedtype.NamedType('serviceFeeAmount', MoneyAmount().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 6))),
        namedtype.NamedType('successCode', ServFeeDeductSuccessCode().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 7))),
        namedtype.NamedType('oldServiceClass', ServiceClass().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 8))),
        namedtype.OptionalNamedType('newServiceClass', ServiceClass().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 9))),
        namedtype.NamedType('currencyType', CurrencyType().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 10))),
        namedtype.OptionalNamedType('servFeeExpDateBefore', Date().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 11))),
        namedtype.OptionalNamedType('servFeeExpDateAfter', Date().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 12))),
        namedtype.NamedType('accountFlags', AccountFlags().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 13))),
        namedtype.OptionalNamedType('negativeBalanceBarringDate', Date().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 14))),
        namedtype.NamedType('balanceAfterDeduction', MoneyAmount().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 15))),
        namedtype.OptionalNamedType('lastRecord', univ.Boolean().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 16))),
        namedtype.OptionalNamedType('accountGroupID', AccountGroupID().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 17))),
        namedtype.OptionalNamedType('subscriberConvergent', univ.Boolean().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 18))),
        namedtype.OptionalNamedType('subscriberNumber', NumberString().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 19))),
        namedtype.OptionalNamedType('serviceFeeType', ServiceFeeType().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 20))),
        namedtype.OptionalNamedType('debt', MoneyAmount().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 21))),
        namedtype.OptionalNamedType('subscriberFee', MoneyAmount().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 22))),
        namedtype.OptionalNamedType('clearedDedicatedAccounts', univ.SequenceOf(componentType=ClearedDedicatedAccount()).subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 23))),
        namedtype.OptionalNamedType('clearedAccumulators', univ.SequenceOf(componentType=ClearedAccumulator()).subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 24))),
        namedtype.OptionalNamedType('aggregatedBalanceBefore', MoneyAmount().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 25))),
        namedtype.OptionalNamedType('aggregatedBalanceAfter', MoneyAmount().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 26))),
        namedtype.OptionalNamedType('aggregatedBalanceDedicatedAccounts', univ.SequenceOf(componentType=AggregatedBalanceDedicatedAccount()).subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 27))),
        namedtype.OptionalNamedType('removedFaFs', univ.SequenceOf(componentType=RemovedFaF()).subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 28))),
        namedtype.OptionalNamedType('removedOffers', univ.SequenceOf(componentType=RemovedOffer()).subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 29))),
        namedtype.OptionalNamedType('ignoredDebt', MoneyAmount().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 30))),
        namedtype.OptionalNamedType('offerID', OfferID().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 31))),
        namedtype.OptionalNamedType('offerExpiryDateBefore', Date().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 32))),
        namedtype.OptionalNamedType('offerExpiryDateAfter', Date().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 33))),
        namedtype.OptionalNamedType('adjustmentDedicatedAccounts', univ.SequenceOf(componentType=AdjustmentDedicatedAccount()).subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 34))),
        namedtype.OptionalNamedType('totalAmountDeducted', MoneyAmount().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 35))),
        namedtype.OptionalNamedType('maAmountDeducted', MoneyAmount().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 36))),
        namedtype.OptionalNamedType('deductionStatus', SfeeFromDAReturnCode().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 37))),
        namedtype.OptionalNamedType('removedUsageCounters', univ.SequenceOf(componentType=RemovedUsageCounter()).subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 38))),
        namedtype.OptionalNamedType('accumulateDebtOfferID', OfferID().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 39))),
        namedtype.OptionalNamedType('productOfferingName', ProductOfferingName().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 40))))

class LifeCycleChange(univ.Sequence): 
    componentType = namedtype.NamedTypes( 
        namedtype.NamedType('sdpID', NodeID().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))),
        namedtype.NamedType('cdrID', RecordSequenceNumberString().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2))),
        namedtype.NamedType('originNodeType', NodeType().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 3))),
        namedtype.NamedType('timeStamp', TimeStamp().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 4))),
        namedtype.NamedType('accountNumber', NumberString().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 5))),
        namedtype.NamedType('subscriberNumber', NumberString().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 6))),
        namedtype.NamedType('serviceClassId', ServiceClass().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 7))),
        namedtype.OptionalNamedType('language', Language().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 8))),
        namedtype.NamedType('currencyType', CurrencyType().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 9))),
        namedtype.OptionalNamedType('initialAmountAdded', MoneyAmount().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 10))),
        namedtype.OptionalNamedType('initialSupervisionExpDate', Date().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 11))),
        namedtype.OptionalNamedType('initialServiceFeeExpDate', Date().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 12))),
        namedtype.OptionalNamedType('supervisionExpDate', Date().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 13))),
        namedtype.OptionalNamedType('creditClearancePeriod', Period().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 14))),
        namedtype.OptionalNamedType('servFeeExpDate', Date().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 15))),
        namedtype.OptionalNamedType('serviceRemovalPeriod', Period().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 16))),
        namedtype.OptionalNamedType('clearedAccountValue', MoneyAmount().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 17))),
        namedtype.NamedType('accountFlagsBefore', AccountFlags().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 18))),
        namedtype.NamedType('accountFlagsAfter', AccountFlags().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 19))),
        namedtype.OptionalNamedType('activationDate', Date().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 20))),
        namedtype.OptionalNamedType('refillUnbarTimeStamp', TimeStamp().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 21))),
        namedtype.OptionalNamedType('iVRWelcomeStatus', univ.Boolean().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 22))),
        namedtype.OptionalNamedType('negativeBalanceBarringDate', Date().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 23))),
        namedtype.OptionalNamedType('promotionPlanID', PromotionPlan().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 24))),
        namedtype.OptionalNamedType('promotionPlanStartDate', Date().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 25))),
        namedtype.OptionalNamedType('promotionPlanEndDate', Date().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 26))),
        namedtype.OptionalNamedType('accumulatedRefillCounter', univ.Integer().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 27))),
        namedtype.OptionalNamedType('accumulatedRefillValue', MoneyAmount().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 28))),
        namedtype.OptionalNamedType('accumulatedProgressionCounter', univ.Integer().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 29))),
        namedtype.OptionalNamedType('accumulatedProgressionValue', MoneyAmount().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 30))),
        namedtype.OptionalNamedType('preActReasonCode', PreActReasonCode().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 31))),
        namedtype.OptionalNamedType('creditCleared', univ.Boolean().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 32))),
        namedtype.OptionalNamedType('serviceExpired', univ.Boolean().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 33))),
        namedtype.OptionalNamedType('originOperatorId', IDString().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 34))),
        namedtype.NamedType('originNodeId', IDString().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 35))),
        namedtype.OptionalNamedType('origTransactionID', TransactionID().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 36))),
        namedtype.OptionalNamedType('origTransactionTimeStamp', TimeStamp().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 37))),
        namedtype.OptionalNamedType('lastRecord', univ.Boolean().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 38))),
        namedtype.OptionalNamedType('accountGroupID', AccountGroupID().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 39))),
        namedtype.OptionalNamedType('serviceOfferings', ServiceOfferings().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 40))),
        namedtype.OptionalNamedType('communityID1', CommunityID().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 41))),
        namedtype.OptionalNamedType('communityID2', CommunityID().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 42))),
        namedtype.OptionalNamedType('communityID3', CommunityID().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 43))),
        namedtype.OptionalNamedType('subscriberConvergent', univ.Boolean().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 44))),
        namedtype.OptionalNamedType('initialCreditClearanceGracePeriod', Period().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 45))),
        namedtype.OptionalNamedType('initialServiceRemovalGracePeriod', Period().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 46))),
        namedtype.OptionalNamedType('subscriberCreated', univ.Boolean().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 47))),
        namedtype.OptionalNamedType('subscriberDeleted', univ.Boolean().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 48))),
        namedtype.OptionalNamedType('accountHomeRegion', AccountHomeRegion().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 49))),
        namedtype.OptionalNamedType('disconnectionCode', DisconnectionCode().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 50))),
        namedtype.OptionalNamedType('clearedDedicatedAccounts', univ.SequenceOf(componentType=ClearedDedicatedAccount()).subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 51))),
        namedtype.OptionalNamedType('creditClearedReasonMainAccount', Reason().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 52))),
        namedtype.OptionalNamedType('clearedAggregatedValue', MoneyAmount().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 53))),
        namedtype.OptionalNamedType('removedFaFs', univ.SequenceOf(componentType=RemovedFaF()).subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 54))),
        namedtype.OptionalNamedType('removedOffers', univ.SequenceOf(componentType=RemovedOffer()).subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 55))),
        namedtype.OptionalNamedType('periodicAccountMgmtDataLCY', univ.SequenceOf(componentType=PeriodicAccountMgmtDataLCY()).subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 56))),
        namedtype.OptionalNamedType('balanceBefore', MoneyAmount().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 57))),
        namedtype.OptionalNamedType('balanceAfter', MoneyAmount().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 58))),
        namedtype.OptionalNamedType('aggregatedBalanceBefore', MoneyAmount().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 59))),
        namedtype.OptionalNamedType('aggregatedBalanceAfter', MoneyAmount().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 60))),
        namedtype.OptionalNamedType('aggregatedBalanceDedicatedAccounts', univ.SequenceOf(componentType=AggregatedBalanceDedicatedAccount()).subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 61))),
        namedtype.OptionalNamedType('adjustmentDedicatedAccounts', univ.SequenceOf(componentType=AdjustmentDedicatedAccount()).subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 62))),
        namedtype.OptionalNamedType('adjustmentAccumulators', univ.SequenceOf(componentType=AdjustmentAccumulator()).subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 63))),
        namedtype.OptionalNamedType('adjustmentOffers', univ.SequenceOf(componentType=AdjustmentOffer()).subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 64))),
        namedtype.OptionalNamedType('adjustmentUsageCounters', univ.SequenceOf(componentType=UsageCounter()).subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 65))),
        namedtype.OptionalNamedType('adjustmentUsageThresholds', univ.SequenceOf(componentType=UsageThreshold()).subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 66))),
        namedtype.OptionalNamedType('eocnSelectionId', EocnSelectionId().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 67))),
        namedtype.OptionalNamedType('selectionTreeQualifiers', SelectionTreeQualifiers().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 68))),
        namedtype.OptionalNamedType('accountPrepaidEmptyLimit', MoneyAmount().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 69))),
        namedtype.OptionalNamedType('removedPredefinedOfferValues', univ.SequenceOf(componentType=RemovedPredefinedOfferValue()).subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 70))),
        namedtype.OptionalNamedType('removedGlobalParameters', univ.SequenceOf(componentType=RemovedGlobalParameter()).subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 71))))

class ValueVoucherExpiry(univ.Sequence): 
    componentType = namedtype.NamedTypes( 
        namedtype.NamedType('sdpID', NodeID().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))),
        namedtype.NamedType('cdrID', RecordSequenceNumberString().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2))),
        namedtype.NamedType('accountNumber', NumberString().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 3))),
        namedtype.NamedType('timeStamp', TimeStamp().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 4))),
        namedtype.OptionalNamedType('accountFlagsBefore', AccountFlags().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 5))),
        namedtype.OptionalNamedType('accountFlagsAfter', AccountFlags().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 6))),
        namedtype.NamedType('oldServiceClass', ServiceClass().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 7))),
        namedtype.NamedType('newServiceClass', ServiceClass().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 8))),
        namedtype.OptionalNamedType('negativeBalanceBarringDate', Date().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 9))),
        namedtype.NamedType('currencyType', CurrencyType().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 10))),
        namedtype.NamedType('valueVoucherExpDate', Date().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 11))),
        namedtype.OptionalNamedType('lastRecord', univ.Boolean().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 12))),
        namedtype.OptionalNamedType('subscriberConvergent', univ.Boolean().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 13))),
        namedtype.OptionalNamedType('clearedDedicatedAccounts', univ.SequenceOf(componentType=ClearedDedicatedAccount()).subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 14))),
        namedtype.OptionalNamedType('clearedAccumulators', univ.SequenceOf(componentType=ClearedAccumulator()).subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 15))),
        namedtype.OptionalNamedType('aggregatedBalanceBefore', MoneyAmount().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 16))),
        namedtype.OptionalNamedType('aggregatedBalanceAfter', MoneyAmount().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 17))),
        namedtype.OptionalNamedType('removedFaFs', univ.SequenceOf(componentType=RemovedFaF()).subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 18))),
        namedtype.OptionalNamedType('removedOffers', univ.SequenceOf(componentType=RemovedOffer()).subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 19))),
        namedtype.OptionalNamedType('removedUsageCounters', univ.SequenceOf(componentType=RemovedUsageCounter()).subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 20))))

class PeriodicAccountMgmt(univ.Sequence): 
    componentType = namedtype.NamedTypes( 
        namedtype.NamedType('sdpID', NodeID().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))),
        namedtype.NamedType('cdrID', RecordSequenceNumberString().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2))),
        namedtype.NamedType('accountNumber', NumberString().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 3))),
        namedtype.NamedType('subscriberNumber', NumberString().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 4))),
        namedtype.NamedType('timeStamp', TimeStamp().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 5))),
        namedtype.NamedType('serviceClassId', ServiceClass().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 6))),
        namedtype.NamedType('currencyType', CurrencyType().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 7))),
        namedtype.OptionalNamedType('originOperatorId', IDString().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 8))),
        namedtype.OptionalNamedType('originNodeType', NodeType().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 9))),
        namedtype.OptionalNamedType('originNodeID', IDString().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 10))),
        namedtype.OptionalNamedType('origTransactionID', TransactionID().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 11))),
        namedtype.OptionalNamedType('origTransactionTimeStamp', TimeStamp().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 12))),
        namedtype.OptionalNamedType('transactionType', TransactionType().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 13))),
        namedtype.OptionalNamedType('transactionCode', TransactionCode().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 14))),
        namedtype.NamedType('pamEventType', PamEventType().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 15))),
        namedtype.NamedType('periodicAccountMgmtService', univ.SequenceOf(componentType=PeriodicAccountMgmtService()).subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 16))),
        namedtype.OptionalNamedType('unchangedDedicatedAccounts', univ.SequenceOf(componentType=DedicatedAccountInfo()).subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 17))),
        namedtype.OptionalNamedType('unchangedAccumulators', univ.SequenceOf(componentType=AccumulatorInfo()).subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 18))),
        namedtype.OptionalNamedType('negativeBalanceBarringDate', Date().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 19))),
        namedtype.OptionalNamedType('accountFlagsBefore', AccountFlags().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 20))),
        namedtype.OptionalNamedType('accountFlagsAfter', AccountFlags().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 21))),
        namedtype.OptionalNamedType('unchangedUsageCounters', univ.SequenceOf(componentType=UnchangedUsageCounter()).subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 22))),
        namedtype.OptionalNamedType('unchangedOffers', univ.SequenceOf(componentType=OfferInfo()).subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 23))),
        namedtype.OptionalNamedType('accountHomeTimeZone', TimeZone().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 24))),
        namedtype.OptionalNamedType('periodicAccountMgmtBillCycleData', PeriodicAccountMgmtData().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 25))),
        namedtype.OptionalNamedType('accountStateSequenceNumber', Unsigned63().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 26))),
        namedtype.OptionalNamedType('requestData', univ.OctetString().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 27))),
        namedtype.OptionalNamedType('providerNumber', NumberString().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 28))),
        namedtype.OptionalNamedType('periodicAccountMgmtRerateCycleData', PeriodicAccountMgmtData().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 29))),
        namedtype.OptionalNamedType('lastRecord', univ.Boolean().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 30))))

class TimeBasedActions(univ.Sequence): 
    componentType = namedtype.NamedTypes( 
        namedtype.NamedType('sdpID', NodeID().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))),
        namedtype.NamedType('cdrID', RecordSequenceNumberString().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2))),
        namedtype.NamedType('accountNumber', NumberString().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 3))),
        namedtype.NamedType('subscriberNumber', NumberString().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 4))),
        namedtype.NamedType('serviceClassId', ServiceClass().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 5))),
        namedtype.NamedType('currencyType', CurrencyType().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 6))),
        namedtype.NamedType('timeStamp', TimeStamp().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 7))),
        namedtype.NamedType('timeBasedAction', univ.SequenceOf(componentType=TimeBasedAction()).subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 8))))

class SDPCallDataRecord(univ.Choice): 
    componentType = namedtype.NamedTypes( 
        namedtype.NamedType('accountAdjustment', AccountAdjustment().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 2))),
        namedtype.NamedType('negativeBalance', NegativeBalance().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 3))),
        namedtype.NamedType('bonusAdjustment', BonusAdjustment().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 4))),
        namedtype.NamedType('serviceFeeDeduction', ServiceFeeDeduction().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 5))),
        namedtype.NamedType('lifeCycleChange', LifeCycleChange().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 6))),
        namedtype.NamedType('negativeBalanceBarred', NegativeBalanceBarred().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 7))),
        namedtype.NamedType('valueVoucherExpiry', ValueVoucherExpiry().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 8))),
        namedtype.NamedType('periodicAdjustment', PeriodicAdjustment().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 9))),
        namedtype.NamedType('periodicReset', PeriodicReset().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 10))),
        namedtype.NamedType('temporaryBlock', TemporaryBlock().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 11))),
        namedtype.NamedType('periodicAccountMgmt', PeriodicAccountMgmt().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 12))),
        namedtype.NamedType('cdrFileControlBlock', CDRFileControlBlock().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 13))),
        namedtype.NamedType('subscriberTransfer', SubscriberTransfer().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 14))),
        namedtype.NamedType('timeBasedActions', TimeBasedActions().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 15))))


