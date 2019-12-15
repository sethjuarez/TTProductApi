import json
import logging
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    category = req.route_params['category'].lower()

    products = []

    if category == 'hardware':
        products = [
            {'id': 22, 'Name': 'Hammer', 'Image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/84/Claw-hammer.jpg/1200px-Claw-hammer.jpg'},
            {'id': 34, 'Name': 'Wrench', 'Image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/98/Chrome_Vanadium_Adjustable_Wrench.jpg/1200px-Chrome_Vanadium_Adjustable_Wrench.jpg'}
        ]

    logging.info(json.dumps(products))

    return func.HttpResponse(
            body=json.dumps(products),
            status_code=200
    )
