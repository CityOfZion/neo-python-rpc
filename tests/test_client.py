from unittest import TestCase
from neorpc.Settings import SettingsHolder
from neorpc.Client import RPCClient,RPCEndpoint
import binascii


class RPCClientTestCase(TestCase):

    sample_addr = 'AXjaFSP23Jkbe6Pk9pPGT6NBDs1HVdqaXK'

    sample_asset = 'c56f33fc6ecfcd0c225c4ab356fee59390af8560be0e930faebe74a6daff7c9b'

    def test_client(self):

        client = RPCClient()

        self.assertIsNotNone(client.endpoints)

        self.assertGreater(len(client.endpoints), 0)

        self.assertIsInstance(client.default_endpoint, RPCEndpoint)

        self.assertEqual(client.default_endpoint.height, None)

    def test_settings(self):
        settings = SettingsHolder()
        settings.setup_mainnet()

        client = RPCClient(config=settings)

        self.assertIsNotNone(client.endpoints)

    def test_client_setup(self):

        client = RPCClient(setup=True)

        self.assertIsNotNone(client.endpoints)

        self.assertGreater(len(client.endpoints), 0)

        self.assertIsInstance(client.default_endpoint, RPCEndpoint)

        self.assertIsNotNone(client.default_endpoint.height)

        self.assertEqual(client.default_endpoint.status, 200)

    def test_height(self):
        client = RPCClient()

        response = client.get_height()

        height = int(response)

        self.assertGreaterEqual(height, 0)

    def test_account_state(self):

        client = RPCClient()

        account = client.get_account(self.sample_addr)

        script_hash = bytearray(binascii.unhexlify(account['script_hash'][2:]))
        script_hash.reverse()

        self.assertEqual(len(script_hash), 20)

        balances = account['balances']

        self.assertIsNotNone(balances)
        self.assertGreater(len(balances), 0)

    def test_asset_state(self):

        client = RPCClient()

        asset = client.get_asset(self.sample_asset)

        self.assertEqual(asset['type'], 'GoverningToken')

        self.assertEqual(int(asset['available']), 100000000)

        self.assertEqual(int(asset['precision']), 0)

    def test_best_blockhash(self):

        client = RPCClient()

        hash = bytearray(binascii.unhexlify(client.get_best_blockhash()[2:]))
        hash.reverse()

        self.assertEqual(len(hash), 32)

    def test_get_block_json(self):

        client = RPCClient()

        height = 12344
        blockjson1 = client.get_block(height)

        blockhash = blockjson1['hash'][2:]

        self.assertEqual(blockhash, '1e67372c158a4cfbb17b9ad3aaae77001a4247a00318e354c62e53b56af4006f')

        blockjson2 = client.get_block(blockhash)

        self.assertEqual(blockjson1, blockjson2)

        self.assertEqual(height, blockjson1['index'])

    def test_getblockhash(self):

        client = RPCClient()

        height = 12344

        hash = client.get_block_hash(height)

        self.assertEqual(hash[2:], '1e67372c158a4cfbb17b9ad3aaae77001a4247a00318e354c62e53b56af4006f')

    def test_sysfee(self):

        client = RPCClient()

        height = 740324

        fee = int(client.get_block_sysfee(height))

        self.assertEqual(fee, 469014)

    def test_contract_state(self):

        client = RPCClient()

        contract_hash = 'f8d448b227991cf07cb96a6f9c0322437f1599b9'

        contract = client.get_contract_state(contract_hash)

        hash = contract['hash'][2:]

        self.assertEqual(hash, contract_hash)

    def test_connection_count(self):

        client = RPCClient()

        connection_count = int(client.get_connection_count())

        self.assertGreater(connection_count, 0)

    def test_mempool(self):

        client = RPCClient()

        mempool = client.get_raw_mempool()

        self.assertIsInstance(mempool, list)

    def test_tx_json(self):

        client = RPCClient()

        hash = '58c634f81fbd4ae2733d7e3930a9849021840fc19dc6af064d6f2812a333f91d'
        tx = client.get_transaction(hash)

        self.assertEqual(tx['blocktime'], 1510283768)

        self.assertEqual(tx['txid'][2:], hash)

    def test_get_storage(self):

        client = RPCClient()

        contract_hash = 'd7678dd97c000be3f33e9362e673101bac4ca654'
        key = 'totalSupply'

        storage = client.get_storage(contract_hash, key)

        self.assertIsInstance(storage, bytearray)

        intval = int.from_bytes(storage, 'little')

        self.assertEqual(intval, 196800000000000)

    def test_tx_out(self):

        client = RPCClient()

        tx_hash = '58c634f81fbd4ae2733d7e3930a9849021840fc19dc6af064d6f2812a333f91d'
        index = 0
        txout = client.get_tx_out(tx_hash, index)

        self.assertEqual(txout['asset'][2:], '602c79718b16e442de58778e148d0b1084e3b2dffd5de6b7b16cee7969282de7')
        self.assertEqual(txout['n'], index)
        self.assertEqual(txout['address'], self.sample_addr)

    def test_invoke(self):

        client = RPCClient()

        contract_hash = 'd7678dd97c000be3f33e9362e673101bac4ca654'
        params = [{'type': 7, 'value': 'symbol'}, {'type': 16, 'value': []}]

        result = client.invoke_contract(contract_hash, params)

        self.assertEqual(result['state'], 'HALT, BREAK')
        invoke_result = result['stack']
        self.assertEqual(len(invoke_result), 1)

        stack_item = invoke_result[0]

        self.assertEqual(stack_item['type'], 'ByteArray')
        self.assertEqual(binascii.hexlify('LWTF'.encode('utf-8')).decode('utf-8'), stack_item['value'])

    def test_invoke_fn(self):

        client = RPCClient()

        contract_hash = 'd7678dd97c000be3f33e9362e673101bac4ca654'

        result = client.invoke_contract_fn(contract_hash, 'name')

        self.assertEqual(result['state'], 'HALT, BREAK')
        invoke_result = result['stack']
        self.assertEqual(len(invoke_result), 1)

        invoke_result = result['stack']
        self.assertEqual(len(invoke_result), 1)

        stack_item = invoke_result[0]

        self.assertEqual(stack_item['type'], 'ByteArray')

        val = binascii.unhexlify(stack_item['value'].encode('utf-8')).decode('utf-8')

        self.assertEqual(val, 'LOCALTOKEN')

    def test_invoke_script(self):

        client = RPCClient()

        script = '00c10b746f74616c537570706c796754a64cac1b1073e662933ef3e30b007cd98d67d7'

        result = client.invoke_script(script)

        self.assertEqual(result['state'], 'HALT, BREAK')
        invoke_result = result['stack']
        self.assertEqual(len(invoke_result), 1)

        invoke_result = result['stack']
        self.assertEqual(len(invoke_result), 1)

        stack_item = invoke_result[0]

        self.assertEqual(stack_item['type'], 'ByteArray')

        val = int.from_bytes(binascii.unhexlify(stack_item['value'].encode('utf-8')), 'little')

        self.assertEqual(val, 196800000000000)

    def test_send_raw_tx(self):

        client = RPCClient()

        raw_tx = '80000120d8edd2df8d6907caacd4af8872a596cb75c5829d015ce72895ce376d12def9a780ba502ae28ad7a4b7fbcf6baa4856edb537417d2a0000029b7cffdaa674beae0f930ebe6085af9093e5fe56b34a5c220ccdcf6efc336fc500a3e11100000000d8edd2df8d6907caacd4af8872a596cb75c5829d9b7cffdaa674beae0f930ebe6085af9093e5fe56b34a5c220ccdcf6efc336fc500bbeea000000000d8edd2df8d6907caacd4af8872a596cb75c5829d01414044dfd2b360e548607ece3d453173079233040c2484a99671a7346a8ca16969245b946bfa4c13125f4c931b0cbab216e0d241d908f37ad96abb776890832a3a4b2321025de86902ed42aca7246207a70869b22253aeb7cc84a4cb5eee3773fd78b3f339ac'

        # this will result in a false, since this tx has already been made
        # but, if it were badly formmated, it would be an error
        # so we are testing if we get back a false
        result = client.send_raw_tx(raw_tx)

        self.assertEqual(result, False)

    def test_validate_addr(self):

        client = RPCClient()

        result = client.validate_addr(self.sample_addr)

        self.assertEqual(result['isvalid'], True)
        self.assertEqual(result['address'], self.sample_addr)

        bad_addr = 'BXjaFSP23Jkbe6Pk9pPGT6NBDs1HVdqaXK'

        result = client.validate_addr(bad_addr)

        self.assertEqual(result['isvalid'], False)

    def test_get_peers(self):

        client = RPCClient()

        result = client.get_peers()

        self.assertIsNotNone(result)
#        self.assertIn('connected', result)
#        self.assertIn('unconnected', result)


# Not all endpoints currently implement this method
#
#    def test_get_version(self):
#
#        client = RPCClient()
#
#        version = client.get_version()
#
#        print("versin: %s " % version)
