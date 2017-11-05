from ws4py.client.threadedclient import WebSocketClient
import initio
import json


class LamPiCarClient(WebSocketClient):
    
    def opened(self):
        ws.send('{"message":"device", "device":"car"}')
        
    def closed(self, code, reason=None):
        print "Closed down", code, reason
        
    def received_message(self, m):
        print m
        json_String = str(m)
        json_Parsed = json.loads(json_String)
        if json_Parsed.action == 'fwd':
            initio.forward(50)
        if json_Parsed.action == 'bwd':
            initio.reverse(50)
        if json_Parsed.action == 'right':
            initio.spinLeft(50)
        if json_Parsed.action == 'left':
            initio.spinRight(50)
        if json_Parsed.action == 'stop':
            initio.stop()
        
        
if __name__ == '__main__':
    try:
        ws = LamPiCarClient('ws://lampi-server')
        ws.connect()
        ws.run_forever()
    except KeyboardInterrupt:
        ws.close()
