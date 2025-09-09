### Admin (Streamlit) 

[![My Skills](https://skillicons.dev/icons?i=python)](https://skillicons.dev) 

### 1. Plan Endpoints 
<details>
<summary> 📌 POST /create_plan/ </summary>
  
### Create Plan endpoint

> Request body: 
```json
{
"plan_name": "English A1",
"language": "english",
"level": "A1",
"translation_language": "uzbek",
"icon": "eng"

}
```

> Response (200): 
```json
{
 "plan_id": 233
}
```
</details>



<details>
<summary> 📌 POST /create_words/ </summary>
  
### Create Words endpoint

> Request body: 
```json
{
  "plan_id": 233,
  "words": [
      {"word": "apple", "translation": "olma"},
      {"word": "lion", "translation": "sher"},
      {"word": "tiger", "translation": "yo'lbars"}
  ]
}
```

> Response (200): 
```json
{
 "plan_id": 233
}
```
</details>
