from mitmproxy.options import Options
from mitmproxy.proxy.config import ProxyConfig
from mitmproxy.proxy.server import ProxyServer
from mitmproxy.tools.dump import DumpMaster
from mitmproxy.tools.web.master import WebMaster
from mitmproxy.tools.console.master import ConsoleMaster
from mitmproxy import master
from addons import ArkEssential,ArkInterceptor
from addons.allChars import allChars
from addons.moreChars import moreChars
from addons.gachaSimulation import gachaSimulation
from addons.userStatus import userInfo,userData
from addons.graduateChars import graduateChars


from addons.unlockSkins import unlockSkins
from addons.CharsEssential import CharsEssential
from addons.BattleEssential import BattleEssential
from model.troopBuilder import troopBuilder,characterBuilder
import json

def run_web(options):
    webserver = WebMaster(options)
    webserver.server = ProxyServer(ProxyConfig(options))
    return webserver  # type: master.Master


def run_dump(options):
    server = DumpMaster(options, with_termlog=False, with_dumper=False)
    server.server = ProxyServer(ProxyConfig(options))
    return server  # type: master.Master

def run_console(options):
    server = ConsoleMaster(options)
    server.server = ProxyServer(ProxyConfig(options))
    return server  # type: master.Master
from mitmproxy.http import HTTPFlow

if __name__ == "__main__":
    ops = Options(listen_host='0.0.0.0', listen_port=8080, http2=True, ssl_insecure=True)
    master = run_web(ops)
    #ArkInterceptor.tBuilder = troopBuilder.init()
    master.addons.add(ArkEssential())
    master.addons.add(CharsEssential())
    master.addons.add(BattleEssential())
    master.addons.add(allChars())
    master.addons.add(graduateChars())
    master.addons.add(unlockSkins())
    # mc = moreChars()
    # mc.addChars(["char_400_weedy"]*12)
    # master.addons.add(mc)
    #master.addons.add(testa())
    # master.addons.add(fakeGacha())
    # master.addons.add(userInfo.init("Rua牛","0000",120,0))
    # master.addons.add(userData.init(999,999,1919810,114514,6666666))
    # gs = gachaSimulation()
    # gs.setUp("char_264_f12yin","char_108_silent","char_214_kafka","char_440_pinecn")
    # master.addons.add(gs)
    master.run()
