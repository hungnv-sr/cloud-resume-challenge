
[![codecov](https://codecov.io/gh/hungnv-sr/cloud-resume-challenge/graph/badge.svg?token=ZFFQHAQF8C)](https://codecov.io/gh/hungnv-sr/cloud-resume-challenge)
[![Coverage](https://github.com/hungnv-sr/cloud-resume-challenge/actions/workflows/coverage.yml/badge.svg?branch=main)](https://github.com/hungnv-sr/cloud-resume-challenge/actions/workflows/coverage.yml)
[![Deploy Status](https://github.com/hungnv-sr/cloud-resume-challenge/actions/workflows/deploy.yml/badge.svg?branch=main)](https://github.com/hungnv-sr/cloud-resume-challenge/actions/workflows/deploy.yml)

# AWS Cloud Resume Challenge


This is my take on [AWS Cloud Resume Challenge](https://cloudresumechallenge.dev/docs/the-challenge/aws/)

## Architecture

![architecture](./documents/cloud-resume-challenge.png)

| Service  | Description |
| ------------- | ------------- |
| Route53  | DNS resolver  |
| Cloudfront  | Content Delivery network  |
| S3  | Store [React static site content](https://github.com/hungnv-sr/React-Portfolio)  |
| Api Gateway  | Serve HTTP API  |
| Lambda  |  Count request and save to database. This will only count the requests made from browser  |
| Lambda@Edge  | Count all requests to Cloudfront and save to database (bot requests included)   |
| DynamoDB  | Database  |
