import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

pipe = pipeline("text-generation", model="stabilityai/StableBeluga-7B")
tokenizer = AutoTokenizer.from_pretrained("stabilityai/StableBeluga2", use_fast=False)


tokenizer = AutoTokenizer.from_pretrained("stabilityai/StableBeluga-7B")
model = AutoModelForCausalLM.from_pretrained("stabilityai/StableBeluga-7B")
system_prompt = "### System:\nYou are Stable Beluga, an AI that follows instructions extremely well. Help as much as you can. Remember, be safe, and don't do anything illegal.\n\n"

message = "Write me a poem please"
prompt = f"{system_prompt}### User: {message}\n\n### Assistant:\n"
inputs = tokenizer(prompt, return_tensors="pt").to("cuda")
output = model.generate(**inputs, do_sample=True, top_p=0.95, top_k=0, max_new_tokens=256)

print(tokenizer.decode(output[0], skip_special_tokens=True))
