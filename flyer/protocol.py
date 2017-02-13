#! /usr/bin/env python
#-----------------------------------------------------------------------
# COPYRIGHT_BEGIN
# Copyright (C) 2017, FixFlyer, LLC.
# All rights reserved.
# COPYRIGHT_END
#-----------------------------------------------------------------------


# Carriage return + linefeed, used in properties serialisation.
FLYER_CRLF = "\r\n"

# SOH, used as field separator in FIX-style serialisation.
FLYER_SOH = "\x01"

# End-of-message marker for Flyer protocol messages.
FLYER_EOF = "EOF"



PayloadEventId = 0;
ResendEventId = 104;
SessionLogonEventId = 105;
SessionLogoutEventId = 106;
RestoreEventId = 111;
LogonResponseEventId = 200;
HeartbeatEventId = 201;
HeartbeatAckEventId = 202;
LogonRequestEventId = 203;
LogoutRequestEventId = 204;
ErrorEventId = 301;


HeartbeatMessageType = 0;
PayloadMessageType = 1;
CommonMessageType = 2;
HeartbeatAckMessageType = 3;
CommitMessageType = 4;


FlyerMessageTypeTag = 50001;
FlyerRequestIdTag = 50002;
FlyerFixMessageTypeTag = 50003;
FlyerMessageSequenceNumberTag = 50004;
FlyerSenderCompIdTag = 50005;
FlyerTargetCompIdTag = 50006;
FlyerMessageTag = 50007;
FlyerPossDupTag = 50008;
FlyerPossResendTag = 50009;
FlyerLastAppSeqNoTag = 50010;
FlyerEventTypeTag = 50011;
FlyerBeginStringTag = 50012;
FlyerSerialEventDataTag = 50013;
FlyerRootFieldTag = 50014;
FlyerEofTag = 50015;
FlyerClientMessageIdTag = 50016;
FlyerLastOutgoingMsgSeqNumTag = 50017;
FlyerApplVerIdTag = 50018;
FlyerCustomerApplVerIdTag = 50019;
FlyerSessionQualifierTag = 50020;
