# EC2 Volume Repair Automation

## Overview

This Python script automates the process of detaching disk volumes from impacted EC2 instances, taking snapshots of the volumes, attaching the volumes to new instances for repairs, and then reattaching them to the original instances. It is designed to streamline the recovery process in cloud-based environments, especially for AWS EC2 instances.

## Features

- Detach volumes from EC2 instances.
- Create snapshots of the detached volumes.
- Attach the volumes to new EC2 instances.
- Perform necessary repairs on the new instances.
- Reattach the volumes to the original EC2 instances.

## Prerequisites

- AWS account with EC2 and IAM permissions.
- Python 3.x installed on your local machine.
- `boto3` library installed.

## Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/infosecsingh/Volume-Repair-CrowdStrike.git
   cd Volume-Repair-CrowdStrike
   ```
   
## Install Dependencies

Make sure you have boto3 installed. You can install it using pip:
```bash
pip install boto3
```
## Configure AWS Credentials

Ensure your AWS credentials are configured. You can use the AWS CLI to configure them:
```bash
aws configure
```

Alternatively, you can set environment variables for **AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY**, and **AWS_SESSION_TOKEN**.


## Configuration
#### Edit the script to set your specific parameters. Modify the instances_volumes list with your specific instances and volumes:
```bash
instances_volumes = [
    {
        "instance_id": "i-xxxxxxxx",
        "volume_id": "vol-xxxxxxxx",
        "new_instance_id": "i-yyyyyyyy",
        "device": "/dev/sdh"
    },
    # Add more instances and volumes as needed
]
```

## Usage
Run the script from the command line:
```bash
python volume_repair_automation.py
```
Ensure you have modified the script to include your specific volume IDs and instance IDs before running it.

## Example
Here’s an example of how you might modify the instances_volumes list:
```bash
instances_volumes = [
    {
        "instance_id": "i-1234567890abcdef0",
        "volume_id": "vol-1234567890abcdef0",
        "new_instance_id": "i-0987654321fedcba0",
        "device": "/dev/sdh"
    },
    {
        "instance_id": "i-abcdef1234567890",
        "volume_id": "vol-fedcba0987654321",
        "new_instance_id": "i-1234fedcba567890",
        "device": "/dev/sdh"
    }
]

```

## Error Handling
The script includes basic error handling. Errors will be logged to the console. Make sure to review the logs to address any issues that arise.

## Automation
For automation, consider integrating the script with AWS Lambda, Systems Manager, or CI/CD pipelines as described in the Automation section of this README.


## Contributing
Feel free to submit issues or pull requests if you have improvements or bug fixes. Ensure you follow the contribution guidelines.

## Contact
For any questions or support, please contact infosecsingh@gmail.com






