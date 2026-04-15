from botocore.exceptions import ClientError

from app.services.evidence_storage import EvidenceStorage


def run() -> None:
    storage = EvidenceStorage()
    key = "smoke/runtime-check.txt"
    payload = b"privacy-response-platform-smoke-test"

    try:
        storage.client.head_bucket(Bucket=storage.bucket)
    except ClientError:
        storage.client.create_bucket(Bucket=storage.bucket)

    storage.put_bytes(key=key, data=payload, content_type="text/plain")
    obj = storage.client.get_object(Bucket=storage.bucket, Key=key)
    body = obj["Body"].read()
    if body != payload:
        raise RuntimeError("S3 smoke test failed: uploaded payload mismatch")

    print(f"S3 smoke test passed: s3://{storage.bucket}/{key}")


if __name__ == "__main__":
    run()

