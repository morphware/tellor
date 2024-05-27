#!/usr/bin/env python3

import json

import boto3
from pprint import pprint


class AWSGPUInstanceAPIWrapper:
    def __init__(self, region_name='us-east-1'):
        self.ec2_client = boto3.client('ec2', region_name=region_name)
        self.pricing_client = boto3.client('pricing', region_name='us-east-1')
    
    def list_gpu_instances(self):
        # Fetch all instance types
        paginator = self.ec2_client.get_paginator('describe_instance_types')
        page_iterator = paginator.paginate()
        
        gpu_instances = []
        for page in page_iterator:
            for instance in page['InstanceTypes']:

                # XXX TEST SNIPPET
                #print('\n\n\n\n\nGPU INFO:',gpu_info)
                print('\n\n\n\n\nGPU INFO','-'*40)
                pprint(instance)
                # END OF TEST SNIPPET



                gpu_info = instance.get('GpuInfo')

                # XXX TEST SNIPPET
                #print('\n\n\n\n\nGPU INFO:',gpu_info)
                #pprint(gpu_info)
                # END OF TEST SNIPPET

                if gpu_info and 'Gpus' in gpu_info:
                    total_vram = sum(gpu.get('GpuSizeInMiB', 0) for gpu in gpu_info['Gpus'])
                    if total_vram > 0:
                        gpu_instances.append({
                            'instance_type': instance['InstanceType'],
                            'total_vram': total_vram,
                            'gpu_count': len(gpu_info['Gpus'])
                        })
                    else:
                        print(f"Debug: Instance {instance['InstanceType']} has zero VRAM")
                else:
                    print(f"Debug: Instance {instance['InstanceType']} has no GpuInfo or Gpus")
        
        return gpu_instances
    
    def get_instance_pricing(self, instance_type):
        response = self.pricing_client.get_products(
            ServiceCode='AmazonEC2',
            Filters=[
                {'Type': 'TERM_MATCH', 'Field': 'instanceType', 'Value': instance_type},
                {'Type': 'TERM_MATCH', 'Field': 'location', 'Value': 'US East (N. Virginia)'}
            ],
            MaxResults=1
        )
        
        price_list = response['PriceList']
        if not price_list:
            return None
        
        price_item = json.loads(price_list[0])
        on_demand_pricing = price_item['terms']['OnDemand']
        price_dimensions = list(on_demand_pricing.values())[0]['priceDimensions']
        price_per_hour = list(price_dimensions.values())[0]['pricePerUnit']['USD']
        
        return float(price_per_hour)
    
    def get_gpu_instance_details(self):
        gpu_instances = self.list_gpu_instances()
        for instance in gpu_instances:
            instance['price'] = self.get_instance_pricing(instance['instance_type'])
        
        # Sort by total VRAM
        gpu_instances.sort(key=lambda x: x['total_vram'], reverse=True)
        
        return gpu_instances

# Example usage
if __name__ == "__main__":
    aws_api = AWSGPUInstanceAPIWrapper()
    gpu_instances = aws_api.get_gpu_instance_details()
    
    for instance in gpu_instances:
        print(f"Instance Type: {instance['instance_type']}, VRAM: {instance['total_vram']} MiB, Price: ${instance['price']} per hour")

