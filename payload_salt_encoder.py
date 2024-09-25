import base64
import hashlib
import os


def encode_payload(payload: str, salt_key: str, salt_index: int) -> str:

    salt = hashlib.sha256(f"{salt_key}{salt_index}".encode()).digest()
    salted_payload = f"{payload}{salt.hex()}"

    # Encode the salted payload to base64
    encoded_payload = base64.b64encode(salted_payload.encode()).decode()
    return encoded_payload


def decode_payload(encoded_payload: str, salt_key: str, salt_index: int) -> str:

    salted_payload = base64.b64decode(encoded_payload).decode()
    salt = hashlib.sha256(f"{salt_key}{salt_index}".encode()).digest()
    salt_hex = salt.hex()

    # Ensure the salted payload ends with the correct salt
    if not salted_payload.endswith(salt_hex):
        raise ValueError("Incorrect salt key or salt index. Decoding failed.")

    original_payload = salted_payload[: -len(salt_hex)]
    return original_payload


if __name__ == "__main__":

    payload = "True Moments!"
    salt_key = "my__dowell_secret_salt_key"
    salt_index = 1

    encoded = encode_payload(payload, salt_key, salt_index)
    print("Encoded Payload:", encoded)

    try:
        decoded = decode_payload(encoded, salt_key, salt_index)
        print("Decoded Payload:", decoded)
    except ValueError as e:
        print(e)

    # Attempt decoding with an incorrect salt key
    try:
        decoded = decode_payload(encoded, "wrong_salt_key", salt_index)
        print("Decoded Payload with incorrect key:", decoded)
    except ValueError as e:
        print(e)
