=====
Usage
=====

To use neo-python-rpc in a project::

    >>> from neo.Network.RPC.Client import RPCClient
    >>> client = RPCClient()
    >>> blockchain_height = client.get_height()
    >>> blockchain_height
    769332


Get a block

    >>> block = client.get_block(123456)
    >>> block
    {
        "nextconsensus": "AdyQbbn6ENjqWDa5JNYMwN3ikNcA4JeZdk",
        "size": 686,
        "previousblockhash": "0xdbee7804eb1f648e640401a864ed29bbc787d7f9d36b6f4be0a3ffd693723d5e",
        "script": {
            "invocation": "4012bbee0bac21b6ec5c4b0cda3aa28f3aa51e3b4a6c230908370adc8758fc3b051a865539bdca0cc6b450ff4fa18d3295f5c5a05a862b8aa9baff3e69011cb0f640ca5e3e5b3399a2014aa96575
    e2b0c3d1239d41ac05a92ec430ab0e0388f5e76e30062dd9aecca3007993e8bde7a00b70cdbef2fbb641164b9fba5f6ed724dc2e40458bcdf880cfef8d94aef714274ff4c258a13f541d2f8f678520bb5414704662cc5b9e714
    f2e42c94c2a61f8e0b3fb2ec8cc6e9ef2e0670056082370e9331e0f40f0a005fbb338e69465c6e0760ac04c2d61bdbec9922f10b8936d277609dd0f6cab1d7ee944902e0af2ba4ac6183a30158c1aa96c77262070161d24e1c5
    530842403cc25ba0ce9ca460d3bf6108a48c676f131076c1542173278cace43a69b7038d4f2f5b401e8bdea2e10c9c68598d9f530b6618b3165a7c791442cd6d093b6aa2",
            "verification": "55210209e7fd41dfb5c2f8dc72eb30358ac100ea8c72da18847befe06eade68cebfcb9210327da12b5c40200e9f65569476bbff2218da4f32548ff43b6387ec1416a231ee821034ff5ceeac41a
    cf22cd5ed2da17a6df4dd8358fcb2bfb1a43208ad0feaab2746b21026ce35b29147ad09e4afe4ec4a7319095f08198fa8babbe3c56e970b143528d2221038dddc06ce687677a53d54f096d2591ba2302068cf123c1f2d75c2dd
    dc542557921039dafd8571a641058ccc832c5e2111ea39b09c0bde36050914384f7a48bce9bf92102d02b1873a0863cd042cc717da31cea0d7cf9db32b74d4c72c01b0011503e2e2257ae"
        },
        "tx": [
            {
                "vin": [],
                "size": 10,
                "type": "MinerTransaction",
                "txid": "0x0981c5e57997af0ce18d032bc9969220308dce8ec643844398649b6732ad91fe",
                "attributes": [],
                "net_fee": "0",
                "vout": [],
                "nonce": 1808064137,
                "version": 0,
                "scripts": [],
                "sys_fee": "0"
            }
        ],
        "nextblockhash": "0xed2cf18a0b15bb3b6a244abd2de1227afde61d1b0a9cbc582e587c18b3c3a00e",
        "confirmations": 647426,
        "merkleroot": "0x0981c5e57997af0ce18d032bc9969220308dce8ec643844398649b6732ad91fe",
        "hash": "0x10d1473c9fa133b28ea4f470e58b97bfe1222e102b14fbc50d3ade59eb8e3b74",
        "version": 0,
        "time": 1496944720,
        "nonce": "c8f9672b6bc4de89",
        "index": 123456
    }