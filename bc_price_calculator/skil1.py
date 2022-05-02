import json
from requests import Session


def login():
    data = {"username": "rafik.parsyan", "password": "rafik1998"}
    headers = {"kbn-version": "6.4.2"}
    url = "https://swarm-metrics.betcoapps.com:5601/api/v1/auth/login"
    session = Session()
    response = session.post(url=url, json=data, headers=headers)
    print(response.text)
    print(response.status_code)
    search(session=session)


def search(session):
    url = "https://swarm-metrics.betcoapps.com:5601/elasticsearch/_msearch"
    headers = {"kbn-version": "6.4.2", 'Content-Type': 'application/x-ndjson'}
    d = {"index": "swarmmetrics-*", "ignore_unavailable": True, "timeout": 30000, "preference": 1650611619901}
    query = {"version": True, "size": 500, "sort": [{"@timestamp": {"order": "desc", "unmapped_type": "boolean"}}],
             "_source": {"excludes": []}, "aggs": {"2": {
            "date_histogram": {"field": "@timestamp", "interval": "30s", "time_zone": "Europe/Moscow",
                               "min_doc_count": 1}}}, "stored_fields": ["*"], "script_fields": {},
             "docvalue_fields": [{"field": "@timestamp", "format": "date_time"}], "query": {"bool": {
            "must": [{"query_string": {"query": "\"QUERY-WEIGHT\"", "analyze_wildcard": True, "default_field": "*"}},
                     {"range": {"@timestamp": {"gte": 1650613140000, "lte": 1650613150000, "format": "epoch_millis"}}}],
            "filter": [], "should": [], "must_not": []}},
             "highlight": {"pre_tags": ["@kibana-highlighted-field@"], "post_tags": ["@/kibana-highlighted-field@"],
                           "fields": {"*": {}}, "fragment_size": 2147483647}}
    data = json.dumps(d) + "\n" + json.dumps(query) + "\n"
    print(data)
    response = session.post(url=url, data=data, headers=headers)
    with open('result.json', 'w') as f:
        json.dump(response.json(), f)


login()