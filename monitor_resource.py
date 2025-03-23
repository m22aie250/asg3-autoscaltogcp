import psutil
import time

def monitor_resources(threshold=75):
    while True:
        cpu_usage = psutil.cpu_percent(interval=1)
        memory_usage = psutil.virtual_memory().percent
        print(f"CPU Usage: {cpu_usage}%, Memory Usage: {memory_usage}%")

        if cpu_usage > threshold or memory_usage > threshold:
            print("Resource usage exceeds 75%. Triggering auto-scaling to AWS.")
            trigger_auto_scaling()
        time.sleep(5)

def trigger_auto_scaling():
    # Add AWS auto-scaling logic here
    print("Auto-scaling to AWS...")
    # EUse boto3 to launch an EC2 instance
    import boto3
    ec2 = boto3.client('ec2', region_name='us-east-1')
    response = ec2.run_instances(
        ImageId='ami-05c179eced2eb9b5b',  # AMI ID
        InstanceType='t2.micro',
        MinCount=1,
        MaxCount=1,
        KeyName='vcc-asg3',  #key pair
        # security group
        SecurityGroupIds=['sg-0dcb79a1180da4e5c'],
        SubnetId='subnet-09e4fa9cb3561643f'  #  subnet
    )
    print("EC2 instance launched:", response['Instances'][0]['InstanceId'])

if __name__ == "__main__":
    monitor_resources()
