#!/usr/bin/env python3
"""Fetch the reviewed standalone HAP and verify the pinned digest."""
from pathlib import Path
from urllib.request import urlopen
import hashlib
from prepare import HAP_SHA, HAP_VERSION

URL = f'https://github.com/thx853068675-dev/quietstart/releases/download/v{HAP_VERSION}/quietstart-{HAP_VERSION}.hap'
with urlopen(URL, timeout=120) as response:
    data = response.read(64 * 1024 * 1024 + 1)
if len(data) > 64 * 1024 * 1024 or hashlib.sha256(data).hexdigest() != HAP_SHA:
    raise ValueError('QuietStart HAP digest mismatch')
Path('quietstart.hap').write_bytes(data)
print(f'Downloaded QuietStart {HAP_VERSION}; SHA-256 verified')
