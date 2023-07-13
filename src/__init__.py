import json
from flask import Flask, request, jsonify
from .grammar import gen_grammar
from .llamacpp import infer


app = Flask(__name__)


@app.route('/', methods=['POST'])
def index():
    body = request.get_json()
    prompt = str(body.get('prompt', ''))
    schema = body.get('schema', {'type': 'object', 'properties': {}})
    key_order = [str(x) for x in body.get('order', [])]
    print(prompt, schema)
    grammar = gen_grammar(schema)
    s = infer(grammar, prompt)
    print(s)
    out = json.loads(s.strip().removeprefix(prompt))
    return jsonify(out)
