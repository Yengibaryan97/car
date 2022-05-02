import os

from google.cloud import billing_v1

# name="projects/swarmcloudstaging",

# Create a client
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/home/rafik/work/billing_dir/credentials.json'
# Create a client
client = billing_v1.CloudBillingClient()
# Initialize request argument(s)
request = billing_v1.GetProjectBillingInfoRequest({"name" : "projects/swarmcloudstaging"})
# Make the request
response = client.get_project_billing_info(request=request)
# Handle the response
print(response)