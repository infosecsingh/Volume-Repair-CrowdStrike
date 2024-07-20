import boto3
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)
ec2 = boto3.client('ec2')

# List of instances and volumes to be processed
instances_volumes = [
    {
        "instance_id": "i-xxxxxxxx",
        "volume_id": "vol-xxxxxxxx",
        "new_instance_id": "i-yyyyyyyy",
        "device": "/dev/sdh"
    },
    # Add more instances and volumes as needed
]

def detach_volume(instance_id, volume_id, device):
    try:
        response = ec2.detach_volume(
            VolumeId=volume_id,
            InstanceId=instance_id,
            Device=device
        )
        logging.info(f"Detached volume {volume_id} from instance {instance_id}: {response}")
    except Exception as e:
        logging.error(f"Error detaching volume {volume_id} from instance {instance_id}: {e}")

def create_snapshot(volume_id):
    try:
        response = ec2.create_snapshot(
            VolumeId=volume_id,
            Description='Snapshot of volume before fix'
        )
        snapshot_id = response['SnapshotId']
        logging.info(f"Created snapshot {snapshot_id} for volume {volume_id}")
        return snapshot_id
    except Exception as e:
        logging.error(f"Error creating snapshot for volume {volume_id}: {e}")
        return None

def attach_volume(volume_id, new_instance_id, device):
    try:
        response = ec2.attach_volume(
            VolumeId=volume_id,
            InstanceId=new_instance_id,
            Device=device
        )
        logging.info(f"Attached volume {volume_id} to new instance {new_instance_id}: {response}")
    except Exception as e:
        logging.error(f"Error attaching volume {volume_id} to new instance {new_instance_id}: {e}")

def detach_and_reattach_volume(volume_id, new_instance_id, instance_id, device):
    try:
        # Detach from new instance
        response = ec2.detach_volume(
            VolumeId=volume_id,
            InstanceId=new_instance_id,
            Device=device
        )
        logging.info(f"Detached volume {volume_id} from new instance {new_instance_id}: {response}")

        # Reattach to impacted instance
        response = ec2.attach_volume(
            VolumeId=volume_id,
            InstanceId=instance_id,
            Device=device
        )
        logging.info(f"Reattached volume {volume_id} to impacted instance {instance_id}: {response}")
    except Exception as e:
        logging.error(f"Error during detach/reattach process for volume {volume_id}: {e}")

def main():
    for item in instances_volumes:
        instance_id = item["instance_id"]
        volume_id = item["volume_id"]
        new_instance_id = item["new_instance_id"]
        device = item["device"]

        detach_volume(instance_id, volume_id, device)
        snapshot_id = create_snapshot(volume_id)
        if snapshot_id:
            attach_volume(volume_id, new_instance_id, device)
            # Here you would perform your repairs on the new instance
            detach_and_reattach_volume(volume_id, new_instance_id, instance_id, device)

if __name__ == "__main__":
    main()