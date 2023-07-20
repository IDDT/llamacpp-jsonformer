# llama-jsonformer
Restrict LLMs to generate structured data including valid json when given a prompt and a schema. Supports objects, arrays, strings, integers, booleans. Additional support for multiple choice answering and list generation.



#### JSON binary classification
```bash
curl -X POST http://127.0.0.1:8000/json -H "Content-Type: application/json"  -d '{"schema": '"$(cat samples/is_planet.json)"', "prompt": "Information about Mercury "}'
```
```json
{"is_planet": true}
```



#### JSON list generation
```bash
curl -X POST http://127.0.0.1:8000/json -H "Content-Type: application/json"  -d '{"schema": '"$(cat samples/planets.json)"', "prompt": "Planets of the solar system are "}'
```
```json
{"planets":["Mercury","Venus","Earth","Mars","Jupiter","Saturn","Uranus","Neptune"]}
```



#### Extracting structured information
```bash
curl -X POST http://127.0.0.1:8000/json -H "Content-Type: application/json"  -d '{"schema": '"$(cat samples/product.json)"', "order": ["product_title", "category", "color_name", "garmant_pattern", "wearing_occasions"], "prompt": "Product described as \"Floral Bow Tie Shoulder Sleeveless Dress - Green\"\nAdditional information follows: "}'
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



#### Structured data generation
```bash
curl -X POST http://127.0.0.1:8000/json -H "Content-Type: application/json"  -d '{"schema": '"$(cat samples/student.json)"', "order": ["is_student", "name", "age"], "prompt": "Hermione Granger "}'
```
```json
{"age":30,"courses":["Study of Magical Creatures","Defense Against the Dark Arts","Transfiguration"],"is_student":true,"name":"Hermione Granger"}
```



### Multiple choice answering
```bash
curl -X POST http://127.0.0.1:8000/choices -H "Content-Type: application/json" -d '{"prompt": "Q: Is Sun a celestial body?\nA: ", "choices": ["yes", "no"]}'
```
```
yes
```



### List generation
```bash
curl -X POST http://127.0.0.1:8000/list -H "Content-Type: application/json" -d '{"prompt": "Following are the planets of the solar system:\n", "n_items": 4, "chars": "A-z"}'
```
- Mercury
- Venus
- Earth
- Mars
```



#### Running locally
```bash
#Get a GGML model and place inside ./temp/
./build.sh
python3 -m venv . && source ./bin/activate && pip3 install -U pip wheel
pip3 install -r requirements.txt
uvicorn src:app --reload
```
