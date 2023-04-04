"""Custom topology example

Two directly connected switches plus a host for each switch:

   host --- switch --- switch --- host

Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=mytopo' from the command line.
"""

from mininet.topo import Topo

from mininet.net import Mininet
from mininet.node import CPULimitedHost
from mininet.link import TCLink
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel

class MyTopo( Topo ):
    "Simple topology example."

    def build( self ):
        "Create custom topo."

        # Add hosts and switches
        Host1 = self.addHost( 'h1' )
        Host2 = self.addHost( 'h2' )
        Host3 = self.addHost( 'h3' )
        Host4 = self.addHost( 'h4' )
        Switch1 = self.addSwitch( 's1' )
        Switch2 = self.addSwitch( 's2' )
        Switch3 = self.addSwitch( 's3' )
        Switch4 = self.addSwitch( 's4' )

        # Add links
        self.addLink( Host1, Switch1 )
        self.addLink( Host2, Switch1 )
        self.addLink( Switch1, Switch2 )
        #arbol 1 terminado
        self.addLink( Host3, Switch3 )
        self.addLink( Host4, Switch4 )
        self.addLink( Switch4, Switch3, bw =10 , delay = '30ms', loss = 10, cls=TCLink )
        #arbol 2 termiado
        self.addLink( Switch3, Switch2, bw =10 , delay = '15ms', cls=TCLink)
        #conexion entre arboles terminado


topos = { 'mytopo': ( lambda: MyTopo() ) }