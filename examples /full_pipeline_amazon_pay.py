# Full system usage example
from src.ingestion.kafka_consumer import consume_stream
from src.preprocessing.normalization import normalize
from src.detection.vae_model import VAEModel
from src.response.responder import trigger_response
from src.summary_evaluator.llm_wrapper import evaluate_summary

# Step 1: Ingest data
stream = consume_stream("amazon_pay")

# Step 2: Preprocess
for raw_data in stream:
    features = normalize(raw_data['features'])

    # Step 3: Detect anomaly
    vae = VAEModel(input_dim=256, latent_dim=32)
    score = vae.detect(features)

    # Step 4: Respond
    action = trigger_response(score)

    # Step 5: Evaluate analyst summary
    summary = raw_data['analyst_summary']
    feedback = evaluate_summary(summary)

    print(f"Score: {score:.2f} → Action: {action} → Feedback: {feedback}")
