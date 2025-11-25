## **第七章：開發者指南與 API 整合 (Developer Guide)**

對於資訊工程系的學生或開發者，Nano Banana Pro 提供了強大的 API 接口，可透過 **Vertex AI** 或 **Google AI Studio** 進行調用。

### **7.1 Python SDK 實作範例**

以下是使用 Python 調用 Nano Banana Pro (Gemini 3 Pro Image) 的標準代碼結構 36：

```python
from google import genai  
from google.genai import types  
from PIL import Image

# 初始化客戶端  
client = genai.Client(api_key="YOUR_API_KEY")  
PRO_MODEL_ID = "gemini-3-pro-image-preview"

# 定義 Prompt 與配置  
prompt = "A futuristic city on Mars, cinematic lighting, 4K resolution."  
config = types.GenerateContentConfig(  
    response_modalities=['Image'],  
    image_config=types.ImageConfig(  
        aspect_ratio="16:9",  
        generation_count=1  
    ),  
    # 啟用 Google Search Grounding 以獲得真實數據  
    tools=[{"google_search": {}}]  
)

# 多圖像輸入範例 (最多 14 張)  
input_contents = [  
    prompt,  
    Image.open('reference_style.png'),  
    Image.open('character_sheet.png')  
]

# 發送請求  
response = client.models.generate_content(  
    model=PRO_MODEL_ID,  
    contents=input_contents,  
    config=config  
)

# 儲存結果  
for part in response.parts:  
    if image := part.as_image():  
        image.save("output_mars_city.png")
```

### **7.2 參數調優與最佳實踐**

* **Aspect Ratio (長寬比)：** 透過 aspect_ratio 參數設置，如 "1:1", "16:9", "4:3"。  
* **Thinking Mode：** 在 API 後端，開發者可以看到模型的「思考過程」與中間生成的「草圖」（Thought Images），這有助於除錯 Prompt 的邏輯問題.3  
* **Safety Settings：** 開發者需注意模型的安全過濾器設置，過於敏感的設置可能會誤判正常的藝術創作.38
