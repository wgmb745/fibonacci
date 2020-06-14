import json
import datetime

def handler(event, context):
    
    n = int(1000)
    if event is not None:
        n = int(event["queryStringParameters"]["numfib"])
    lista = []
    cadena = ''
    a, b = 0,1
    while a < n:
        #print(a, end=' ')
        cadena = cadena + str(a) + ' '
        a, b = b, a+b
    lista.append(cadena)
    
    data = {
        'result':lista,
        'output': 'Hello World',
        'timestamp': datetime.datetime.utcnow().isoformat()
    }
    return {'statusCode': 200,
            'body': json.dumps(data),
            'headers': {'Content-Type': 'application/json'}}
