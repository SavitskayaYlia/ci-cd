import os

x = os.environ.get("PROD_API_KEY", None)

print(f" x = `{x}` len = `{len(x)}`")
