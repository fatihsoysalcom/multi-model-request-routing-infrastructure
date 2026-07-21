# Multi Model Request Routing Infrastructure

This example demonstrates multi-model routing as an infrastructure decision using a simple Flask application. It simulates multiple machine learning models and implements a central routing mechanism. Incoming requests are directed to the appropriate simulated model based on parameters like user segment or task type, highlighting how routing logic can be a core infrastructure component.

## Language

`python`

## How to Run

1. Install Flask: `pip install Flask`
2. Run the application: `python main.py`
3. Send POST requests to `http://127.0.0.1:5000/predict` with a JSON body. For example:
   - `curl -X POST -H "Content-Type: application/json" -d '{"input": "hello world", "user_segment": "premium"}' http://127.0.0.1:5000/predict`
   - `curl -X POST -H "Content-Type: application/json" -d '{"input": "analyze this", "task_type": "specialized"}' http://127.0.0.1:5000/predict`
   - `curl -X POST -H "Content-Type: application/json" -d '{"input": "default query"}' http://127.0.0.1:5000/predict`

## Original Article

This example accompanies the Turkish article: [Çok Modelli Yönlendirme Bir Özellik mi, Yoksa Altyapı Kararı mı?](https://fatihsoysal.com/blog/cok-modelli-yonlendirme-bir-ozellik-mi-yoksa-altyapi-karari-mi/).

## License

MIT — see [LICENSE](LICENSE).
