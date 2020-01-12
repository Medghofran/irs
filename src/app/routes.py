from app import app
from flask import request
from irs import querySearch


@app.route('/')
@app.route('/search')
def search():
    query = request.args.get('query', default="", type=str)
    print(query)
    queryRelatedDocs = querySearch(query)
    print(queryRelatedDocs)
    if queryRelatedDocs == None:
        return "ERROR"
    result = {"documents": queryRelatedDocs}
    return result
