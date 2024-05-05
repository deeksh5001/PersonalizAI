import openai
import gradio as gr

openai.api_key="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"

typeOfBot=input("What type of bot do you need?\n")
messages=[{"role":"system","content":typeOfBot}]


def customChatGPT(user_input,history):
    messages.append({"role":"user","content":user_input})
    response=openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    reply=response["choices"][0]["message"]["content"]
    messages.append({"role":"assistant","content":reply})
    return reply

demo = gr.ChatInterface(fn=customChatGPT,theme='shivi/calm_seafoam')

if __name__ == "__main__":
    demo.launch()


#WORKING GOOD#