import pyqrcode
from lndgrpc import LNDClient
import configparser


def main():
    config = configparser.ConfigParser()
    config.read("project.config")

    invoice_mac_loc = config["file_locations"]["invoice_mac_loc"]
    tls_cert_loc = config["file_locations"]["tls_cert_loc"]
    ip_address = config["addresses"]["alice"]

    # pass in the ip-address with RPC port and network ('mainnet', 'testnet', 'simnet')
    # the client defaults to 127.0.0.1:10009 and mainnet if no args provided
    lnd = LNDClient(macaroon_filepath=invoice_mac_loc, cert_filepath=tls_cert_loc, network="simnet",
                    ip_address=ip_address)

    # lnd.get_info() #permission denied with invoice_mac -> needs admin

    # create invoice
    invoice = lnd.add_invoice(100, "testing 42069")
    print(type(invoice))
    r_hash = invoice.r_hash
    payment_request = invoice.payment_request
    add_index = invoice.add_index

    # Generate QR code
    url = pyqrcode.create(payment_request)

    # Create and save the png file naming "myqr.png"
    url.png('myqr.png', scale=6)


if __name__ == '__main__':
    main()
