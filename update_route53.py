import json
import boto3


client = boto3.client("route53")

HOSTED_ZONE_NAME = "indigena.xyz"
RECORD_NAME = "bisnaga.indigena.xyz"
RECORD_TYPE = "A"
RECORD_TTL = 300


def get_hosted_zone_id(name):
    name = f"{name}."
    response = client.list_hosted_zones()
    for zone in response["HostedZones"]:
        if zone["Name"] == name:
            return zone["Id"]


def main(event, context):
    try:
        id_ = get_hosted_zone_id(HOSTED_ZONE_NAME)
        print(event)
        ip = event["requestContext"]["http"]["sourceIp"]
        record = {
            "TTL": RECORD_TTL,
            "Type": RECORD_TYPE,
            "Name": RECORD_NAME,
            "ResourceRecords": [{"Value": ip}],
        }

        response = client.change_resource_record_sets(
            HostedZoneId=id_,
            ChangeBatch={
                "Changes": [{"Action": "UPSERT", "ResourceRecordSet": record}],
                "Comment": "Automatic DNS Update",
            },
        )

        body = {"message": "Record updated successfully", "record": record}
    except Exception as e:
        body = {"message": str(e)}
    return {"statusCode": 200, "body": json.dumps(body)}
