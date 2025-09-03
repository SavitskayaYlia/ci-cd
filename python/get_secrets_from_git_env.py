import os

x = os.environ.get("API_KEY", None)

print(f" x = `{x}` len = `{len(x)}`")
