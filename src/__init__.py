import json
import logging
from flask import Flask, request, jsonify
from .grammar import gen_grammar
from .llamacpp import infer


app = Flask(__name__)


@app.route('/', methods=['POST'])
def index():
    body = request.get_json()
    prompt = str(body.get('prompt', ''))
    schema = body.get('schema', {'type': 'object', 'properties': {}})
    order = [str(x) for x in body.get('order', [])]

    # Generate grammar.
    grammar = gen_grammar(schema, order)

    # Run inference.
    s = infer(grammar, prompt)
    logging.info(s)

    # Parse output as json.
    out = json.loads(s.strip().removeprefix(prompt))

    return jsonify(out)
