import boto3
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)
ec2 = boto3.client('ec2')

def lambda_handler(event, context):
    try:
        # Detach volume
        response = ec2.detach_volume(
            VolumeId='vol-xxxxxxxx',
            InstanceId='i-xxxxxxxx',
            Device='/dev/sdh'
        )
        logging.info(f"Detached volume: {response}")

        # Create snapshot
        response = ec2.create_snapshot(
            VolumeId='vol-xxxxxxxx',
            Description='Snapshot of volume before fix'
        )
        snapshot_id = response['SnapshotId']
        logging.info(f"Created snapshot: {snapshot_id}")

        # Attach volume to new instance
        response = ec2.attach_volume(
            VolumeId='vol-xxxxxxxx',
            InstanceId='i-yyyyyyyy',
            Device='/dev/sdh'
        )
        logging.info(f"Attached volume to new instance: {response}")

        # Detach from new instance and reattach to impacted instance
        response = ec2.detach_volume(
            VolumeId='vol-xxxxxxxx',
            InstanceId='i-yyyyyyyy',
            Device='/dev/sdh'
        )
        logging.info(f"Detached volume from new instance: {response}")

        response = ec2.attach_volume(
            VolumeId='vol-xxxxxxxx',
            InstanceId='i-xxxxxxxx',
            Device='/dev/sdh'
        )
        logging.info(f"Reattached volume to impacted instance: {response}")

    except Exception as e:
        logging.error(f"Error: {e}")
        raise e