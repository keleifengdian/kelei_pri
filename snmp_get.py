from pysnmp.hlapi import *

errorIndication, errorStatus, errorIndex, varBinds = next(
    getCmd(SnmpEngine(),
           CommunityData('private'),
           UdpTransportTarget(('187.79.197.198', 161)),
           ContextData(),
           ObjectType(ObjectIdentity('1.3.6.1.2.1.1.1.0')),
           ObjectType(ObjectIdentity('1.3.6.1.2.1.1.6.0')))
)

if errorIndication:
    print(errorIndication)
elif errorStatus:
    print('%s at %s' % (errorStatus.prettyPrint(),
                        errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
else:
    for varBind in varBinds:
        print(' = '.join([x.prettyPrint() for x in varBind]))