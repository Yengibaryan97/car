from google.cloud import billing_v1
import os
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/home/rafik/work/billing_dir/credentials.json'
client = billing_v1.CloudBillingClient()

# Initialize request argument(s)
request = billing_v1.ListProjectBillingInfoRequest(
    {"name": "billingAccounts/000F3D-1281FE-E3E563"},
)

# Make the request
page_result = client.list_project_billing_info(request=request)

# Handle the response
for response in page_result:
    print(response)