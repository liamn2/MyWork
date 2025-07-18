from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
# Generate some parameters. These can be reused.
parameters = dh.generate_parameters(generator=2, key_size=2048)
# Generate a private key for use in the exchange.
server_private_key = parameters.generate_private_key()
# In a real handshake the peer is a remote client. For this
# example we'll generate another local private key though. Note that in
# a DH handshake both peers must agree on a common set of parameters.
peer_private_key = parameters.generate_private_key()
shared_key = server_private_key.exchange(peer_private_key.public_key())
# Perform key derivation.
derived_key = HKDF(
    algorithm=hashes.SHA256(),
    length=32,
    salt=None,
    info=b'handshake data',
).derive(shared_key)
# And now we can demonstrate that the handshake performed in the
# opposite direction gives the same final value
same_shared_key = peer_private_key.exchange(
    server_private_key.public_key()
)
same_derived_key = HKDF(
    algorithm=hashes.SHA256(),
    length=32,
    salt=None,
    info=b'handshake data',
).derive(same_shared_key)
derived_key == same_derived_key

# Generate some parameters. These can be reused.
parameters = dh.generate_parameters(generator=2, key_size=2048)
# Generate a private key for use in the exchange.
private_key = parameters.generate_private_key()
# In a real handshake the peer_public_key will be received from the
# other party. For this example we'll generate another private key and
# get a public key from that. Note that in a DH handshake both peers
# must agree on a common set of parameters.
peer_public_key = parameters.generate_private_key().public_key()
shared_key = private_key.exchange(peer_public_key)
# Perform key derivation.
derived_key = HKDF(
    algorithm=hashes.SHA256(),
    length=32,
    salt=None,
    info=b'handshake data',
).derive(shared_key)
# For the next handshake we MUST generate another private key, but
# we can reuse the parameters.
private_key_2 = parameters.generate_private_key()
peer_public_key_2 = parameters.generate_private_key().public_key()
shared_key_2 = private_key_2.exchange(peer_public_key_2)
derived_key_2 = HKDF(
    algorithm=hashes.SHA256(),
    length=32,
    salt=None,
    info=b'handshake data',
).derive(shared_key_2)

pn = dh.DHParameterNumbers(p, g)
parameters = pn.parameters()
peer_public_numbers = dh.DHPublicNumbers(y, pn)
peer_public_key = peer_public_numbers.public_key()
