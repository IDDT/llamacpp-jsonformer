# llama-jsonformer
Restrict LLMs to generate valid json given a prompt and schema.



#### Request samples
```bash
curl -X POST http://127.0.0.1:5000 -H "Content-Type: application/json"  -d '{"schema": "{"type": "object", "properties": {"is_planet": {"type"}}}", "prompt": "Mercury "}'
```
```bash
curl -X POST http://127.0.0.1:5000 -H "Content-Type: application/json"  -d '{"schema": '"$(cat samples/planets.json)"', "prompt": "Planets of the solar system "}'
```
```json
{"planets":["Mercury","Venus","Earth","Mars","Jupiter","Saturn","Uranus","Neptune"]}
```
Generation depends on previous context, specify key order to control this. Unspecified keys go to the back unordered.
```bash
curl -X POST http://127.0.0.1:5000 -H "Content-Type: application/json"  -d '{"schema": '"$(cat samples/student.json)"', "order": ["is_student", "name", "age"], "prompt": "Hermione Granger "}'
```
```json
```



#### Running locally
```bash
./build.sh
python3 -m venv . && source ./bin/activate && pip3 install -U pip wheel
pip3 install -r requirements.txt
FLASK_APP=src FLASK_DEBUG=1 flask run
```
