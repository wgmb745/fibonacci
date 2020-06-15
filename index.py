import json
import datetime

def handler(event, context):
    
    n = int(0)
    triangular = int(0)
    lista = []
    if event is not None:
        n = int(event["queryStringParameters"]["numfib"])
        a, b = 0,1
        while a < n:
            lista.append(a)
            a, b = b, a+b
            
        triangular = int((n*(n+1)/2))
    else:
        lista.append('No se definio un parametro para inicio')
    
    data = {
        'numero':n,
        'fibonacci':lista,
        'triangular':triangular,
        'output': 'Hello World',
        'timestamp': datetime.datetime.utcnow().isoformat()
    }
    return {'statusCode': 200,
            'body': json.dumps(data),
            'headers': {'Content-Type': 'application/json'}}
