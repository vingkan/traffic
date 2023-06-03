from prometheus_api_client import PrometheusConnect

prometheus_url = ""
client = PrometheusConnect(url=prometheus_url)

query = 'histogram_quantile(0.95, sum(rate(response_latency_bucket{job="fastapi"}[5m])) by (le, endpoint))'
result = client.custom_query(query)

data = result["data"]["result"]
for item in data:
    endpoint = item["metric"]["endpoint"]
    quantile_value = item["value"][1]
    print(f"Endpoint: {endpoint}, 95th Percentile Latency: {quantile_value}")
