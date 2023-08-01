# InputBlaster

We aim at automatically generating a batch of unusual text inputs which can possibly make the mobile apps crash. To achieve this, we propose InputBlaster which leverages LLM to produce the test generators together with the mutation rules which serve as the reasoning chains for boosting the performance, and each test generator then automatically generates a batch of unusual text inputs, as shown in Figure. 
In detail, given a GUI page with text input widgets and its corresponding view hierarchy file, we first leverage LLM to generate the valid text input which can pass the GUI page.


# InputBlaster Source code

## How to use
1. Generate Your API Key: Before we start working with the ChatGPT API, we need to login into OpenAI account and generate our API keys.
   `openai.api_key = "XXXXXXX"`
2. Installing the library: To work with the ChatGPT API, first, we have to install the openai library by running the following command.
3. Using “ChatCompletion” gpt-3.5-turbo, which is the same model used by ChatGPT.
   
   `import os` 
   
   `import openai`
   
   `openai.api_key = os.getenv("OPENAI_API_KEY")`

   `completion = openai.ChatCompletion.create(`
   
   `model="gpt-3.5-turbo",`
     
    `)`

    

4. Appending the users role to the previous list and add the input function in order to interact with the API as if we’re working with ChatGPT.
   
   `import os` 
   
   `import openai`
   
   `content = input("User: ")`

   `messages.append({"role": "user", "content": content})`
   
   `completion = openai.ChatCompletion.create(`

   `model="gpt-3.5-turbo",`
   
   `messages=messages`
   
   `)`


### Requirements
* Android emulator
* Ubuntu or Windows
* Appium Desktop Client: [link](https://github.com/appium/appium-desktop/releases/tag/v1.22.3-4)
* Python 3.7
  * apkutils==0.10.2
  * Appium-Python-Client==1.3.0
  * Levenshtein==0.18.1
  * lxml==4.8.0
  * opencv-python==4.5.5.64
  * sentence-transformers==1.0.3
  * torch==1.6.0
  * torchvision==0.7.0

Use the gpt-3.5.


## structure

![structure](./res/structure.png)

## This example introduces how to use ChatGPT

[a-simple-guide-to-chatgpt-api-with-python](https://medium.com/geekculture/a-simple-guide-to-chatgpt-api-with-python-c147985ae28#id_token=eyJhbGciOiJSUzI1NiIsImtpZCI6ImM5YWZkYTM2ODJlYmYwOWViMzA1NWMxYzRiZDM5Yjc1MWZiZjgxOTUiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL2FjY291bnRzLmdvb2dsZS5jb20iLCJuYmYiOjE2ODMyNjQ1NDksImF1ZCI6IjIxNjI5NjAzNTgzNC1rMWs2cWUwNjBzMnRwMmEyamFtNGxqZGNtczAwc3R0Zy5hcHBzLmdvb2dsZXVzZXJjb250ZW50LmNvbSIsInN1YiI6IjExMTc4NjQ1NDgyMjM3ODU5NTE0NSIsImVtYWlsIjoibWVuZ3podW8uaGFwcHlAZ21haWwuY29tIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsImF6cCI6IjIxNjI5NjAzNTgzNC1rMWs2cWUwNjBzMnRwMmEyamFtNGxqZGNtczAwc3R0Zy5hcHBzLmdvb2dsZXVzZXJjb250ZW50LmNvbSIsIm5hbWUiOiJSb2JpbiBDaGVuIiwicGljdHVyZSI6Imh0dHBzOi8vbGgzLmdvb2dsZXVzZXJjb250ZW50LmNvbS9hL0FHTm15eFlwVnBsVVhlY2lOeEMxd0hlQ3l5eGEyYTh0djBRemdLMzdMcVAtPXM5Ni1jIiwiZ2l2ZW5fbmFtZSI6IlJvYmluIiwiZmFtaWx5X25hbWUiOiJDaGVuIiwiaWF0IjoxNjgzMjY0ODQ5LCJleHAiOjE2ODMyNjg0NDksImp0aSI6IjA0YjQ0YzA3NzA2MmNhOGIxZjUxMDY2MjE5ODllZTI5NWQ3ZTQ4NWEifQ.ZSJupHFC6zap9ybM9ThhtDCVmlRB1OEBXwrA1avqnTjCc3oyZOOnKkJbMBT-Jv1TXX7lWHXW9XAqvPClcCePjHH7xwrxYdJpWsbMzMWU1JOU4zI2t3QMmtWGmBwT6qP9Frq31VBVXqAZ3-X_0mJi7OXtjaPSG93eDkLswF7QFyucB9VEsxJhwlcRY3EVF2K5hhLfRsI58BGlHifdbipeueCCYUVKa4hbYCt_33Per27xZmZdcg0LglnPjq4_zN3ciEyP-pzpxu8O2hbrtW7BqvN2F0m115tTddv3hBwp47DHGRwB1XukoTCJe9gkhhLd3nNqLBmHen3AWRLG0ExY_w)


# Evaluationn

## RQ3 Usefulness evaluation (./Usefulness evaluation/)

The apks confirmed or fixed from usefulness evaluation.

Because the Google Play requires that individuals cannot upload apk without permission. You can download them on Google play through the information in the table.

**ID** | **App name** | **Category** | **Download** | **Status**
 :-: | :-: | :-: | :-: | :-: 
1 | OTOMU | Music | 100M+ | fixed
2 | KWork | Tool | 50M+ | confirmed  
3 | NoxSecu | Tool  | 50M+ | fixed  
4 | EarnMon | Finance | 50M+ | fixed  
5 | RewardM | Finance | 50M+ | confirmed  
6 | AttaPOl | Tool | 10M+  | confirmed  
7 | ISAY | Commun | 10M+  | fixed 
8 | Ipsos | Commun | 10M+  | fixed  
9 | MediaFire | Product | 5M+  | confirmed 
10 | DRBUs | Navig | 500K+ | fixed   
11 | MyTransp | Travel | 500K+ | fixed  
12 | MMDR | Utilities | 500K+ | fixed   
13 | Genting | Travel | 500K+ | pending  
14 | Fair | Health | 500K+ | confirmed   
15 | ClassySha | Tool | 500K+  | pending   
16 | Linphone | Commun | 50K+  | confirmed  
17 | IvyWall | Finance | 50K+  | pending  
18 | Monefy | Finance | 50K+  | fixed  
19 | Spend | Finance | 50K+  | pending  
20 | NYBA | Tool | 50K+  | confirmed  
