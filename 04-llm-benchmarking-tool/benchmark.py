import os
import time
import csv
from google import genai

client = genai.Client()

test_prompt = "Generate a complex 200-word software test plan for a mobile banking login page."

# We will test Gemini 1.5 Flash (Fast/Cheap) vs Gemini 1.5 Pro (Heavy/Expensive)
models_to_test = ['gemini-1.5-flash', 'gemini-1.5-pro']
results = []

print("📊 Starting LLM Performance Benchmarking Suite...")

for model_name in models_to_test:
    print(f"⚡ Testing performance of model: {model_name}...")
    
    # Start the clock to measure latency
    start_time = time.time()
    
    response = client.models.generate_content(
        model=model_name,
        contents=test_prompt,
    )
    
    # Calculate exactly how many seconds it took to respond
    end_time = time.time()
    latency_seconds = round(end_time - start_time, 2)
    
    # Calculate word count to measure throughput velocity
    word_count = len(response.text.split())
    
    results.append({
        "Model": model_name,
        "Latency_Seconds": latency_seconds,
        "Output_Word_Count": word_count
    })

# Save the benchmark analytics to a CSV file for engineering leadership
output_file = "llm_performance_metrics.csv"
with open(output_file, mode='w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=["Model", "Latency_Seconds", "Output_Word_Count"])
    writer.writeheader()
    writer.writerows(results)

print(f"\n📈 Performance assessment complete! Metrics exported to {output_file}")
for r in results:
    print(f"👉 {r['Model']}: Took {r['Latency_Seconds']}s to generate {r['Output_Word_Count']} words.")
