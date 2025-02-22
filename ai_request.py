from openai import OpenAI

client = OpenAI(
  api_key="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"
)

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  store=True,
  messages=[
    {"role": "user", "content": "write a haiku about ai"}
  ]
)

print(completion.choices[0].message)
