from bitcoin_tools.core.keys import generate_keys, store_keys
from bitcoin_tools.wallet import generate_wif, generate_btc_addr

#################################################
# Key management and Bitcoin address generation #
#################################################
# ---------------------------------------------------------------------------------------------------------------------
# The following piece of code generates fresh keys and Bitcoin address.
# - Both mainnet and testnet addresses can be generated. Tesnet are generated by default.
# - Keys are stored in the folder defined in conf.py.
# - WIF can be stored as a qr image or text. Image is set by default.
# ---------------------------------------------------------------------------------------------------------------------

# First of all the ECDSA keys are generated.
sk, pk = generate_keys()
# Then, the Bitcoin address is derived from the public key created above.
btc_addr = generate_btc_addr(pk)
# Both the public and private key are stored in disk in pem format. The Bitcoin address is used as an identifier in the
# name of the folder that contains both keys.
store_keys(sk.to_pem(), pk.to_pem(), btc_addr)
# Finally, the private key is encoded as WIF and also stored in disk, ready to be imported in a wallet.
generate_wif(btc_addr, sk)

print "Keys for address " + btc_addr + " properly generated and stored."


