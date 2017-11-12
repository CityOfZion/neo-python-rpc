=====
Usage
=====

To use neo-python-rpc in a project::

    >>> from neo.Network.RPC.Client import RPCClient
    >>> client = RPCClient()
    >>> blockchain_height = client.get_height()
    >>> blockchain_height
    769332

