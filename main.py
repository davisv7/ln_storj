import pyqrcode
from lndgrpc import LNDClient
import configparser
from time import sleep


def create_node_obj(config, name):
    invoice_mac_loc = config[name]["admin_mac_loc"]
    tls_cert_loc = config[name]["tls_cert_loc"]
    ip_address = config[name]["address"]

    # pass in the ip-address with RPC port and network ('mainnet', 'testnet', 'simnet')
    # the client defaults to 127.0.0.1:10009 and mainnet if no args provided
    node_obj = LNDClient(macaroon_filepath=invoice_mac_loc, cert_filepath=tls_cert_loc, network="simnet",
                         ip_address=ip_address)

    return node_obj


def create_qrcode(payment_request):
    # Generate QR code
    url = pyqrcode.create(payment_request)

    # Create and save the png file naming "myqr.png"
    url.png('qrcode.png', scale=6)


def check_invoice_paid():
    pass


def main():
    config = configparser.ConfigParser()
    config.read("project.config")

    alice = create_node_obj(config, "alice")
    bob = create_node_obj(config, "bob")

    # alice create invoice
    invoice = bob.add_invoice(8008, "testing 42069")
    r_hash = invoice.r_hash
    add_index = invoice.add_index
    payment_request = invoice.payment_request
    print(payment_request)

    # save invoice as qrcode
    # create_qrcode(payment_request)

    # alice pay invoice
    alice.send_payment(payment_request)

    # wait a few seconds
    # sleep(10)

    # check if invoice has been paid
    a_paid_invoice = alice.list_payments()
    b_paid_invoice = bob.list_payments()
    print(a_paid_invoice)
    print(b_paid_invoice)


if __name__ == '__main__':
    main()
