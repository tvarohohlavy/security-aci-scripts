#!/usr/bin/env python
'''
Autogenerated code using arya
Original Object Document Input: 
'''

# list of packages that should be imported for this code to work
import cobra.mit.access
import cobra.mit.request
import cobra.mit.session
import cobra.model.fv
import cobra.model.pol
import cobra.model.vns
from cobra.internal.codec.xmlcodec import toXMLStr
import sys
pod_num = int(sys.argv[1])
tenant_name = sys.argv[2]
csr_ip = sys.argv[3]

lab_prefix,owner,ownersid,ownerpod = tenant_name.split("-")
tenant_login = '%s' % tenant_name

# log into an APIC and create a directory object
ls = cobra.mit.session.LoginSession('https://198.19.254.61', '%s' % tenant_login, 'p%s' % tenant_login)

md = cobra.mit.access.MoDirectory(ls)
md.login()

# the top level object on which operations will be made
polUni = cobra.model.pol.Uni('')
fvTenant = cobra.model.fv.Tenant(polUni, '%s' % tenant_name)

# build the request using cobra syntax
vnsAbsGraph = cobra.model.vns.AbsGraph(fvTenant, ownerKey=u'', name=u'asa1-graph', descr=u'', ownerTag=u'', uiTemplateType=u'UNSPECIFIED')
vnsAbsTermNodeCon = cobra.model.vns.AbsTermNodeCon(vnsAbsGraph, ownerKey=u'', name=u'T1', descr=u'', ownerTag=u'')
vnsAbsTermConn = cobra.model.vns.AbsTermConn(vnsAbsTermNodeCon, ownerKey=u'', attNotify=u'no', name=u'1', descr=u'', ownerTag=u'')
vnsInTerm = cobra.model.vns.InTerm(vnsAbsTermNodeCon, name=u'input-terminal', descr=u'')
vnsOutTerm = cobra.model.vns.OutTerm(vnsAbsTermNodeCon, name=u'output-terminal', descr=u'')
vnsAbsTermNodeProv = cobra.model.vns.AbsTermNodeProv(vnsAbsGraph, ownerKey=u'', name=u'T2', descr=u'', ownerTag=u'')
vnsAbsTermConn2 = cobra.model.vns.AbsTermConn(vnsAbsTermNodeProv, ownerKey=u'', attNotify=u'no', name=u'1', descr=u'', ownerTag=u'')
vnsInTerm2 = cobra.model.vns.InTerm(vnsAbsTermNodeProv, name=u'input-terminal', descr=u'')
vnsOutTerm2 = cobra.model.vns.OutTerm(vnsAbsTermNodeProv, name=u'output-terminal', descr=u'')

vnsAbsConnection = cobra.model.vns.AbsConnection(vnsAbsGraph, adjType=u'L3', ownerKey=u'', name=u'C1', descr=u'', connDir=u'provider', connType=u'external', unicastRoute=u'yes', ownerTag=u'')
vnsRsAbsConnectionConns = cobra.model.vns.RsAbsConnectionConns(vnsAbsConnection, tDn=u'uni/tn-%s/AbsGraph-asa1-graph/AbsNode-FIREWALL/AbsFConn-consumer'  % tenant_name)

vnsRsAbsConnectionConns2 = cobra.model.vns.RsAbsConnectionConns(vnsAbsConnection, tDn=u'uni/tn-%s/AbsGraph-asa1-graph/AbsTermNodeCon-T1/AbsTConn'  % tenant_name)

vnsAbsConnection2 = cobra.model.vns.AbsConnection(vnsAbsGraph, adjType=u'L3', ownerKey=u'', name=u'C2', descr=u'', connDir=u'provider', connType=u'external', unicastRoute=u'yes', ownerTag=u'')

vnsRsAbsConnectionConns3 = cobra.model.vns.RsAbsConnectionConns(vnsAbsConnection2, tDn=u'uni/tn-%s/AbsGraph-asa1-graph/AbsTermNodeProv-T2/AbsTConn'  % tenant_name)
vnsRsAbsConnectionConns4 = cobra.model.vns.RsAbsConnectionConns(vnsAbsConnection2, tDn=u'uni/tn-%s/AbsGraph-asa1-graph/AbsNode-FIREWALL/AbsFConn-provider'  % tenant_name)

vnsAbsNode = cobra.model.vns.AbsNode(vnsAbsGraph, ownerKey=u'', funcTemplateType=u'FW_ROUTED', managed=u'yes', name=u'FIREWALL', descr=u'', funcType=u'GoTo', shareEncap=u'no', sequenceNumber=u'0', ownerTag=u'')

vnsAbsFuncConn = cobra.model.vns.AbsFuncConn(vnsAbsNode, ownerKey=u'', attNotify=u'no', name=u'consumer', descr=u'', ownerTag=u'')
vnsRsMConnAtt = cobra.model.vns.RsMConnAtt(vnsAbsFuncConn, tDn=u'uni/infra/mDev-CISCO-ASA-1.2/mFunc-Firewall/mConn-external')

vnsAbsFuncConn2 = cobra.model.vns.AbsFuncConn(vnsAbsNode, ownerKey=u'', attNotify=u'no', name=u'provider', descr=u'', ownerTag=u'')
vnsRsMConnAtt2 = cobra.model.vns.RsMConnAtt(vnsAbsFuncConn2, tDn=u'uni/infra/mDev-CISCO-ASA-1.2/mFunc-Firewall/mConn-internal')


vnsRsNodeToAbsFuncProf = cobra.model.vns.RsNodeToAbsFuncProf(vnsAbsNode, tDn=u'uni/tn-%s/absFuncProfContr/absFuncProfGrp-asa1-gr/absFuncProf-asa1-fprof'  % tenant_name)
vnsRsNodeToMFunc = cobra.model.vns.RsNodeToMFunc(vnsAbsNode, tDn=u'uni/infra/mDev-CISCO-ASA-1.2/mFunc-Firewall')
vnsRsNodeToLDev = cobra.model.vns.RsNodeToLDev(vnsAbsNode, tDn=u'uni/tn-%s/lDevVip-asa1-l3out' % tenant_name)


# commit the generated code to APIC
print toXMLStr(fvTenant)
c = cobra.mit.request.ConfigRequest()
c.addMo(fvTenant)
md.commit(c)

