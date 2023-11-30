from bardapi import Bard
import os
import requests
import json

os.environ['_BARD_API_KEY']="dQh7a2VL72hAjugeTpFd5Nbqj6rDSHK1Lyh-tRBnlyY_593F3uD1xFH-UxkCnbyvw1fSsw."

def Comment(file_path):
    
    session = requests.Session()
    session.headers = {
                "Host": "bard.google.com",
                "X-Same-Domain": "1",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
                "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
                "Origin": "https://bard.google.com",
                "Referer": "https://bard.google.com/",
            }
    session.cookies.set("__Secure-1PSID", os.getenv("_BARD_API_KEY")) 

    bard = Bard(token=os.environ['_BARD_API_KEY'], session=session, timeout=30)

    while True:
        # message = str(input("Prompt:[COMMENT|DOCUMENT: ] "))
        message = "comment"
        _message = message.lower()
        if _message=="comment":
            _code = open('./gpt.py')
            code = _code.read()
            _code.close()
            prompt ="Comment the code above"
            final_message = str(code)+"\n"+prompt
            try:
                answer = bard.get_answer(final_message)
                final_answer = answer['content'].split("\n")
                return final_answer,True
                # with open("./output.py",'w') as write_file:
                #     store=answer['content'].split("\n")
                #     for i in range(1,len(store)):
                #         write_file.write(store[i]+"\n")
            except Exception as e:
                return "",False
            

            
        else:
            return "",False



