#!/bin/bash

# Local debug runner for SecureApp

API="http://localhost:5000"
TOKEN="abc-123"

echo "[*] Uploading test file..."

curl -X POST "$API/upload" \
  -H "X-Session-Token: $TOKEN" \
  -F "file=@./test_payload.txt" \
  --insecure

echo "[*] Fetching profile info..."

curl -X GET "$API/profile" \
  -H "X-Session-Token: $TOKEN" \
  --insecure
