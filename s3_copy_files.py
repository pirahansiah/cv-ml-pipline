"""Copy selected files from AWS S3 using boto3 with sampling conditions."""

from __future__ import annotations

import os
from pathlib import Path
from typing import Any, Iterator

import boto3
from botocore.exceptions import ClientError


def get_all_s3_objects(s3: Any, **kwargs: Any) -> Iterator[dict[str, Any]]:
    """Yield all objects from an S3 prefix, handling pagination."""
    kwargs["MaxKeys"] = 1000
    continuation_token = None

    while True:
        if continuation_token:
            kwargs["ContinuationToken"] = continuation_token
        response = s3.list_objects_v2(**kwargs)
        yield from response.get("Contents", [])
        if not response.get("IsTruncated"):
            break
        continuation_token = response.get("NextContinuationToken")


def main() -> None:
    bucket = os.environ.get("S3_BUCKET", "sagemaker-us-east-1")
    prefix = os.environ.get("S3_PREFIX", "images/")
    output_dir = Path(os.environ.get("S3_OUTPUT_DIR", Path.home() / "s3_downloads"))
    output_dir.mkdir(parents=True, exist_ok=True)

    skip_interval = 40
    max_files = 110

    s3 = boto3.client("s3")
    count = 0
    skip_counter = 0

    for obj in get_all_s3_objects(s3, Bucket=bucket, Prefix=prefix):
        skip_counter += 1
        if skip_counter <= skip_interval:
            continue
        skip_counter = 0

        key: str = obj["Key"]
        if not key.endswith(".png"):
            out_path = output_dir / f"{count:04d}.png"
            print(f"> downloading {bucket}/{key} -> {out_path}")
            s3.download_file(bucket, key, str(out_path))
            count += 1
            if count >= max_files:
                break


if __name__ == "__main__":
    main()
