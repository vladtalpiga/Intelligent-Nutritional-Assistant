import base64
import os
import requests

def main():
    engine_id = "stable-diffusion-xl-beta-v2-2-2"
    api_host = os.getenv('API_HOST', 'https://api.stability.ai')
    api_key = "sk-nBP582k1Q9KCL7a1Qay3ltiR2L3GYVWa3Yk5BqnCU7XVwwuy"

    if api_key is None:
        raise Exception("Missing Stability API key.")

    folder_list = os.listdir("C:/Users/Vlad Talpiga.VLR_PROJAMZ/OneDrive - Valrom Industrie SRL/Desktop/IAVA/Proiect/FoodClassifier/data/food-101/images")
    for s in folder_list:
        # prompt = f'an image of {s.replace("_", " ")}'
        prompt = f'a realistic image of {s.replace("_", " ")}'


        response = requests.post(
            f"{api_host}/v1/generation/{engine_id}/text-to-image",
            headers={
                "Content-Type": "application/json",
                "Accept": "application/json",
                "Authorization": f"Bearer {api_key}"
            },
            json={
                "text_prompts": [
                    {
                        "text": prompt
                    }
                ],
                "cfg_scale": 7,
                "height": 512,
                "width": 512,
                "samples": 2,
                "steps": 30,
            },
        )

        if response.status_code != 200:
            raise Exception("Non-200 response: " + str(response.text))

        data = response.json()

        os.mkdir(f"test/out/{s}")

        for i, image in enumerate(data["artifacts"]):
            with open(f"test/out/{s}/{i+1}.jpg", "wb") as f:
                f.write(base64.b64decode(image["base64"]))

main()