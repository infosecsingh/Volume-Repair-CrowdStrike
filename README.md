# EC2 Volume Repair Automation

## Overview

This Python script automates the process of detaching a disk volume from an impacted EC2 instance, taking a snapshot of the volume, attaching the volume to a new instance for repairs, and then reattaching it to the original instance. It is designed to streamline the recovery process in cloud-based environments, especially for AWS EC2 instances.

## Features

- Detach a volume from an EC2 instance.
- Create a snapshot of the detached volume.
- Attach the volume to a new EC2 instance.
- Perform necessary repairs on the new instance.
- Reattach the volume to the original EC2 instance.

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
#### Edit the script to set your specific parameters:

- VolumeId – The ID of the volume to be detached.
- InstanceId – The ID of the impacted EC2 instance.
- NewInstanceId – The ID of the new EC2 instance for repairs.
- Device – The device name for the volume attachment (e.g., /dev/sdh).


## Usage
Run the script from the command line:
```bash
python volume_repair_automation.py
```
Ensure you have modified the script to include your specific volume IDs and instance IDs before running it.


## Example
Here’s an example of how you might modify the script:
```bash 
response = ec2.detach_volume(
    VolumeId='vol-1234567890abcdef0',
    InstanceId='i-1234567890abcdef0',
    Device='/dev/sdh'
)
```

## Error Handling
The script includes basic error handling. Errors will be logged to the console. Make sure to review the logs to address any issues that arise.

## Automation
For automation, consider integrating the script with AWS Lambda, Systems Manager, or CI/CD pipelines as described in the Automation section of this README.


## Contributing
Feel free to submit issues or pull requests if you have improvements or bug fixes. Ensure you follow the contribution guidelines.

## Contact
For any questions or support, please contact infosecsingh@gmail.com






