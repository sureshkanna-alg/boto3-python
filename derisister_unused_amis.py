import boto3
client = boto3.client('ec2')
response = client.describe_instances()
used_amis=[]
all_amis=[]
for instance in response['Reservations']:
    for x in  instance['Instances']:
        used_amis.append(x['ImageId'])
print(used_amis)

response1 = client.describe_images(
    Filters=[
        {
            'Name': 'state',
            'Values': [
                'available',
            ]
        },
    ],    
    Owners=[
        'self'
        ]
)

for amis in response1['Images']:
    all_amis.append(amis['ImageId'])
print(all_amis)

unused=list(set(all_amis)-set(used_amis))
print(unused)
for ami in unused:
    client.deregister_image(ImageId=ami)
