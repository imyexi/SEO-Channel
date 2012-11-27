# coding=utf-8
import suds
import traceback as tb
import sys
default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)
 
try:
    url = 'https://sfapitest.baidu.com/sem/sms/v2/AccountService?wsdl'
    client = suds.client.Client(url)
    print client    #The soap client stub
 
    header = client.factory.create('ns0:AuthHeader')
    header.username = '途牛大连'
    header.password = 'oyXM7MtO1JsBEGQg'
    header.token = 'f9f46d13feba682a3e72be3ddf45a36c'
    client.set_options(soapheaders=header)
    print header    #The soap AuthHeader
 
    result =  client.service.getAccountInfo(1)
    resheader = client.last_received().getChild("Envelope").getChild("Header").getChild("ResHeader")
 
    print "Execution status: \t", resheader.getChild("desc").getText();
    print "   consume quota: \t", resheader.getChild("quota").getText();
    print "    remain quota: \t", resheader.getChild("rquota").getText();
    print "Execution result: \t", result;
except Exception, e:
    print e
    tb.print_exc()
