from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport

_transport = RequestsHTTPTransport(
    url='http://127.0.0.1:8000/graphql/',
    use_json=True,
)


client = Client(
    transport=_transport,
    fetch_schema_from_transport=True,
)
query = gql("""
{
    
        allCategories{
            edges{node{id,name}}
        }
    
    }
""")

print(client.execute(query))