import azure.functions as func
import logging
from sent2sent import sent2sent

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="sentsim")
def sentsim(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    sent1 = req.params.get('sentA')
    sent2 = req.params.get('sentB')
    if not sent1 or not sent2:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            sent1 = req.params.get('sentA')
            sent2 = req.params.get('sentB')

    if sent1 and sent2:
        output = sent2sent(sent1,sent2)
        return func.HttpResponse(f"Hello, {sent1} and {sent2} are {output} to each other.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )