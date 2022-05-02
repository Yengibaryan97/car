from elasticsearch import Elasticsearch

es = Elasticsearch(host='https://swarm-metrics.betcoapps.com:5601/app/kibana#/discover?_g=()&_a=(columns:!'
                        '(_source),index:e6c16f50-b217-11ea-a20a-85e6a8c18fed,interval:auto,query:(language:lucene,'
                        'query:''), '
                        'sort:!("@timestamp",desc))', port=9200)

doc = {"message": "QUERY-WEIGHT",
       "source": "betting",
       "index": "swarmmetrics-* "

       }
resp = es.index(doc_type="message", id=1, index="swarmmetrics-* ", body=doc)

res = es.get(doc_type="message", id=1, index="swarmmetrics-* ", body=doc)
