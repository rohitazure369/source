import json
import boto3

fhclient = boto3.client('firehose')
streamname = 'JSONData'
filename = "peopleData1.json"
with open(filename) as json_file:
    observations = json.load(json_file)
    for observation in observations:
        print(observation)
        newline =  str(observation) + '\n'

        response = fhclient.put_record(
           DeliveryStreamName = streamname,
           Record={
                'Data': newline
            }
        )
       
        print(newline)

