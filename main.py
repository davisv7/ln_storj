from lndgrpc import LNDClient

invoice_mac_loc = "/mnt/c/Users/v1ntage/.polar/networks/1/volumes/lnd/alice/data/chain/bitcoin/regtest/invoice.macaroon"
tls_cert_loc = "/mnt/c/Users/v1ntage/.polar/networks/1/volumes/lnd/alice/tls.cert"
# pass in the ip-address with RPC port and network ('mainnet', 'testnet', 'simnet')
# the client defaults to 127.0.0.1:10009 and mainnet if no args provided
lnd = LNDClient(macaroon_filepath=invoice_mac_loc, cert_filepath=tls_cert_loc)

lnd.get_info()

# create invoice
lnd.add_invoice(100, "testing 42069")
print('Listening for invoices...')
for invoice in lnd.subscribe_invoices():
    print(invoice)
