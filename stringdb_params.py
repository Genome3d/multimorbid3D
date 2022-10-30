import requests
import json
import pandas as pd
import os

def get_stringapi_info(string_version):
    sdb_df = pd.read_csv(os.path.join(os.path.dirname(__file__), 'data/string_api_urls.txt'), 
        sep='\t')
    url = sdb_df.loc[sdb_df['string_version'] == string_version, 'stable_address'].iloc[0]
    if string_version == 'latest':
        api_info = requests.get(url).text                           
        parse_info = json.loads(api_info)                                                           
        version = parse_info[0]['string_version']
        url = parse_info[0]['stable_address']
    else:
        version = string_version
        url = url
    return "/".join([url, "api"]), version

OUTPUT_FORMAT = "tsv"
GET_IDS = "get_string_ids"
INTERACTION_PARTNERS = "interaction_partners"

PARAMS = {
    "species": 9606,
    "limit": 5,
    "echo_query": 1,
    "caller_identity": ""}

def get_params(gene_list):
    params = PARAMS
    params["identifiers"] = "\r".join([str(gene) for gene in gene_list])
    return params

def get_request_ids_url(API_URL):
    return "/".join([API_URL, OUTPUT_FORMAT, GET_IDS])


def get_request_interaction_url(API_URL):
    return "/".join([API_URL, OUTPUT_FORMAT, INTERACTION_PARTNERS])
