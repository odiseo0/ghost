from functools import partial

from aioaws.s3 import S3Client, S3Config
from httpx import AsyncClient

from src.settings import settings


http_client = AsyncClient(verify=False)
AWSClient = partial(
    S3Client,
    http_client=http_client,
    config=S3Config(
        aws_access_key=settings.S3_KEY,
        aws_secret_key=settings.S3_SECRET,
        aws_region=settings.S3_REGION,
        aws_s3_bucket=settings.S3_BUCKET,
        aws_host=f"{settings.S3_BUCKET}.s3.{settings.S3_REGION}.amazonaws.com",
    ),
)
s3_client = AWSClient()
