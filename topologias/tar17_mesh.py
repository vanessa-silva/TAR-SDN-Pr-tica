#!/usr/bin/python

"""
TAR 2017

Remi / Vanessa

Based on Mininet's examples/emptynet.py
"""

from mininet.net import Mininet
from mininet.node import Controller, RemoteController
from mininet.cli import CLI
from mininet.log import setLogLevel, info

def emptyNet():

    "Mesh topology with 2 hosts per switch & a remote Floodlight Controller"

    net = Mininet( controller=RemoteController )

    info( '*** Adding remote controller\n' )
    net.addController( 'c0', controller=RemoteController, ip="127.0.0.1", port=6653 )

    info( '*** Adding hosts\n' )
    h1 = net.addHost( 'h1', ip='10.0.0.1' )
    h2 = net.addHost( 'h2', ip='10.0.0.2' )
    h3 = net.addHost( 'h3', ip='10.0.0.3' )
    h4 = net.addHost( 'h4', ip='10.0.0.4' )
    h5 = net.addHost( 'h5', ip='10.0.0.5' )
    h6 = net.addHost( 'h6', ip='10.0.0.6' )
    h7 = net.addHost( 'h7', ip='10.0.0.7' )
    h8 = net.addHost( 'h8', ip='10.0.0.8' )

    info( '*** Adding switches\n' )
    s1 = net.addSwitch( 's1' )
    s2 = net.addSwitch( 's2' )
    s3 = net.addSwitch( 's3' )
    s4 = net.addSwitch( 's4' )

    info( '*** Creating links to hosts\n' )
    net.addLink( h1, s1 )
    net.addLink( h2, s1 )

    net.addLink( h3, s2 )
    net.addLink( h4, s2 )

    net.addLink( h5, s3 )
    net.addLink( h6, s3 )

    net.addLink( h7, s4 )
    net.addLink( h8, s4 )

    info( '*** Creating links between switches\n' )
    net.addLink( s1, s2 )
    net.addLink( s1, s3 )
    net.addLink( s1, s4 )
    net.addLink( s2, s3 )
    net.addLink( s2, s4 )
    net.addLink( s3, s4 )

    info( '*** Starting network\n')
    net.start()

    info( '*** Running CLI\n' )
    CLI( net )

    info( '*** Stopping network' )
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    emptyNet()
