from time import sleep
import openai
import speect_text
import re
import threading



def chatgpt():
    l = []
    code = []
    codes = []
    j = []
    dele = []
    count = 0
    openai.api_key = "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"
    messages = []
    system_msg = "you are an assistant that answers anything i ask and have a conversation like a human and also gives me codes for programmes and"
    messages.append({"role": "system",
                     "content": system_msg + " you will always give different respose and will have a conversation like a human when i am talking to you  and take my name avinav"})
    # messages.append({"role": "user" , "content" :"you will always give different respose and will have a conversation like a human when i am talking to you " })
    # messages.append({"role" : "system" ,"content" : "wrap the code inside <code> </code> when i ask you any code or if their is a code in your response"})
    k = []
    print("i am ready , okey?")

    def talk_like(messages):
        global response
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages)

    for i in range(1):
        message = "okey and give and answer small as possible and your name now is lane and Talk like a human, not as a robot , you are lazy and savage at a a same time and you make jokes quite a lot and you answer like a human"
        messages.append({"role": "user", "content": message})

        talk_like(messages)
        reply = response["choices"][0]["message"]["content"]
        messages.append({"role": "assistant", "content": reply})
        print(reply)

        message = "and try to give savage answers if possible keep our discussion small as possible and also don't response that you are an ai model , say that you are not so matured and informative in that question and if i ever ask for a code or a program or a command  the can you give the title for the programs in a  seprate line that is wrap between <ttl> # here  should be the title </ttl> "
        messages.append({"role": "user", "content": message})

        talk_like(messages)
        reply = response["choices"][0]["message"
        ]["content"]
        messages.append({"role": "assistant", "content": reply})
        print(reply)


    while input != "quit()":

        print("-------------------------")
        message = speect_text.usemic("" , "")
        if "assistant" in message and "mode" in message :
            break
        messages.append({"role": "user", "content": message})
        if "command" in message and "mode" in message :
            break

        talk_like(messages)
        reply = response["choices"][0]["message"]["content"]
        messages.append({"role": "assistant", "content": reply})

        program = reply
        pattern = r'<ttl>(.*?)</ttl>'
        match = re.search(pattern, program, re.DOTALL)
        if match:

            Title_of_code = match.group(1)

            print(Title_of_code)
        else:
            print(reply)


        with open("app.txt", "w") as fs:
            fs.write(reply)

        with open("app.txt", "r") as fs:
            for i in fs.readlines():
                j.append(i)
                if "```" in i:
                    l.append(count)
                count += 1
            count = 0

            if not l:
                pass
            else:
                for k in range(0, len(j)):
                    if k < l[1] and k > l[0]:
                        code.append(j[k])
                    else:
                        codes.append(j[k])

        if not code:
            print(reply)
            speect_text.say(reply)

        else:
            for id in range(0, len(codes)):
                if "```" in codes[id]:
                    dele.append(id)
            for i in range(0, len(dele)):
                codes.pop(dele[0])

            print(f"--------------------------- {l}-----------------------")
            for i in range(0, len(codes)):
                if l[0] == i:
                    for le in code:
                        print(le)
                print(codes[i])
            l = []


def stops():
    while True:
        stopss = speect_text.usemic("", "")
        if stopss == "stop" or stopss == "pause" or stopss == "wait":
            break




