from flask import Flask, request, jsonify

app = Flask(__name__)

# --- Simulated Machine Learning Models ---
# These functions represent different ML models that would typically
# be loaded and executed. For this example, they return simple strings.
def model_a_predict(data):
    """Simulates Model A, potentially optimized for 'premium' users or specific features."""
    return f"Prediction from Model A for data: '{data}' (Premium Strategy)"

def model_b_predict(data):
    """Simulates Model B, a default model for 'standard' users or A/B test group B."""
    return f"Prediction from Model B for data: '{data}' (Standard Strategy)"

def model_c_predict(data):
    """Simulates Model C, a specialized model for unique tasks or edge cases."""
    return f"Prediction from Model C for data: '{data}' (Specialized Task Strategy)"

# --- Multi-Model Routing Infrastructure ---
@app.route('/predict', methods=['POST'])
def predict():
    """
    This endpoint serves as the central multi-model router.
    It inspects incoming requests to determine which underlying model to invoke.
    This routing logic is treated as an infrastructure component, not application logic.
    """
    request_data = request.json
    if not request_data or 'input' not in request_data:
        return jsonify({"error": "Missing 'input' in request body"}), 400

    # Extract routing criteria from the request
    user_segment = request_data.get('user_segment', 'standard').lower()
    task_type = request_data.get('task_type', None)
    input_data = request_data['input']

    # --- Core Routing Logic ---
    # This decision-making process is the 'multi-model routing' infrastructure.
    # It can be based on various factors like user attributes, A/B test groups,
    # specific task requirements, feature flags, or model versions.
    if user_segment == 'premium':
        # Route to Model A for users identified as 'premium'
        prediction = model_a_predict(input_data)
        model_used = "Model A"
    elif task_type == 'specialized':
        # Route to Model C for specialized tasks, potentially overriding other criteria
        prediction = model_c_predict(input_data)
        model_used = "Model C"
    else:
        # Default route to Model B for standard users or unspecified cases
        prediction = model_b_predict(input_data)
        model_used = "Model B"

    return jsonify({
        "input": input_data,
        "user_segment": user_segment,
        "task_type": task_type,
        "model_used": model_used,
        "prediction": prediction
    })

@app.route('/')
def index():
    return "Multi-Model Routing Example. Send POST requests to /predict with JSON data."

if __name__ == '__main__':
    # For production deployments, use a WSGI server like Gunicorn or uWSGI.
    # For this example, Flask's built-in development server is sufficient.
    app.run(debug=True, port=5000)
