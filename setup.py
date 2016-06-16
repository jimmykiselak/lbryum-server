from setuptools import setup

setup(
    name="lbryum-server",
    version="1.0",
    scripts=['run_lbryum_server.py', 'lbryum-server'],
    install_requires=['sha3', 'plyvel', 'jsonrpclib', 'irc >= 11, <=14.0'],
    package_dir={
        'lbryumserver':'src'
        },
    py_modules=[
        'lbryumserver.__init__',
        'lbryumserver.utils',
        'lbryumserver.storage',
        'lbryumserver.deserialize',
        'lbryumserver.networks',
        'lbryumserver.blockchain_processor',
        'lbryumserver.server_processor',
        'lbryumserver.processor',
        'lbryumserver.version',
        'lbryumserver.ircthread',
        'lbryumserver.stratum_tcp'
    ],
    description="Lbryum Server",
    author="Thomas Voegtlin",
    author_email="thomasv@electrum.org",
    license="MIT Licence",
    url="https://github.com/lbryio/lbryum-server/",
    dependency_links=['https://github.com/bjornedstrom/python-sha3/tarball/master/#egg=python-sha3'],
    long_description="""Server for the Electrum Lightweight LBRY Wallet"""
)
