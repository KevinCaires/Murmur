from gql import Client
from gql.transport.requests import RequestsHTTPTransport

def get_gql_client(url, auth=None):
    """
    Retorna um client de execução de requisições graphql para acesso ao Bill.
    param : auth : <str> : hash de autorização.
    """
    if not auth:
        transport = RequestsHTTPTransport(url=url, use_json=True)
    else:
        headers = {
            'content-type': 'application/json',
            'auth': '{}'.format(auth)
        }
        transport = RequestsHTTPTransport(
            url=url,
            use_json=True,
            headers=headers
        )

    client = Client(transport=transport, fetch_schema_from_transport=False)
    return client
