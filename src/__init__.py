import json
from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route
from .grammar import gen_grammar
from .llamacpp import infer


async def index(request):
    x = await request.json()
    schema = x.get('schema', {'type': 'object', 'properties': {}})
    order = [str(x) for x in x.get('order', [])]
    prompt = str(x.get('prompt', ''))
    grammar = gen_grammar(schema, order)
    out = infer(grammar, prompt).strip().removeprefix(prompt)
    print(out)
    return JSONResponse(json.loads(out))


app = Starlette(debug=True, routes=[
    Route('/', index, methods=['POST'])
])
