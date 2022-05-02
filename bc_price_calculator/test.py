import os

from google.cloud import bigquery

credention_path = "/home/rafik/Downloads/skilBq.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credention_path

client = bigquery.Client()
table_id = "skil-348713.skilTest.skilTest1"

# rows_to_insert = [
#     {u'name': 'Armen', u'surname': 'Armenyan'},
#     {u'name': 'Ashot', u'surname': 'Ashotyan'},
#     {u'name': 'Suren', u'surname': 'Surenyan'}
# ]
#
# errors = client.insert_rows_json(table_id, rows_to_insert)
# if errors == []:
#     print("NEW row")
# else:
#     print(f"{errors}")
query_job = client.query("""SELECT * FROM `skil-348713.skilTest.skilTest1`""")
results = query_job.result()
for row in results:
    print(row.name, row.surname)
