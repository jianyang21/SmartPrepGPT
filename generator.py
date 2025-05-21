from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

# Load model and tokenizer
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")

model.eval()  # Disable training

def build_prompt(topic, exam_type, level):
    return f"""
You are an expert tutor helping a {level.lower()} student prepare for a {exam_type.lower()} on the topic: "{topic}".

Generate a list of 5 to 7 high-quality study questions that help the student:
- Understand key concepts
- Apply knowledge
- Prepare for real exam conditions

Respond in a simple numbered list format.
"""

def get_study_prompts(topic, exam_type, level, max_length=200):
    prompt = build_prompt(topic, exam_type, level)
    inputs = tokenizer.encode(prompt, return_tensors="pt")

    with torch.no_grad():
        outputs = model.generate(
            inputs,
            max_length=max_length,
            temperature=0.8,
            top_p=0.95,
            do_sample=True,
            num_return_sequences=1,
            pad_token_id=tokenizer.eos_token_id
        )

    output_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return output_text[len(prompt):].strip()

