
import db
def do_search(word):

    ind = db.indexes.find({"index": word})
    docs_list = []
    for i in ind:
        i.pop('_id', None)
        i.pop('index', None)
        docs_list.append(i)

    return docs_list
