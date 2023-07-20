import json
from starlette.applications import Starlette
from starlette.responses import JSONResponse, PlainTextResponse
from starlette.routing import Route
from .grammar import gen_grammar
from .llamacpp import infer


async def api_choices(request):
    x = await request.json()
    choices = [str(x) for x in x.get('choices', ['yes', 'no'])]
    prompt = str(x.get('prompt', ''))
    grammar = 'root ::= ' + ' | '.join(f'"{x}"' for x in choices)
    out = infer(grammar, prompt).strip().removeprefix(prompt)
    return PlainTextResponse(out)

async def api_list(request):
    x = await request.json()
    prompt = str(x.get('prompt', ''))
    n_items = int(x.get('n_items', 5))
    chars = str(x.get('chars', '0-9A-z'))
    grammar = '\n'.join([
        'root ::= ' + ' '.join('line' for _ in range(n_items)),
        f'line ::= "- " [{chars}]+ "\n"'
    ])
    print(grammar)
    out = infer(grammar, prompt).strip().removeprefix(prompt)
    return PlainTextResponse(out)

async def api_json(request):
    x = await request.json()
    schema = x.get('schema', {'type': 'object', 'properties': {}})
    order = [str(x) for x in x.get('order', [])]
    prompt = str(x.get('prompt', ''))
    grammar = gen_grammar(schema, order)
    out = infer(grammar, prompt).strip().removeprefix(prompt)
    print(out)
    return JSONResponse(json.loads(out))


app = Starlette(debug=True, routes=[
    Route('/choices', api_choices, methods=['POST']),
    Route('/list', api_list, methods=['POST']),
    Route('/json', api_json, methods=['POST'])
])
