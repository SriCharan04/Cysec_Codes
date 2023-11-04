import base64
base64_str = "V2UgYXJlIGFub21hbG91cy4gV2UgYXJlIHJlZ2lvbi4gRm9yZ2l2ZSBhbmQgZm9yZ2V0LiBFeHBlY3RvIHBhdHJvbnVtLgo="
bytes = base64_str.encode('ascii')
data_bytes = base64.b64decode(bytes)
decoded_string = data_bytes.decode('ascii')
print(decoded_string)
