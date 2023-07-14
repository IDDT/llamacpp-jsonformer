# llama-jsonformer
Restrict LLMs to generate valid json given a prompt and schema. Supports objects, arrays, strings, integers, booleans.



#### Binary classification
```bash
curl -X POST http://127.0.0.1:5000 -H "Content-Type: application/json"  -d '{"schema": '"$(cat samples/is_planet.json)"', "prompt": "Information about Mercury "}'
```
```json
{"is_planet": true}
```



#### Knowledge extraction
```bash
curl -X POST http://127.0.0.1:5000 -H "Content-Type: application/json"  -d '{"schema": '"$(cat samples/planets.json)"', "prompt": "Planets of the solar system are "}'
```
```json
{"planets":["Mercury","Venus","Earth","Mars","Jupiter","Saturn","Uranus","Neptune"]}
```



#### Text parsing
```bash
curl -X POST http://127.0.0.1:5000 -H "Content-Type: application/json"  -d '{"schema": '"$(cat samples/product.json)"', "order": ["product_title", "category", "color_name", "garmant_pattern", "wearing_occasions"], "prompt": "Product described as \"Floral Bow Tie Shoulder Sleeveless Dress - Green\"\nAdditional information follows: "}'
```
```json
{
  "category": "dresses",
  "color_name": "Green",
  "search_queries": [
    "Floral Bow Tie",
    "Shoulder Sleeveless Dress",
    "Sleeveless Dress"
  ],
  "title": "Floral Bow Tie Shoulder Sleeveless Dress - Green",
  "wearing_occasions": [
    "Prom",
    "Party",
    "Evening event",
    "Cocktail Party"
  ]
}
```


#### Sample data generatio1n
```bash
curl -X POST http://127.0.0.1:5000 -H "Content-Type: application/json"  -d '{"schema": '"$(cat samples/student.json)"', "order": ["is_student", "name", "age"], "prompt": "Hermione Granger "}'
```
```json
{"age":30,"courses":["Study of Magical Creatures","Defense Against the Dark Arts","Transfiguration"],"is_student":true,"name":"Hermione Granger"}
```



#### Running locally
```bash
#Get a GGML model.
./build.sh
python3 -m venv . && source ./bin/activate && pip3 install -U pip wheel
pip3 install flask
FLASK_APP=src FLASK_DEBUG=1 flask run
```
